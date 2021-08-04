from typing import Optional

from ..strings import STR
from ..util.safeGetter import get_username

class EventBase(object):
    KEY : Optional[str] = None

    def __init__(self, event: dict, key = None):
        if key is not None and self.KEY is None:
            self.KEY = key
        self.event = event

    def header(self, title : str = "") -> str:
        return STR["header"].format(
            repo=self.event['repository']['full_name'], # TODO repository is not guaranteed! maybe organization
            action=title or self.KEY,
        )

    def sender(self) -> str:
        return get_username(self.event["sender"])

    def body(self, **kwargs) -> str:
        if self.KEY in STR and self.event['action'] in STR[self.KEY]:
            return STR[self.KEY][self.event['action']].format(**kwargs)
        return STR["generic"].format(
            key = self.KEY.capitalize().replace("_", " "),
            sender = self.sender(),
            action = self.event["action"],
        )

    def parse(self) -> str:
        return self.header() + self.body()

# class CheckRun(EventBase):
#     KEY = "check_run"
 
# class CheckSuite(EventBase):
#     KEY = "check_suite"
 
# class CodeScanningAlert(EventBase):
#     KEY = "alert"

# class CommitComment(EventBase):
#     KEY = "comment"

# class ContentReference(EventBase):
#     KEY = "content_reference"

# class Create(EventBase):
#     KEY = "ref"

# class Delete(EventBase):
#     KEY = "ref"

# class DeployKey(EventBase):
#     KEY = "key"

# class Deployment(EventBase):
#     KEY = "deployment"

# class DeploymentStatus(EventBase):
#     KEY = "deployment_status"

# class Discussion(EventBase):
#     KEY = "discussion"

# class DiscussionComment(EventBase):
#     KEY = "comment"

# class Fork(EventBase):
#     KEY = "forkee"

# class GithubAppAuthorization(EventBase):
#     KEY = 

# class WikiPages(EventBase): # This is called "gollum" for some reason?
#     KEY = "pages"

# class Installation(EventBase):
#     KEY = "installation"