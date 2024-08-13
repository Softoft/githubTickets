import datetime
from typing import Optional


class AnswerData:
    def __init__(self, author: str, body: str, creation_time: datetime.datetime):
        self.author = author
        self.body = body
        self.creation_time = creation_time

    def __repr__(self):
        return (f"Author: {self.author}\n"
                f"Body: {self.body[:200]}...\n"
                f"Creation Time: {self.creation_time}\n")


class MyIssue:
    def __init__(self,
                 repo_name: str,
                 title: str, url: str, author_name: str,
                 question_body: str, labels: list[str], comments: int,
                 comments_data: list[dict],
                 issue_creation_time: datetime.datetime,
                 first_answer: AnswerData,
                 was_closed_after_first_comment: Optional[bool]):
        self.repo_name = repo_name
        self.title = title
        self.url = url
        self.first_answer = first_answer
        self.author_name = author_name
        self.question_body = question_body
        self.labels = labels
        self.comments = comments
        self.comments_data = comments_data
        self.issue_creation_time = issue_creation_time
        self.was_closed_after_first_comment = was_closed_after_first_comment

    def __repr__(self):
        return (f"Issue Title: {self.title}\n"
                f"URL: {self.url}\n"
                f"Author: {self.author_name}\n"
                f"Question Body: {self.question_body[:200]}...\n"
                f"First Answer: {self.first_answer}\n"
                f"Was Closed After First Comment: {self.was_closed_after_first_comment}\n"
                f"Comments: {self.comments}\n"
                f"Comments Data: {self.comments_data}\n"
                f"Labels: {', '.join(self.labels)}\n"
                f"Issue Creation Time: {self.issue_creation_time}\n")

    def to_dict(self):
        return {
            "title": self.title,
            "repo_name": self.repo_name,
            "url": self.url,
            "author_name": self.author_name,
            "question_body": self.question_body,
            "labels": self.labels,
            "comments": self.comments,
            "comments_data": self.comments_data,
            "issue_creation_time": self.issue_creation_time.isoformat(),
            "first_answer_author": self.first_answer.author,
            "first_answer_body": self.first_answer.body,
            "first_answer_creation_time": self.first_answer.creation_time.isoformat(),
            "was_closed_after_first_comment": self.was_closed_after_first_comment
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            url=data["url"],
            repo_name=data["repo_name"],
            author_name=data["author_name"],
            question_body=data["question_body"],
            labels=data["labels"],
            comments=data["comments"],
            issue_creation_time=datetime.datetime.fromisoformat(data["issue_creation_time"]),
            first_answer=AnswerData(
                author=data["first_answer_author"],
                body=data["first_answer_body"],
                creation_time=datetime.datetime.fromisoformat(data["first_answer_creation_time"])
            ),
            comments_data=data["comments_data"],
            was_closed_after_first_comment=data["was_closed_after_first_comment"]
        )
