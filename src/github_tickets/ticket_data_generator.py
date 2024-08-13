import json
import logging
from typing import List

from github_tickets.github_repo_fetcher import GithubRepoFetcher


class TicketDataGenerator:
    def __init__(self, repo_fetchers: List[GithubRepoFetcher], file_name: str):
        self.repo_fetchers = repo_fetchers
        self.file_name = file_name
        self.issues = []

    def add_new_issue(self, issue):
        self.issues.append(issue)
        self.save_to_file()

    async def generate_ticket_data(self):
        all_issues = []
        for repo_fetcher in self.repo_fetchers:
            try:
                async for issue in repo_fetcher.search_issues():
                    self.issues.append(issue)
            except Exception as e:
                logging.error(f"Error in {repo_fetcher.repo_name}: {e}")
        return all_issues

    def save_to_file(self):
        dict_issues = [issue.to_dict() for issue in self.issues]
        json.dump(dict_issues, open(self.file_name, 'w'))
