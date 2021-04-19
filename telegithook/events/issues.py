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

