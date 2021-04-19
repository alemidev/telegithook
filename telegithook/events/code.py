from ..strings import STR
from ..util.safeGetter import get_username
from .base import EventBase

class Commit(EventBase):
    KEY = 'commits'
    row_str = STR["code"]["commits"]

    def parse(self) -> str:
        to_return = self.header("new commits")
        for commit in self.event[self.KEY]:
            to_return += self.row_str.format(
                author=get_username(commit['author']),
                message=commit['message'].replace("<", "&lt;").replace(">", "&gt;"),
                url=commit['url'],
                branch=self.event["ref"].split("/")[-1],
                hash=commit['id'][:7],
            )
        return to_return


class Fork(EventBase):
    KEY = 'forkee'
    string = STR["code"]["forkee"]

    def parse(self) -> str:
        return self.header("new fork") + self.string.format(
            forker=self.event['sender']['login'],
            repo=self.event['repository']['full_name'],
            forks=self.event['repository']['forks']
        )
