---
id: "codex-playwright-test-writer"
slug: "codex/playwright/playwright-test-writer/SKILL"
title: "Playwright Test Writer Skill for Codex"
description: "Codex skill for a Playwright test writer. Use when you want that test writer on a Playwright change. Do not use it for a different stack."
type: "skill"
tools:
  - "codex"
stack: "playwright"
tags:
  - "playwright"
  - "testing"
  - "e2e"
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
  - "playwright@1.65.0"
updated_for: "Playwright 1.65.0, Nov 2026"
---

# Playwright Test Writer Skill for Codex

## Install

Install the native export at `.agents/skills/playwright-test-writer/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Playwright Test Writer Skill for Codex

Codex skill `playwright-test-writer` for Playwright. Call it with `$playwright-test-writer` or `/skills`. Do not install the other tools' copies beside it.

## When to run

Run this when the user wants a Playwright test, a regression for a UI bug, or an end-to-end case. The result is a spec that fails before the fix and passes after it.

## When to leave it

Stop for a unit-test request in pytest, Jest, or another runner, or when the repository has no Playwright config and the user did not ask to add Playwright.

## Steps

1. Read `playwright.config` and one existing spec. Match fixtures, the base URL, and the import style. Read the installed version before using a 1.65-only reporter or lock.
2. Write the failure down in one sentence: who does what, and what they should see.
3. Drive the UI with role or test-id locators. Assert the outcome with a web-first assertion. Do not add a timeout sleep.
4. Keep the test isolated. Use the existing auth fixture. Create only the data this case needs.
5. Run the single spec. If it cannot fail on the bug, the test is wrong. Record the command and the result. If the browser cannot start, write `not run` and the error. Do not claim a pass.

## Output

The spec path, the behavior it locks, the command, and the output. No production URL and no password in the report.

## Stop

Stop when the user asks you to hit production, to commit a live session, or to add `waitForTimeout` so the suite looks green.
