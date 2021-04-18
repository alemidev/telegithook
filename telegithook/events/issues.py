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
        return self.header("issue opened") + open_str.format(
                url=self.event["issue"]["html_url"],
                number=self.event["issue"]["number"],
                title=self.event["issue"]["title"],
            ) + body_str.format(
                author=self.event["issue"]["user"]["login"],
                text=self.event["issue"]["body"]
                        if len(self.event["issue"]["body"]) < 100 else
                     self.event["issue"]["body"][:100] + "...",
            )

class IssueComment(EventBase):
    KEY = 'comment'
    comment_str = STR["issues"]["comment"]
    body_str = STR["issues"]["body"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return 'issue' in event and cls.KEY in event and event["action"] == "created"

    def parse(self) -> str:
        return self.header("issue comment") + self.comment_str.format(
                url=self.event["comment"]["html_url"],
                number=self.event["comment"]["number"],
                title=self.event["comment"]["title"],
            ) + body_str.format(
                author=self.event["comment"]["user"]["login"],
                text=self.event["comment"]["body"]
                        if len(self.event["comment"]["body"]) < 100 else
                     self.event["comment"]["body"][:100] + "...",
            )
