"""Public data models for TaskPulse."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import IntEnum


class Priority(IntEnum):
    """User-facing priority levels."""

    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass(frozen=True, slots=True)
class Task:
    """A task that can be ranked and scheduled.

    Args:
        title: Short, human-readable task name.
        minutes: Expected focused work time; must be positive.
        priority: Importance from 1 (low) to 3 (high).
        due: Optional due date. Earlier dates receive more urgency.
    """

    title: str
    minutes: int
    priority: Priority = Priority.MEDIUM
    due: date | None = None

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("title must not be empty")
        if self.minutes <= 0:
            raise ValueError("minutes must be greater than zero")
        if not isinstance(self.priority, Priority):
            raise TypeError("priority must be a Priority value")

