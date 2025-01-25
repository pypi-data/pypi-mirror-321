from enum import Enum


class ActivityProgress(str, Enum):
    INITIALIZED = "Initialized"
    STARTED = "Started"
    IN_PROGRESS = "InProgress"
    SUBMITTED = "Submitted"
    COMPLETED = "Completed"


class GradingProgress(str, Enum):
    FULLY_GRADED = "FullyGraded"
    PENDING = "Pending"
    PENDING_MANUAL = "PendingManual"
    FAILED = "Failed"
    NOT_READY = "NotReady"
