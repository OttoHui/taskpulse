"""Command-line interface for quick planning from CSV input."""

from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path

from .models import Priority, Task
from .planner import schedule


def _read_tasks(path: Path) -> list[Task]:
    with path.open(newline="", encoding="utf-8") as source:
        rows = csv.DictReader(source)
        required = {"title", "minutes", "priority"}
        if not required.issubset(rows.fieldnames or set()):
            raise ValueError("CSV must contain title, minutes, and priority columns")
        tasks = []
        for row in rows:
            due = date.fromisoformat(row["due"]) if row.get("due") else None
            tasks.append(
                Task(
                    title=row["title"],
                    minutes=int(row["minutes"]),
                    priority=Priority(int(row["priority"])),
                    due=due,
                )
            )
    return tasks


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a focused task schedule.")
    parser.add_argument("csv_file", type=Path, help="CSV with title, minutes, priority, due")
    parser.add_argument("--daily-minutes", type=int, default=120)
    args = parser.parse_args()

    for day, tasks in schedule(
        _read_tasks(args.csv_file),
        daily_minutes=args.daily_minutes,
    ).items():
        print(day.isoformat())
        for task in tasks:
            print(f"  - {task.title} ({task.minutes} min, priority {task.priority.name})")


if __name__ == "__main__":
    main()

