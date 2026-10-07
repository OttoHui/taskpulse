"""Task ranking and schedule generation."""

from __future__ import annotations

from datetime import date, datetime, timedelta

from .models import Task


def _score(task: Task, today: date) -> tuple[int, int, int]:
    """Return a sortable score; larger values represent more urgency."""
    due_score = 0 if task.due is None else max(0, 30 - (task.due - today).days)
    return (int(task.priority) * 100 + due_score, -task.minutes, -len(task.title))


def prioritize(tasks: list[Task], *, today: date | None = None) -> list[Task]:
    """Return tasks from most to least urgent without mutating the input."""
    reference = today or datetime.now().astimezone().date()
    return sorted(tasks, key=lambda task: _score(task, reference), reverse=True)


def schedule(
    tasks: list[Task],
    *,
    daily_minutes: int,
    start: date | None = None,
) -> dict[date, list[Task]]:
    """Pack prioritized tasks into consecutive workdays.

    A task is never split. If one task exceeds ``daily_minutes``, it receives
    a day of its own so the function always makes progress.
    """
    if daily_minutes <= 0:
        raise ValueError("daily_minutes must be greater than zero")

    start_date = start or datetime.now().astimezone().date()
    result: dict[date, list[Task]] = {}
    remaining = daily_minutes
    day = start_date

    for task in prioritize(tasks, today=start_date):
        if result.get(day) and task.minutes > remaining:
            day += timedelta(days=1)
            remaining = daily_minutes
        result.setdefault(day, []).append(task)
        remaining -= task.minutes
        if remaining <= 0:
            day += timedelta(days=1)
            remaining = daily_minutes
    return result
