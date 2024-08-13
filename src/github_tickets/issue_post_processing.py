import asyncio
import json

from github_tickets.ai_issue_test import IssueAI
from github_tickets.myissue import MyIssue


class IssuePostProcessing:
    def __init__(self):
        self.ai_issue_tester = IssueAI()

    def read_issues(self) -> list[MyIssue]:
        with open("../../results/all_issues.json") as file:
            issue_list = json.load(file)
        return [MyIssue.from_dict(issue) for issue in issue_list]

    async def get_ticket_like_issues(self):
        issues: list[MyIssue] = self.read_issues()

        ticket_like_issues = []

        is_ticket_like_issue = await asyncio.gather(*[self.ai_issue_tester.is_ticket_like(issue) for issue in issues])

        for issue, is_ticket_like in zip(issues, is_ticket_like_issue):
            if is_ticket_like:
                ticket_like_issues.append(issue)
        return ticket_like_issues

    async def save_ticket_like_issues(self):
        ticket_like_issues = await self.get_ticket_like_issues()
        with open("../../results/ticket_like_issues.json", "w") as file:
            json.dump([issue.to_dict() for issue in ticket_like_issues], file, indent=4)
