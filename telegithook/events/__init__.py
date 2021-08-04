from .code import Commit, Fork, Starred, Unstarred
from .issues import IssueOpened, IssueComment, IssueLabeled, IssueAssigned, IssueEditedTitle, IssueEditedBody, IssueDeleted, IssuePinned, IssueTransferred, IssueUnpinned, IssueClosed, IssueReopened, IssueUnassigned, IssueLocked, IssueUnlocked, IssueTransferred, IssueMilestoned, IssueDemilestoned
from .collaborator import colabAdded, colabRemoved
from .milestone import milestoneCreated, milestoneDeleted, milestoneOpened, milestoneEdited, milestoneClosed
from .branch import branchCreated, branchDeleted
from .base import EventBase
from ..env import EXCLUDE_EVENTS

_events = [branchCreated, branchDeleted, Commit, Fork, IssueOpened, IssueComment, IssueLabeled, IssueAssigned, IssueEditedTitle, IssueEditedBody, IssueDeleted, IssuePinned, IssueUnpinned, IssueUnpinned, IssueClosed, IssueReopened, IssueUnassigned, IssueLocked, IssueUnlocked, IssueTransferred, IssueMilestoned, IssueDemilestoned, colabAdded, colabRemoved, Starred, Unstarred, milestoneCreated, milestoneDeleted, milestoneOpened, milestoneEdited, milestoneClosed]

class EventsContainer:
    def __init__(self) -> None:
        self.events = []
        for event in _events:
            if type(event).__name__.lower() not in EXCLUDE_EVENTS:
                self.events.append(event)

    def __getitem__(self, name:str) -> EventBase:
        for event in self.events:
            if event.KEY == name:
                return event
        return EventBase


EVENTS = EventsContainer()