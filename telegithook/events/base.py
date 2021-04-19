from ..strings import STR


class EventBase(object):
    KEY = 'None'
    head = STR['header']

    def __init__(self, event: dict):
        self.event = event

    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event

    def header(self, action: str = 'new event') -> str:
        return self.head.format(
            repo=self.event['repository']['full_name'],
            action=action,
        )

    def parse(self) -> str:
        return str(self.event[self.KEY])
