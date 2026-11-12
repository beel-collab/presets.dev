---
name: "python-test-writer"
description: "Add or extend pytest coverage for a Python change, using the project's uv environment and Ruff. Use when the user asks for Python tests or a failing case. Do not use for a non-Python repository or to upgrade the interpreter unasked."
paths:
  - "**/*.py"
  - "pyproject.toml"
---

# Python Test Writer Skill for Cursor

Cursor skill `python-test-writer` for Python. Run it with `/python-test-writer`, or let Agent select it when the request matches. `paths` only limits automatic surfacing.

## When to run

Run this when the user asks for tests, a regression case, or coverage for a Python change. Write pytest tests against the behavior, using the project's uv environment.

## When to leave it

Stop for a non-Python repository, or when the user asked for production code and said not to add tests. Do not upgrade Python or add a new test framework.

## Steps

1. Read `pyproject.toml`, the lockfile, and an existing test so the style matches. Note the interpreter constraint. Do not change it.
2. Name the behavior that is missing. One test, one behavior. Include the failure case: empty input, a missing row, or a dependency error.
3. Reuse fixtures. Build only the data the assertion needs. Call the real function. Assert the return value, the raised error, or the persisted row.
4. If the bug is not reproduced by the new test, stop and say so. Do not weaken the assertion to go green.
5. Run the test command the repository documents. If it uses uv, that is `uv run pytest`. If it uses Poetry, Hatch, tox, or a venv, use that command. Do not force uv onto a project that does not use it. Run Ruff only when the project configures it. Record the outputs. If a command cannot run, write `not run` and the reason.

## Output

```
## Files written
- tests/test_notes.py

## Covered
- `parse_port("0")` and `parse_port("99999")` raise `ValueError`.

## How to run
The command the repo documents. `uv run pytest tests/test_notes.py` only when uv owns the project. Poetry, Hatch, tox, or a venv otherwise.

## Result
pass, fail, or not run, with the output. A failing test stays failing unless the user also asked for the fix.

## Gaps
- Cases this file does not lock, and any command that could not run.
```

Example: `notes.py` adds `parse_port` and nothing asserts the out-of-range ports. Add those two cases and run the repo command. Do not mark them passed without a run.

## Stop

Stop when there is no Python project, when adding a test would require a new framework, or when the user asks you to mark tests passed without running them.
