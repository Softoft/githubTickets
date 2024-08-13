import asyncio
import datetime
import logging
import os
from typing import Optional, List

import aiohttp
from tenacity import retry, stop_after_attempt, retry_if_exception_type, wait_exponential

from src.github_tickets.myissue import MyIssue, AnswerData

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_ISSUE_PAT")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}"
}


class RateLimitExceeded(Exception):
    pass


class GithubRepoFetcher:
    def __init__(self,
                 repo_name: str,
                 positive_labels: Optional[List[str]] = None,
                 negative_labels: Optional[List[str]] = None,
                 max_issues: int = 20,
                 min_body_word_count: int = 20,
                 max_body_word_count: int = 150,
                 min_answer_word_count: int = 20,
                 max_answer_word_count: int = 150,
                 max_comments_count: int = 4):
        self.repo_name = repo_name
        self.positive_labels = positive_labels
        self.negative_labels = negative_labels
        self.max_issues = max_issues
        self.min_body_word_count = min_body_word_count
        self.max_body_word_count = max_body_word_count
        self.min_answer_word_count = min_answer_word_count
        self.max_answer_word_count = max_answer_word_count
        self.max_comments_count = max_comments_count
        self.current_issue_page_url = ""

    def construct_search_query(self) -> str:
        query_parts = [f"repo:{self.repo_name}", "is:issue", "is:closed"]

        if self.positive_labels:
            query_parts.append(f"label:" + ",".join([f'"{label}"' for label in self.positive_labels]))

        if self.negative_labels:
            query_parts += [f"-label:\"{label}\"" for label in self.negative_labels]

        query_parts.append(f"comments:<={self.max_comments_count}")

        return " ".join(query_parts)

    @retry(stop=stop_after_attempt(100),
           wait=wait_exponential(min=datetime.timedelta(minutes=2), max=datetime.timedelta(hours=1)),
           retry=retry_if_exception_type(RateLimitExceeded))
    async def fetch_issue_data(self, session: aiohttp.ClientSession, issue_url: str) -> Optional[MyIssue]:
        async with (session.get(issue_url, headers=HEADERS) as response):
            if response.status == 200:
                issue_data = await response.json()
                if not self._is_valid_issue(issue_data):
                    return None

                comments_data = await self._get_comments(session, issue_data['comments_url'])
                if comments_data is None or len(comments_data) == 0:
                    return None
                first_answer_body = comments_data[0]['body']
                first_answer_time = datetime.datetime.strptime(comments_data[0]['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                first_answer_author = comments_data[0]['user']['login']
                first_answer = AnswerData(body=first_answer_body, creation_time=first_answer_time,
                                          author=first_answer_author)
                if first_answer is None:
                    return None

                first_answer_words = first_answer.body.split()
                if not self.min_answer_word_count <= len(first_answer_words) <= self.max_answer_word_count:
                    return None

                was_closed_after_first_comment = issue_data['state'] == 'closed' and issue_data['comments'] == 1

                return MyIssue(
                    title=issue_data['title'],
                    repo_name=self.repo_name,
                    url=issue_data['html_url'],
                    first_answer=first_answer,
                    author_name=issue_data['user']['login'],
                    question_body=issue_data['body'] or "",
                    labels=[label['name'] for label in issue_data['labels']],
                    comments=issue_data['comments'],
                    comments_data=comments_data,
                    issue_creation_time=datetime.datetime.strptime(issue_data['created_at'], '%Y-%m-%dT%H:%M:%SZ'),
                    was_closed_after_first_comment=was_closed_after_first_comment
                )
            elif response.status == 403 or response.status == 429:
                logging.info("Rate limit exceeded")
                raise RateLimitExceeded()
            else:
                logging.error(f"Failed to fetch issue data from {issue_url}")
                logging.error(f"Response status: {response.status}")

    @retry(stop=stop_after_attempt(100),
           wait=wait_exponential(min=datetime.timedelta(minutes=2), max=datetime.timedelta(hours=1)),
           retry=retry_if_exception_type(RateLimitExceeded))
    async def _get_comments(self, session: aiohttp.ClientSession, comments_url: str) -> Optional[list[dict]]:
        async with session.get(comments_url, headers=HEADERS, params={"per_page": 10}) as response:
            if response.status == 200:
                try:
                    return await response.json()
                except Exception as e:
                    logging.error(f"Failed to parse comments from {comments_url}")
                    logging.error(e)
                    return None

            elif response.status == 403 or response.status == 429:
                raise RateLimitExceeded()
            else:
                logging.error(f"Failed to fetch comments from {comments_url}")
            return None

    def _is_valid_issue(self, issue_data: dict) -> bool:
        body_words = (issue_data['body'] or "").split()
        return self.min_body_word_count <= len(body_words) <= self.max_body_word_count

    @retry(stop=stop_after_attempt(100),
           wait=wait_exponential(min=datetime.timedelta(minutes=2), max=datetime.timedelta(hours=1)),
           retry=retry_if_exception_type(RateLimitExceeded))
    async def get_next_issue_page(self, session, params):
        logging.info(f"Fetching issues from {self.current_issue_page_url}")
        issues = []
        async with session.get(self.current_issue_page_url, headers=HEADERS, params=params) as response:

            if response.status == 200:
                search_results = await response.json()
                logging.info("total count: " + str(search_results["total_count"]))
                issue_urls = [item['url'] for item in search_results['items']]

                tasks = [self.fetch_issue_data(session, issue_url) for issue_url in issue_urls]
                new_issues = await asyncio.gather(*tasks)
                issues.extend([issue for issue in new_issues if issue is not None])

                if 'next' not in response.links:
                    self.current_issue_page_url = None
                else:
                    self.current_issue_page_url = response.links['next']['url']
                return issues
            elif response.status == 403 or response.status == 429:
                logging.info("Rate limit exceeded")
                raise RateLimitExceeded()

            else:
                logging.error(f"Failed to fetch issues from {self.current_issue_page_url}")
                logging.error(f"Response status: {response.status}")
                return issues

    async def search_issues(self):
        search_query = self.construct_search_query()
        logging.info(f"Searching for issues in {self.repo_name} with query: {search_query}")
        self.current_issue_page_url = f"{GITHUB_API_URL}/search/issues"
        params = {"q": search_query, "per_page": 100}

        issues = []
        async with aiohttp.ClientSession() as session:
            while len(issues) < self.max_issues and self.current_issue_page_url is not None:
                new_issues = await self.get_next_issue_page(session, params)
                for issue in new_issues:
                    yield issue

    def __hash__(self):
        return hash(
            hash(self.repo_name) * hash(frozenset(self.positive_labels)) * hash(frozenset(self.negative_labels)))

    def __eq__(self, other):
        return hash(self) == hash(other)
