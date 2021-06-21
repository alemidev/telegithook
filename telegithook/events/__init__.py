from .code import Commit, Fork
from .issues import IssueOpened, IssueComment, IssueLabeled, IssueAssigned, IssueEditedTitle, IssueEditedBody, IssueDeleted, IssuePinned, IssueTransferred, IssueUnpinned, IssueClosed, IssueReopened, IssueUnassigned, IssueLocked, IssueUnlocked, IssueTransferred
from ..env import EXCLUDE_EVENTS

_events = [ Commit, Fork, IssueOpened, IssueComment, IssueLabeled, IssueAssigned, IssueEditedTitle, IssueEditedBody, IssueDeleted, IssuePinned, IssueUnpinned, IssueUnpinned, IssueClosed, IssueReopened, IssueUnassigned, IssueLocked, IssueUnlocked, IssueTransferred ]
events = []

for event in _events:
    if type(event).__name__.lower() not in EXCLUDE_EVENTS:
        events.append(event)

EVENTS = events