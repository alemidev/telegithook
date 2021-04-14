from . import strings


class EventBase(object):
    KEY = 'None'

    def __init__(self, event: dict):
        self.event = event

    @property
    def string(self):
        return strings.action(self.KEY)

    @classmethod
    def isPresent(cls, event: dict) -> bool:
        return cls.KEY in event

    def parse(self) -> str:
        return str(self.event[self.KEY])


class Commit(EventBase):
    KEY = 'commits'

    def parse(self) -> str:
        to_return = self.string.head().format(
            repo=self.event['repository']['full_name'],
            branch=self.event['repository']['master_branch'],
        )
        for commit in self.event[self.KEY]:
            to_return += self.string.row().format(
                # TODO safe getter for this
                author=commit['author']['username'],
                message=commit['message'],
                url=commit['url'],
                hash=commit['id'][:7],
            )
        return to_return


class Fork(EventBase):
    KEY = 'forkee'

    def parse(self) -> str:
        return self.string().format(
            forker=self.event['sender']['login'],
            repo=self.event['repository']['full_name'],
            forks=self.event['repository']['forks']
        )


EVENTS = [Commit, Fork]
