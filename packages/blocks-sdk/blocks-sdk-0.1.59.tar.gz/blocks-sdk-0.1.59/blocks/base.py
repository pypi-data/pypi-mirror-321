class BaseRepoProvider:
    def request(self, endpoint: str, params=None, method='GET', data=None):
        raise NotImplementedError
    
    def update_pull_request(self, pull_request_number = None, title = None, description = None, state = None, target_branch = None):
        raise NotImplementedError

    def update_issue(self, issue_number = None, title = None, body = None, assignees = None, labels = None, state = None):
        raise NotImplementedError

    def create_issue(self, title = None, body = None, assignees = None, labels = None):
        raise NotImplementedError

    def create_pull_request(self, source_branch = None, target_branch = None, title = None, body = None, draft = False):
        raise NotImplementedError

    def comment_on_pull_request(self, pull_request_number = None, body = None):
        raise NotImplementedError

    def update_pull_request_comment(self, comment_id = None, body = None):
        raise NotImplementedError

    def delete_pull_request_comment(self, comment_id = None):
        raise NotImplementedError

    def comment_on_pull_request_file(self, commit_id = None, file_path = None, pull_request_number = None, body = None, line = None, delete_existing = True):
        raise NotImplementedError

    def update_issue_comment(self, comment_id = None, body = None):
        raise NotImplementedError

    def delete_issue_comment(self, comment_id = None):
        raise NotImplementedError

    def comment_on_issue(self, issue_number = None, body = None):
        raise NotImplementedError

    def reply_to_pull_request_comment(self, reply_to_id = None, pull_request_number = None, body = None):
        raise NotImplementedError

    def review_pull_request(self, pull_request_number = None, body = None, commit_sha = None, comments = None):
        raise NotImplementedError
