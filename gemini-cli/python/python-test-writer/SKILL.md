---
id: "gemini-cli-python-test-writer"
slug: "gemini-cli/python/python-test-writer/SKILL"
title: "Python Test Writer Skill for Gemini CLI"
description: "Gemini CLI skill for a Python test writer. Use when you want that test writer on a Python change. Do not use it for a different stack."
type: "skill"
tools:
  - "gemini-cli"
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
  - "Gemini CLI docs 2026-11-11; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "uv@0.13.7"
  - "ruff@0.17.4"
updated_for: "uv 0.13.7 and Ruff 0.17.4, Nov 2026"
---

# Python Test Writer Skill for Gemini CLI

## Install

Install the native export at `.gemini/skills/python-test-writer/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Python Test Writer Skill for Gemini CLI

Gemini CLI skill `python-test-writer` for Python. Activation calls `activate_skill` and waits for consent. Keep this copy under `.gemini/skills`.

## When to run

Run this when the user asks for tests, a regression case, or coverage for a Python change. Write pytest tests against the behavior, using the project's uv environment.

## When to leave it

Stop for a non-Python repository, or when the user asked for production code and said not to add tests. Do not upgrade Python or add a new test framework.

## Steps

1. Read `pyproject.toml`, the lockfile, and an existing test so the style matches. Note the interpreter constraint. Do not change it.
2. Name the behavior that is missing. One test, one behavior. Include the failure case: empty input, a missing row, or a dependency error.
3. Reuse fixtures. Build only the data the assertion needs. Call the real function. Assert the return value, the raised error, or the persisted row.
4. If the bug is not reproduced by the new test, stop and say so. Do not weaken the assertion to go green.
5. Run the narrowest pytest command through `uv run`, then Ruff if the project configures it. Record both outputs. If a command cannot run, write `not run` and the reason.

## Output

List the test files, the behavior each one locks, the commands, and the results. A failing test stays failing until the code is fixed, and only when the user asked for the fix too.

## Stop

Stop when there is no Python project, when adding a test would require a new framework, or when the user asks you to mark tests passed without running them.
