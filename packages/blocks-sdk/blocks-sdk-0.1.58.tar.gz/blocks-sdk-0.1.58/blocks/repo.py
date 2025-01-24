from .config import Config
from .github import GithubRepoProvider

class Repo:
    def factory_repo_provider(self):
        if self.config.get_repo_provider() == "github":
            return GithubRepoProvider()

    def __init__(self):
        self.config = Config()
        self.repo_provider = self.factory_repo_provider()

    def request(self, endpoint: str, params=None, method='GET', data=None):
        return self.repo_provider.request(endpoint, params, method, data)

    def update_pull_request(self, pull_request_number, title = None, description = None, state = None, target_branch = None):
        self.repo_provider.update_pull_request(pull_request_number, title, description, state, target_branch)

    def update_issue(self, issue_number, title = None, body = None, assignees = [], labels = [], state = None):
        self.repo_provider.update_issue(issue_number, title, body, assignees, labels, state)

    def create_issue(self, title, body = "", assignees = [], labels = []):
        self.repo_provider.create_issue(title, body, assignees, labels)

    def create_pull_request(self, source_branch, target_branch, title, body = "", draft=False):
        self.repo_provider.create_pull_request(source_branch, target_branch, title, body, draft)

    def comment_on_pull_request(self, pull_request_number, body = ""):
        self.repo_provider.comment_on_pull_request(pull_request_number, body)

    def update_pull_request_comment(self, comment_id, body):
        self.repo_provider.update_pull_request_comment(comment_id, body)

    def delete_pull_request_comment(self, comment_id):
        self.repo_provider.delete_pull_request_comment(comment_id)

    def comment_on_pull_request_file(self, commit_id, file_path, pull_request_number, body = "", line=None, delete_existing = True):
        self.repo_provider.comment_on_pull_request_file(commit_id, file_path, pull_request_number, body, line, delete_existing)

    def update_issue_comment(self, comment_id, body):
        self.repo_provider.update_issue_comment(comment_id, body)

    def delete_issue_comment(self, comment_id):
        self.repo_provider.delete_issue_comment(comment_id)

    def comment_on_issue(self, issue_number, body = ""):
        self.repo_provider.comment_on_issue(issue_number, body)

    def reply_to_pull_request_comment(self, reply_to_id, pull_request_number, body = ""):
        self.repo_provider.reply_to_pull_request_comment(reply_to_id, pull_request_number, body)

    def review_pull_request(self, pull_request_number, body = "", commit_sha = None, comments = [], event = "COMMENT"):
        self.repo_provider.review_pull_request(pull_request_number, body, commit_sha, comments, event)