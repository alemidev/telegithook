from .strings.strings import get_string

class EventBase(object):
    KEY = "None"

    def __init__(self, event: dict):
        self.event = event

    @staticmethod
    def isPresent(event: dict) -> bool:
        return self.KEY in event

    def parse(self) -> str:
        return str(self.event[self.KEY])

class Commit(EventBase):
    KEY = "commits"

    def parse(event: dict) -> str:
        out = ""
        out += get_string("commitHead").format(
            repo=event['repository']['full_name'],
            branch=event['repository']['master_branch'],
        )
        for commit in event[self.KEY]:
            out += get_string("commitRow").format(
                author=commit['author']['username'], # TODO safe getter for this
                message=commit['message'],
                url=commit['url'],
                hash=commit['id'][:7],
            )
        return out

EVENTS = [ Commit ]
