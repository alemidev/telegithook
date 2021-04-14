from .strings.strings import STRINGS

class EventBase(object):
    KEY = "None"

    def __init__(self, event: dict):
        self.event = event

    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event

    def parse(self) -> str:
        return str(self.event[self.KEY])

class Commit(EventBase):
    KEY = "commits"

    def parse(self) -> str:
        out = ""
        out += STRINGS["actions"]["commit"]["head"].format(
            repo=self.event['repository']['full_name'],
            branch=self.event['repository']['master_branch'],
        )
        for commit in self.event[self.KEY]:
            out += STRINGS["actions"]["commit"]["row"].format(
                author=commit['author']['username'], # TODO safe getter for this
                message=commit['message'],
                url=commit['url'],
                hash=commit['id'][:7],
            )
        return out

EVENTS = [ Commit ]
