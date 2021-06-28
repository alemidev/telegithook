from ..strings import STR
from .base import EventBase

class colabRemoved(EventBase):
    KEY = 'member'
    labeled_str = STR["collaborator"]["removed"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "removed"

    def parse(self) -> str:
        return self.header("collaborator removed") + self.labeled_str.format(
                profile_url=self.event["member"]["html_url"],
                member_name=self.event["member"]["login"],
                repo_name=self.event["repository"]["name"],
            )

class colabAdded(EventBase):
    KEY = 'member'
    labeled_str = STR["collaborator"]["added"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "added"

    def parse(self) -> str:
        return self.header("collaborator added") + self.labeled_str.format(
                profile_url=self.event["member"]["html_url"],
                member_name=self.event["member"]["login"],
                repo_name=self.event["repository"]["name"],
            )

# colabEditing remaining because that can be tested for organisations only