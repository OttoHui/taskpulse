# TaskPulse

TaskPulse is a small, dependency-free Python package that turns a task list
into a focused daily plan. It is designed for students and small project teams
who want transparent prioritization without sending personal data to a service.

## Project team

**Group 24 (6/6 members)**

- Tsz Hei CHUI
- Fong Kwan HUI
- David KWONG
- Sik Man LAM
- Hong Shing WONG
- Chun Hin YIU

## Why it exists

Most task apps either require a hosted account or hide prioritization behind a
complex interface. TaskPulse keeps the algorithm inspectable:

1. importance is explicit (`LOW`, `MEDIUM`, or `HIGH`);
2. approaching due dates add urgency;
3. shorter tasks win ties, making plans easier to finish;
4. tasks are packed into days without splitting a task across sessions.

The result is useful for study plans, sprint preparation, and a one-minute
project demonstration.

## Install

```bash
pip install taskpulse-24
```

For local development:

```bash
git clone https://github.com/OttoHui/taskpulse.git
cd taskpulse
pip install -e ".[dev]"  # or: pip install -e .
pytest
```

## Python API

```python
from datetime import date
from taskpulse import Priority, Task, schedule

tasks = [
    Task("Write project abstract", 45, Priority.HIGH, date(2026, 10, 10)),
    Task("Review references", 30, Priority.MEDIUM),
]

plan = schedule(tasks, daily_minutes=60, start=date(2026, 10, 7))
for day, items in plan.items():
    print(day, [item.title for item in items])
```

## Command line

Create `tasks.csv`:

```csv
title,minutes,priority,due
Write project abstract,45,3,2026-10-10
Review references,30,2,
```

Then run:

```bash
taskpulse tasks.csv --daily-minutes 60
```

## Project and collaboration

Suggested team split for Group 24:

- **Tsz Hei CHUI:** project coordination, requirements, and final integration.
- **Fong Kwan HUI:** core models, prioritization, and scheduling logic.
- **David KWONG:** command-line interface and user experience.
- **Sik Man LAM:** tests, edge cases, and quality checks.
- **Hong Shing WONG:** documentation, examples, and PyPI metadata.
- **Chun Hin YIU:** demo, presentation wiki, and release verification.

Make small commits by feature and review each other's pull requests. The
published distribution is named `taskpulse-24`; its import name remains
`taskpulse`.

## One-minute demonstration

1. Show the two-row CSV (10 seconds).
2. Run `taskpulse tasks.csv --daily-minutes 60` (15 seconds).
3. Explain that priority and due date determine order, while capacity determines
   the day (20 seconds).
4. Show the equivalent Python API and mention that no external service or
   dependency is required (15 seconds).

## Roadmap

- optional weekend skipping;
- JSON input/output;
- calendar export;
- configurable scoring strategies.
