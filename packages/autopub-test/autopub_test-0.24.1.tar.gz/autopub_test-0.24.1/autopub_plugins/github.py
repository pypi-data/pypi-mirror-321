import json
import os
import pathlib
import textwrap
from functools import cached_property
from typing import Optional, TypedDict

from autopub.exceptions import AutopubException
from autopub.plugins import AutopubPlugin
from autopub.types import ReleaseInfo
from github import Github
from github.PullRequest import PullRequest
from github.Repository import Repository


class PRContributors(TypedDict):
    pr_author: str
    additional_contributors: set[str]
    reviewers: set[str]


class Sponsors(TypedDict):
    sponsors: set[str]
    private_sponsors: int


class GithubPlugin(AutopubPlugin):
    def __init__(self) -> None:
        super().__init__()
        # Get GitHub token from environment
        self.github_token = os.environ.get("GITHUB_TOKEN")
        if not self.github_token:
            raise AutopubException("GITHUB_TOKEN environment variable is required")

        # Get repository and PR information from GitHub Actions environment
        self.repository = os.environ.get("GITHUB_REPOSITORY")

    @cached_property
    def _github(self) -> Github:
        return Github(self.github_token)

    @cached_property
    def _event_data(self) -> Optional[dict]:
        event_path = os.environ.get("GITHUB_EVENT_PATH")
        if not event_path:
            return None

        with open(event_path) as f:
            return json.load(f)

    def _get_pr_number(self) -> Optional[int]:
        if not self._event_data:
            return None

        if self._event_data.get("event_name") in [
            "pull_request",
            "pull_request_target",
        ]:
            return self._event_data["pull_request"]["number"]

        if self._event_data.get("pull_request"):
            return self._event_data["pull_request"]["number"]

        sha = self._event_data["commits"][0]["id"]
        g = Github(self.github_token)
        repo: Repository = g.get_repo(self.repository)

        commit = repo.get_commit(sha)

        pulls = commit.get_pulls()

        try:
            first_pr = pulls[0]
        except IndexError:
            return None

        return first_pr.number

    def _update_or_create_comment(
        self, text: str, pr_number: int, marker: str = "<!-- autopub-comment -->"
    ) -> None:
        """Update or create a comment on the current PR with the given text."""
        print(f"Updating or creating comment on PR {pr_number} in {self.repository}")
        repo: Repository = self._github.get_repo(self.repository)
        pr: PullRequest = repo.get_pull(pr_number)

        # Look for existing autopub comment
        comment_body = f"{marker}\n{text}"

        # Search for existing comment
        for comment in pr.get_issue_comments():
            if marker in comment.body:
                # Update existing comment
                comment.edit(comment_body)
                return

        # Create new comment if none exists
        pr.create_issue_comment(comment_body)

    def _get_sponsors(self, pr_number: int) -> Sponsors:
        query = """
            query GetSponsors($organization: String!) {
                organization(login: $organization) {
                    sponsorshipsAsMaintainer(
                        first: 100
                        includePrivate: true
                        activeOnly: true
                    ) {
                        nodes {
                            privacyLevel
                            sponsorEntity {
                                __typename
                                ... on User {
                                login
                            }
                            ... on Organization {
                                login
                                }
                            }
                        }
                    }
                }
            }
        """

        repo: Repository = self._github.get_repo(self.repository)
        # TODO: this is assuming that the repository is owned by an organization
        # TODO: there might be some permission issues in some cases
        _, response = self._github.requester.graphql_query(
            query, {"organization": repo.organization.login}
        )

        sponsors = set()
        private_sponsors = 0

        for node in response["data"]["organization"]["sponsorshipsAsMaintainer"]["nodes"]:
            if node["privacyLevel"] == "PUBLIC":
                sponsors.add(node["sponsorEntity"]["login"])
            else:
                private_sponsors += 1

        return Sponsors(
            sponsors=sponsors,
            private_sponsors=private_sponsors,
        )

    def _get_discussion_category_id(self) -> str:
        repo: Repository = self._github.get_repo(self.repository)

        category_name = "Announcements"

        query = """
            query GetDiscussionCategoryId($owner: String!, $repositoryName: String!) {
                repository(owner: $owner, name: $repositoryName) {
                    discussionCategories(first:100) {
                        nodes {
                            name
                            id
                        }
                    }
                }
            }
        """

        _, response = self._github.requester.graphql_query(
            query,
            {
                "owner": repo.owner.login,
                "repositoryName": repo.name,
            },
        )

        for node in response["data"]["repository"]["discussionCategories"]["nodes"]:
            if node["name"] == category_name:
                return node["id"]

        raise AutopubException(f"Discussion category {category_name} not found")

    def _create_discussion(self, pr_number: int) -> None:
        mutation = """
        mutation CreateDiscussion($repositoryId: ID!, $categoryId: ID!, $body: String!, $title: String!) {
            createDiscussion(input: {repositoryId: $repositoryId, categoryId: $categoryId, body: $body, title: $title}) {
                discussion {
                    id
                }
            }
        }
        """

        repo: Repository = self._github.get_repo(self.repository)


        _, response = self._github.requester.graphql_query(
            mutation,
            {
                # TODO: repo.node_id is not yet been published to pypi
                "repositoryId": repo.raw_data["node_id"],
                "categoryId": self._get_discussion_category_id(),
                "body": self.release_info.release_notes,
                "title": f"Release {self.release_info.version}",
            },
        )

        print(response)

    def _get_pr_contributors(self, pr_number: int) -> PRContributors:
        repo: Repository = self._github.get_repo(self.repository)
        pr: PullRequest = repo.get_pull(pr_number)

        pr_author = pr.user.login
        pr_contributors = PRContributors(
            pr_author=pr_author,
            additional_contributors=set(),
            reviewers=set(),
        )

        for commit in pr.get_commits():
            if commit.author.login != pr_author:
                pr_contributors["additional_contributors"].add(commit.author.login)

            for commit_message in commit.commit.message.split("\n"):
                if commit_message.startswith("Co-authored-by:"):
                    author = commit_message.split(":")[1].strip()
                    author_login = author.split(" ")[0]

                    if author_login != pr_author:
                        pr_contributors["additional_contributors"].add(author_login)

        for review in pr.get_reviews():
            if review.user.login != pr_author:
                pr_contributors["reviewers"].add(review.user.login)

        return pr_contributors

    def on_release_notes_valid(
        self, release_info: ReleaseInfo
    ) -> None:  # pragma: no cover
        pr_number = self._get_pr_number()

        if pr_number is None:
            return

        contributors = self._get_pr_contributors(pr_number)
        sponsors = self._get_sponsors(pr_number)
        discussion_category_id = self._get_discussion_category_id()

        message = textwrap.dedent(
            f"""
            ## {release_info.version}

            {release_info.release_notes}

            This release was contributed by {contributors} in #{pr_number}
            
            Sponsors: {sponsors}

            Discussion: {discussion_category_id}
            """
        )

        self._update_or_create_comment(message, pr_number)

    def on_release_notes_invalid(
        self, exception: AutopubException
    ) -> None:  # pragma: no cover
        pr_number = self._get_pr_number()

        if pr_number is None:
            return

        self._update_or_create_comment(str(exception), pr_number)

    def _get_release_message(self) -> str:
        release_info = self.release_info
        pr_number = self._get_pr_number()
        contributors = self._get_pr_contributors(pr_number)
        sponsors = self._get_sponsors(pr_number)

        message = textwrap.dedent(
            f"""
            ## {release_info.version}

            {release_info.release_notes}

            This release was contributed by @{contributors['pr_author']} in #{pr_number}
            """
        )

        if contributors["additional_contributors"]:
            additional_contributors = [f"@{contributor}" for contributor in contributors["additional_contributors"]]
            message += f"\n\nAdditional contributors: {', '.join(additional_contributors)}"

        if contributors["reviewers"]:
            reviewers = [f"@{reviewer}" for reviewer in contributors["reviewers"]]
            message += f"\n\nReviewers: {', '.join(reviewers)}"

        if sponsors["sponsors"]:
            sponsors = [f"@{sponsor}" for sponsor in sponsors["sponsors"]]
            message += f"\n\nThanks to {', '.join(sponsors)}"
            if sponsors["private_sponsors"]:
                message += f" and the {sponsors['private_sponsors']} private sponsor(s)"

            message += " for making this release possible ✨"

        return message

    def _create_release(self, release_info: ReleaseInfo) -> None:
        message = self._get_release_message()

        repo: Repository = self._github.get_repo(self.repository)
        release = repo.create_git_release(
            tag=release_info.version,
            name=release_info.version,
            message=message,
        )

        for asset in pathlib.Path("dist").glob("*"):
            if asset.suffix in [".tar.gz", ".whl"]:
                release.upload_asset(str(asset))

    def post_publish(self, release_info: ReleaseInfo) -> None:
        text = f"This PR was published as {release_info.version}"
        pr_number = self._get_pr_number()

        if pr_number is None:
            return

        self._update_or_create_comment(
            text, pr_number, marker="<!-- autopub-comment-published -->"
        )

        self._create_release(release_info)
        self._create_discussion(pr_number)
