class BaseRepoProvider:
    def request(self, endpoint: str, params=None, method='GET', data=None):
        raise NotImplementedError
    
    def update_pull_request(self, pull_request_number, title = None, description = None, state = None, target_branch = None):
        raise NotImplementedError

    def update_issue(self, issue_number, title = None, body = None, assignees = [], labels = [], state = None):
        raise NotImplementedError

    def create_issue(self, title, body = "", assignees = [], labels = []):
        raise NotImplementedError

    def create_pull_request(self, source_branch, target_branch, title, body = "", draft=False):
        raise NotImplementedError

    def comment_on_pull_request(self, pull_request_number, body = ""):
        raise NotImplementedError

    def update_pull_request_comment(self, comment_id, body):
        raise NotImplementedError

    def delete_pull_request_comment(self, comment_id):
        raise NotImplementedError

    def comment_on_pull_request_file(self, commit_id, file_path, pull_request_number, body = "", line=None, delete_existing = True):
        raise NotImplementedError

    def update_issue_comment(self, comment_id, body):
        raise NotImplementedError

    def delete_issue_comment(self, comment_id):
        raise NotImplementedError

    def comment_on_issue(self, issue_number, body = ""):
        raise NotImplementedError

    def reply_to_pull_request_comment(self, reply_to_id, pull_request_number, body = ""):
        raise NotImplementedError

    def review_pull_request(self, pull_request_number, body = "", commit_sha = None, comments = [], event = "COMMENT"):
        raise NotImplementedError
