from . import strings


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
    action = strings.action(KEY)

    def parse(self) -> str:
        out = ""
        out += self.action.head().format(
            repo=self.event['repository']['full_name'],
            branch=self.event['repository']['master_branch'],
        )
        for commit in self.event[self.KEY]:
            out += self.action.row().format(
                # TODO safe getter for this
                author=commit['author']['username'],
                message=commit['message'],
                url=commit['url'],
                hash=commit['id'][:7],
            )
        return out


EVENTS = [Commit]
