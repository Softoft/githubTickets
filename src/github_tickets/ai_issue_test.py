import openai
from openai import AsyncOpenAI

from github_tickets.myissue import MyIssue


ISSUE_PROMPT = """
Rate this Github Issue on how much it is like a support ticket
10 meaning it is very much like a support ticket and 0 meaning it is not like a support ticket at all.
In a support ticket, there is a question or a problem that needs to be solved.
From a Customer or a User.
In the answer an agent working for the company provides a solution or an answer.
Answer only with a number from 0 to 10.
The issue to rate is this one:
"""


class IssueAI:
    def __init__(self):
        self.model = AsyncOpenAI()

    async def rate_issue(self, issue: MyIssue) -> float:
        prompt = await self.model.chat.completions.create(
            messages=[
                {"role": "system", "content": f"{ISSUE_PROMPT}"},
                {"role": "user", "content":
                    f"Title: {issue.title}\n"
                    f"Question: {issue.question_body[:200]}\n"
                    f"Answer: {issue.first_answer.body[:200]}\n"
                 },
            ],
            model="gpt-4o-mini"
        )
        return int(prompt.choices[0].message.content)

    async def is_ticket_like(self, issue: MyIssue) -> bool:
        rate = await self.rate_issue(issue)
        return rate >= 8

