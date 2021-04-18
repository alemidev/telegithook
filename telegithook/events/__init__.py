from .code import Commit, Fork
from .issues import IssueOpened, IssueComment, IssueLabeled, IssueAssigned

EVENTS = [ Commit, Fork, IssueOpened, IssueComment, IssueLabeled, IssueAssigned ]
