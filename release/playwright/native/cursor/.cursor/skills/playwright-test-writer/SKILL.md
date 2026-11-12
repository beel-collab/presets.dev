---
name: "playwright-test-writer"
description: "Write a Playwright regression test that reproduces a bug with locators and web-first assertions. Use when the user asks for a Playwright test or an end-to-end case. Do not use for unit tests in another runner or a non-browser bug."
paths:
  - "**/*.spec.ts"
  - "**/*playwright*"
---

# Playwright Test Writer Skill for Cursor

Cursor skill `playwright-test-writer` for Playwright. Run it with `/playwright-test-writer`, or let Agent select it when the request matches. `paths` only limits automatic surfacing.

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

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.

## Output

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
