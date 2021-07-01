from ..strings import STR
from .base import EventBase

class branchCreated(EventBase):
    KEY = 'created'
    labeled_str = STR["branch"]["created"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["before"] == "0000000000000000000000000000000000000000" and event["created"]

    def parse(self) -> str:
        return self.header("Branch created") + self.labeled_str.format(
                branch_title=self.event["ref"].split("/")[-1]
            )

class branchDeleted(EventBase):
    KEY = 'deleted'
    labeled_str = STR["branch"]["deleted"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["after"] == "0000000000000000000000000000000000000000" and event["deleted"]

    def parse(self) -> str:
        return self.header("Branch deleted") + self.labeled_str.format(
                branch_title=self.event["ref"].split("/")[-1]
            )