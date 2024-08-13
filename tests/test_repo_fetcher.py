import logging

import pytest


@pytest.mark.asyncio
async def test_search_issues(github_issue_fetcher):
    for issue in await github_issue_fetcher.search_issues():
        logging.info(issue)
