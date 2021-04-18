class EventBase(object):
    KEY = 'None'

    def __init__(self, event: dict):
        self.event = event

    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event

    def parse(self) -> str:
        return str(self.event[self.KEY])
