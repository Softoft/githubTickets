import logging

import pytest

from github_tickets.github_repo_fetcher import GithubRepoFetcher

POSITIVE_LABELS = [
    "bug",
]
NEGATIVE_LABLES = [
    "invalid",
]


@pytest.fixture
def github_issue_fetcher():
    return GithubRepoFetcher("microsoft/vscode", positive_labels=POSITIVE_LABELS,
                             negative_labels=NEGATIVE_LABLES, max_issues=10)


@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
