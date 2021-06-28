from ..strings import STR
from .base import EventBase

class milestoneCreated(EventBase):
    KEY = 'milestone'
    labeled_str = STR["milestone"]["created"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "created"

    def parse(self) -> str:
        return self.header("milestone created") + self.labeled_str.format(
                milestone_url=self.event["milestone"]["html_url"],
                milestone_title=self.event["milestone"]["title"],
                milestone_due_on=self.event["milestone"]["due_on"],
                milestone_description=self.event["milestone"]["description"],
            )

class milestoneEdited(EventBase):
    KEY = 'milestone'
    labeled_str = STR["milestone"]["edited"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "edited"

    def parse(self) -> str:
        return self.header("milestone edited") + self.labeled_str.format(
                milestone_url=self.event["milestone"]["html_url"],
                milestone_title=self.event["milestone"]["title"],
                milestone_due_on=self.event["milestone"]["due_on"],
                milestone_description=self.event["milestone"]["description"],
            )

class milestoneClosed(EventBase):
    KEY = 'milestone'
    labeled_str = STR["milestone"]["closed"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "closed"

    def parse(self) -> str:
        return self.header("milestone closed") + self.labeled_str.format(
                milestone_url=self.event["milestone"]["html_url"],
                milestone_title=self.event["milestone"]["title"],
                milestone_due_on=self.event["milestone"]["due_on"],
                milestone_description=self.event["milestone"]["description"],
            )

class milestoneDeleted(EventBase):
    KEY = 'milestone'
    labeled_str = STR["milestone"]["deleted"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "deleted"

    def parse(self) -> str:
        return self.header("milestone deleted") + self.labeled_str.format(
                milestone_url=self.event["milestone"]["html_url"],
                milestone_title=self.event["milestone"]["title"],
                milestone_due_on=self.event["milestone"]["due_on"],
                milestone_description=self.event["milestone"]["description"],
            )

class milestoneOpened(EventBase):
    KEY = 'milestone'
    labeled_str = STR["milestone"]["opened"]
    
    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event and event["action"] == "opened"

    def parse(self) -> str:
        return self.header("milestone opened") + self.labeled_str.format(
                milestone_url=self.event["milestone"]["html_url"],
                milestone_title=self.event["milestone"]["title"],
                milestone_due_on=self.event["milestone"]["due_on"],
                milestone_description=self.event["milestone"]["description"],
            )