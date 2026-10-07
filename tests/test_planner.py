from datetime import date

import pytest

from taskpulse import Priority, Task, prioritize, schedule


def test_prioritize_prefers_high_priority_and_earlier_due_date():
    today = date(2026, 10, 7)
    later = Task("Later", 30, Priority.HIGH, date(2026, 10, 20))
    sooner = Task("Sooner", 30, Priority.HIGH, date(2026, 10, 8))
    low = Task("Low", 10, Priority.LOW)

    assert prioritize([low, later, sooner], today=today) == [sooner, later, low]


def test_schedule_packs_tasks_without_splitting():
    start = date(2026, 10, 7)
    tasks = [Task("A", 60, Priority.HIGH), Task("B", 45, Priority.MEDIUM)]

    plan = schedule(tasks, daily_minutes=60, start=start)

    assert plan[start] == [tasks[0]]
    assert plan[date(2026, 10, 8)] == [tasks[1]]


def test_oversized_task_gets_a_day_of_its_own():
    start = date(2026, 10, 7)
    task = Task("Long task", 180)

    assert schedule([task], daily_minutes=120, start=start) == {start: [task]}


@pytest.mark.parametrize(
    "kwargs",
    [{"title": "", "minutes": 10}, {"title": "Task", "minutes": 0}],
)
def test_invalid_tasks_are_rejected(kwargs):
    with pytest.raises(ValueError):
        Task(**kwargs)


def test_invalid_daily_capacity_is_rejected():
    with pytest.raises(ValueError, match="daily_minutes"):
        schedule([], daily_minutes=0)

