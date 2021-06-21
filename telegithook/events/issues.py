from ..strings import STR
from .base import EventBase

class IssueOpened(EventBase):
    KEY = 'issue'
    open_str = STR["issues"]["opened"]
    body_str = STR["issues"]["body"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "opened"

    def parse(self) -> str:
        return self.header("issue opened") + self.open_str.format(
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
                title=self.event["issue"]["title"].replace("<", "&lt;").replace(">", "&gt;"),
            ) + self.body_str.format(
                author=self.event["issue"]["user"]["login"],
                text=self.event["issue"]["body"].replace("<", "&lt;").replace(">", "&gt;"),
            )

class IssueComment(EventBase):
    KEY = 'issue'
    comment_str = STR["issues"]["comment"]
    body_str = STR["issues"]["body"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and "comment" in event and event["action"] == "created"

    def parse(self) -> str:
        return self.header("issue comment") + self.comment_str.format(
                url=self.event["comment"]["html_url"],
                number=self.event["issue"]["number"],
                title=self.event["issue"]["title"].replace("<", "&lt;").replace(">", "&gt;"),
            ) + self.body_str.format(
                author=self.event["comment"]["user"]["login"],
                text=self.event["comment"]["body"].replace("<", "&lt;").replace(">", "&gt;"),
            )

class IssueLabeled(EventBase):
    KEY = 'issue'
    labeled_str = STR["issues"]["label"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "labeled"

    def parse(self) -> str:
        return self.header("issue label") + self.labeled_str.format(
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
                label=self.event["label"]["name"],
            )

class IssueAssigned(EventBase):
    KEY = 'issue'
    assignee_str = STR["issues"]["assignee"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "assigned"

    def parse(self) -> str:
        return self.header("issue assignee") + self.assignee_str.format(
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
                assignee=self.event["assignee"]["login"],
            )

class IssueEditedTitle(EventBase):
    KEY = 'issue'
    edited_str = STR["issues"]["edited_t"]

    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "edited" and "title" in event["changes"]

    def parse(self) -> str:
        return self.header("issue title edited") + self.edited_str.format(
                changes_title=self.event["changes"]["title"]["from"],
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
            )
class IssueEditedBody(EventBase):
    KEY = 'issue'
    edited_str = STR["issues"]["edited_b"]

    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "edited" and "body" in event["changes"]

    def parse(self) -> str:
        return self.header("issue body edited") + self.edited_str.format(
                issue_url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
                comment_url=self.event["comment"]["html_url"],
                comment_id=self.event["comment"]["id"],
                changes_body=self.event["changes"]["body"]["from"],
            )

class IssueDeleted(EventBase):
    KEY = 'issue'
    edited_str = STR["issues"]["deleted"]

    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "deleted"
    def parse(self) -> str:
        return self.header("issue deleted") + self.edited_str.format(
                title=self.event["issue"]["title"],
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
            )

class IssuePinned(EventBase):
    KEY = 'issue'
    edited_str = STR["issues"]["pinned"]

    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "pinned"

    def parse(self) -> str:
        return self.header("issue pinned") + self.edited_str.format(
                title=self.event["issue"]["title"],
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
        )

class IssueUnpinned(EventBase):
    KEY = 'issue'
    edited_str = STR["issues"]["unpinned"]

    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "unpinned"

    def parse(self) -> str:
        return self.header("issue unpinned") + self.edited_str.format(
                title=self.event["issue"]["title"],
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
            )

class IssueClosed(EventBase):
    KEY = 'issue'
    edited_str = STR["issues"]["closed"]

    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "closed"

    def parse(self) -> str:
        return self.header("issue closed") + self.edited_str.format(
                title=self.event["issue"]["title"],
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
            )

class IssueReopened(EventBase):
    KEY = 'issue'
    edited_str = STR["issues"]["reopened"]

    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "reopened"

    def parse(self) -> str:
        return self.header("issue reopened") + self.edited_str.format(
                title=self.event["issue"]["title"],
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
            )

class IssueUnassigned(EventBase):
    KEY = 'issue'
    assignee_str = STR["issues"]["unassigned"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "unassigned"

    def parse(self) -> str:
        return self.header("issue unassigned") + self.assignee_str.format(
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
                assignee=self.event["assignee"]["login"],
            )

class IssueLocked(EventBase):
    KEY = 'issue'
    assignee_str = STR["issues"]["locked"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "locked"

    def parse(self) -> str:
        return self.header("issue locked") + self.assignee_str.format(
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
                reason=self.event["issue"]["active_lock_reason"],
            )

class IssueUnlocked(EventBase):
    KEY = 'issue'
    assignee_str = STR["issues"]["unlocked"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "unlocked"

    def parse(self) -> str:
        return self.header("issue unlocked") + self.assignee_str.format(
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
            )

class IssueTransferred(EventBase):
    KEY = 'issue'
    assignee_str = STR["issues"]["transferred"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "transferred"

    def parse(self) -> str:
        return self.header("issue transferred") + self.assignee_str.format(
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
                target_link=self.event["changes"]["new_repository"]["html_url"],
                target=self.event["changes"]["new_repository"]["full_name"]
            )