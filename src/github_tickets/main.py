import asyncio
import logging

from github_tickets.github_repo_fetchers import REPO_FETCHERS
from github_tickets.issue_post_processing import IssuePostProcessing
from github_tickets.ticket_data_generator import TicketDataGenerator


def issue_post_processing():
    issue_post_processor = IssuePostProcessing()
    asyncio.run(issue_post_processor.save_ticket_like_issues())


def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
    asyncio.run(TicketDataGenerator(repo_fetchers=REPO_FETCHERS,
                                    file_name="../../results/all_issues.json").generate_ticket_data())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
    main()
    # issue_post_processing()
