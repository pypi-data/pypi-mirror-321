class BaseRepoProvider:
    def request(self, endpoint: str, params=None, method='GET', data=None):
        raise NotImplementedError
    
    def update_pull_request(self, pull_request_number = None, title = None, body = None, assignees = None, labels = None, state = None, maintainer_can_modify = None, target_branch = None):
        raise NotImplementedError

    def update_issue(self, issue_number = None, title = None, body = None, assignees = None, labels = None, state = None, state_reason = None, milestone = None):
        raise NotImplementedError

    def create_issue(self, title = None, body = None, assignees = None, labels = None, milestone = None):
        raise NotImplementedError

    def create_pull_request(self, source_branch = None, target_branch = None, title = None, body = None, draft = False, issue_number = None):
        raise NotImplementedError

    def comment_on_pull_request(self, pull_request_number = None, body = None):
        raise NotImplementedError

    def update_pull_request_comment(self, comment_id = None, body = None):
        raise NotImplementedError

    def delete_pull_request_comment(self, comment_id = None):
        raise NotImplementedError

    def comment_on_pull_request_file(self, commit_id = None, file_path = None, pull_request_number = None, body = None, line = None, delete_existing = True, position = None, side = None, start_line = None, start_side = None, reply_to_id = None, subject_type = None):
        raise NotImplementedError

    def update_issue_comment(self, comment_id = None, body = None):
        raise NotImplementedError

    def delete_issue_comment(self, comment_id = None):
        raise NotImplementedError

    def comment_on_issue(self, issue_number = None, body = None):
        raise NotImplementedError

    def reply_to_pull_request_comment(self, reply_to_id = None, pull_request_number = None, body = None):
        raise NotImplementedError

    def review_pull_request(self, pull_request_number = None, body = None, commit_id = None, comments = None):
        raise NotImplementedError
