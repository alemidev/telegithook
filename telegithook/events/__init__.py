from .code import Commit, Fork, Starred, Unstarred
from .issues import IssueOpened, IssueComment, IssueLabeled, IssueAssigned, IssueEditedTitle, IssueEditedBody, IssueDeleted, IssuePinned, IssueTransferred, IssueUnpinned, IssueClosed, IssueReopened, IssueUnassigned, IssueLocked, IssueUnlocked, IssueTransferred, IssueMilestoned, IssueDemilestoned
from .collaborator import colabAdded, colabRemoved
from .milestone import milestoneCreated, milestoneDeleted, milestoneOpened, milestoneEdited, milestoneClosed
from ..env import EXCLUDE_EVENTS

_events = [ Commit, Fork, IssueOpened, IssueComment, IssueLabeled, IssueAssigned, IssueEditedTitle, IssueEditedBody, IssueDeleted, IssuePinned, IssueUnpinned, IssueUnpinned, IssueClosed, IssueReopened, IssueUnassigned, IssueLocked, IssueUnlocked, IssueTransferred, IssueMilestoned, IssueDemilestoned, colabAdded, colabRemoved, Starred, Unstarred, milestoneCreated, milestoneDeleted, milestoneOpened, milestoneEdited, milestoneClosed ]
events = []

for event in _events:
    if type(event).__name__.lower() not in EXCLUDE_EVENTS:
        events.append(event)

EVENTS = events