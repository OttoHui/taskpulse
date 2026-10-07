# TaskPulse

A local-first Python package for turning a task list into a realistic daily plan.

## Team

**Group 24 (6/6 members)**

- Tsz Hei CHUI
- Fong Kwan HUI
- David KWONG
- Sik Man LAM
- Hong Shing WONG
- Chun Hin YIU

## Project links

- GitHub: https://github.com/OttoHui/taskpulse
- PyPI: https://pypi.org/project/taskpulse-group24/
- Demo video / slides: [Add link]

## Motivation

Students and small project teams frequently have too many tasks and not enough
clarity about what to do first. Existing productivity tools often hide the
reasoning behind their recommendations or require accounts and cloud services.

TaskPulse focuses on a simple question: given a list of tasks, which ones should
be tackled first and how should they fit into the next few days? The answer is
made transparent by combining explicit priority, due-date urgency, and realistic
work capacity.

## Innovation

TaskPulse offers a small, inspectable alternative to heavy scheduling tools:

- explicit task priorities (`LOW`, `MEDIUM`, `HIGH`);
- due-date urgency that rises as deadlines approach;
- daily capacity-aware planning without splitting tasks into fragments;
- a simple Python API and CLI that are easy to test and extend.

This makes the package useful for study planning, assignment tracking, and team
workload triage without requiring database storage or a hosted service.

## How it works

The package uses a straightforward scoring strategy:

1. Higher priority values rank above lower ones.
2. Tasks with earlier due dates become more urgent.
3. Daily planning packs tasks into workdays while preserving the original task
   boundaries.
4. The user can inspect and modify the underlying logic in a single small code
   base.

## Demo

Install and run:

```bash
pip install taskpulse-group24
# or from the repo:
python -m pip install -e .
```

Create a CSV file such as:

```csv
title,minutes,priority,due
Write project abstract,45,3,2026-10-10
Review references,30,2,
```

Then run:

```bash
taskpulse tasks.csv --daily-minutes 60
```

Expected output:

```text
2026-10-07
  - Write project abstract (45 min, priority HIGH)
2026-10-08
  - Review references (30 min, priority MEDIUM)
```

## Why this is valuable

- Easy to understand: the logic is human-readable and testable.
- Easy to extend: scoring rules, weekend logic, and export formats can be added
  without rewriting the package.
- Professional fit: the package is installable, documented, and ready to publish
  to PyPI.

## Project status

- Core package implemented
- CLI and Python API available
- Tests included
- Documentation prepared
- Release workflow ready for GitHub + PyPI

## Q&A prompts

- Why not use a database? The package is intentionally local-first and simple,
  which keeps it easy to reason about and deploy.
- Can tasks be split? Not in the initial version. The package preserves task
  integrity while using daily capacity windows.
- How can this grow? We can add weekend skipping, JSON import/export, and calendar
  export in a future release.

## Final checklist before submission

- [ ] Add real GitHub repository link
- [ ] Add real PyPI link
- [x] Update team member names
- [ ] Add demo video or slide deck link
- [ ] Finalize the README and package metadata
- [ ] Practice the 1-minute demo
