from .code import Commit, Fork
from .issues import IssueOpened, IssueComment, IssueLabeled, IssueAssigned
from ..env import EXCLUDE_EVENTS

_events = [ Commit, Fork, IssueOpened, IssueComment, IssueLabeled, IssueAssigned ]
events = []

for event in _events:
    if type(event).__name__.lower() not in EXCLUDE_EVENTS:
        events.append(event)

EVENTS = events