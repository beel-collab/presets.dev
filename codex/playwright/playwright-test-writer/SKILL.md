---
id: "codex-playwright-test-writer"
slug: "codex/playwright/playwright-test-writer/SKILL"
title: "Playwright Test Writer Skill for Codex"
description: "Write a Playwright regression test that reproduces a bug with locators and web-first assertions. Use when the user asks for a Playwright test or an end-to-end case. Do not use for unit tests in another runner or a non-browser bug."
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

Install the native export at `.agents/skills/playwright-test-writer/SKILL.md` (one file shared with Antigravity CLI).
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# Playwright Test Writer

Shared skill `playwright-test-writer` for Playwright. Codex and Antigravity CLI both read `.agents/skills/playwright-test-writer/SKILL.md`. Install this one file. Codex calls it with `$playwright-test-writer` or `/skills`. Cursor, GitHub Copilot, and Devin also read `.agents/skills`. A second copy with the same name collides. Do not install another tool's file there.

## When to run

Run this when the user wants a Playwright test, a regression for a UI bug, or an end-to-end case. The result is a spec that fails before the fix and passes after it.

## When to leave it

Do not upgrade dependencies or the framework version unless the user asked.

Stop for a unit-test request in pytest, Jest, or another runner, or when the repository has no Playwright config and the user did not ask to add Playwright.

## Steps

1. Read `playwright.config` and one existing spec. Match fixtures, the base URL, and the import style. Read the installed version before using a 1.65-only reporter or lock.
2. Write the failure down in one sentence: who does what, and what they should see.
3. Drive the UI with role or test-id locators. Assert the outcome with a web-first assertion. Do not add a timeout sleep.
4. Keep the test isolated. Use the existing auth fixture. Create only the data this case needs.
5. Run the single spec. If it cannot fail on the bug, the test is wrong. Record the command and the result. If the browser cannot start, write `not run` and the error. Do not claim a pass.

## Output

```
## Files written
- tests/login.spec.ts

## Covered
- A signed-in user clicks Save and sees the note.

## How to run
npx playwright test tests/login.spec.ts

## Result
pass, fail, or not run, with the command output. No production URL and no password.

## Gaps
- Browsers or projects this run did not execute.
```

Example: the bug is a Save button that never appears. Write the spec with `getByRole` and `toBeVisible()`, not `waitForTimeout`. Run that one file. If the browser cannot start, the result is `not run` and the gap says so.

## Stop

Stop when the user asks you to hit production, to commit a live session, or to add `waitForTimeout` so the suite looks green.
