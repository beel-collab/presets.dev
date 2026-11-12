---
id: "codex-python-test-writer"
slug: "codex/python/python-test-writer/SKILL"
title: "Python Test Writer Skill for Codex"
description: "Add or extend pytest coverage for a Python change, using the project's uv environment and Ruff. Use when the user asks for Python tests or a failing case. Do not use for a non-Python repository or to upgrade the interpreter unasked."
type: "skill"
tools:
  - "codex"
stack: "python"
tags:
  - "python"
  - "uv"
  - "ruff"
  - "pytest"
  - "testing"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Codex docs 2026-11-11; CLI not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "uv@0.13.7"
  - "ruff@0.17.4"
updated_for: "uv 0.13.7 and Ruff 0.17.4, Nov 2026"
---

# Python Test Writer Skill for Codex

## Install

Install the native export at `.agents/skills/python-test-writer/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Python Test Writer Skill for Codex

Codex skill `python-test-writer` for Python. Call it with `$python-test-writer` or `/skills`. Do not install the other tools' copies beside it.

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

List the test files, the behavior each one locks, the commands, and the results. A failing test stays failing until the code is fixed, and only when the user asked for the fix too.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: a one-line change that matches a rule in the standards.
Output: either one finding with file and line, or "No findings" when the change is the valid pattern named in the standards.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when there is no Python project, when adding a test would require a new framework, or when the user asks you to mark tests passed without running them.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
