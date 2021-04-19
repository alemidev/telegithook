from .code import Commit
from .code import Fork
from .issues import IssueAssigned
from .issues import IssueComment
from .issues import IssueLabeled
from .issues import IssueOpened

EVENTS = [Commit, Fork, IssueOpened, IssueComment, IssueLabeled, IssueAssigned]
