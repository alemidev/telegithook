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
                author=event["issue"]["user"]["login"],
                url=event["issue"]["html_url"],
                number=event["issue"]["number"],
            ) + body_str.format(
                title=event["issue"]["title"],
                text=event["issue"]["body"]
                        if len(event["issue"]["body"]) < 100 else
                     event["issue"]["body"][:100] + "...",
            )
