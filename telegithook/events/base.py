from ..strings import STR

class EventBase(object):
    KEY = 'None'
    header = STR["header"]

    def __init__(self, event: dict):
        self.event = event

    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event

    def header(self, action : str = "new event") -> str:
        return self.header.format(
            repo=self.event['repository']['full_name'],
            branch=self.event['repository']['master_branch'],
            action=action,
        )

    def parse(self) -> str:
        return str(self.event[self.KEY])

