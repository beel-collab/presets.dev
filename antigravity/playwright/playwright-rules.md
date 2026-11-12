---
id: "antigravity-playwright-rules"
slug: "antigravity/playwright/playwright-rules"
title: "Playwright Antigravity CLI Rules: Locators, Fixtures and Assertions"
description: "Antigravity CLI rules for Playwright: Locators, Fixtures and Assertions. Append to GEMINI.md. Structure, security, and tests. Playwright 1.65.0, Nov 2026."
type: "rule"
tools:
  - "antigravity"
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
  - "Antigravity CLI docs 2026-11-12; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "playwright@1.65.0"
updated_for: "Playwright 1.65.0, Nov 2026"
---

# Playwright Antigravity CLI Rules: Locators, Fixtures and Assertions

## Install

Install the native export at `GEMINI.md` or `AGENTS.md` as an appended section.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# Playwright Antigravity CLI Rules: Locators, Fixtures and Assertions

Section to append to `GEMINI.md` for Playwright. Antigravity CLI loads every `GEMINI.md` and every `AGENTS.md` it finds. Do not put this same section in both files. Confirm with `/context`.

## Updated for Playwright 1.65.0, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

## Project shape

Tests live in the directory the config already scans. Name the file the way neighbors are named. Share auth or a seeded account through a fixture, not through a login copied into every test. A storage state file is generated. Do not commit a storage state that contains a real session.

One test owns one behavior. A serial chain is a last resort and must say why.

## Locators and assertions

Locate by role and accessible name first, then by test id when the role is not unique. Do not use a CSS path that walks three `div`s. Do not use an xpath you cannot read out loud.

Assert with a web-first assertion: `toBeVisible`, `toHaveText`, `toHaveURL`. Those wait. `expect(await locator.textContent()).toBe(...)` does not retry the locator. A fixed `waitForTimeout` is a bug, not a fix for a race.

## Isolation

Each test can run alone, in any order. Create the data it needs. Do not depend on a previous test's row. Do not share a mutable account across workers. The exclusive lock exists for the rare case that must be alone. Do not put it on every test.

A dialog, a download, and a popup are events you wait for before the click that opens them, using the project's pattern.

## Failures

On failure, the trace and the screenshot are the evidence. Turn them on in the config the project already has, usually retain-on-failure. Read the trace before you add a sleep. The failures reporter is useful when the installed version has it. Do not add a second reporter that hides the trace.

## Security and performance

Tests use a test account and a local or disposable base URL. Do not point the suite at production, and do not embed a password in the spec. Read credentials from the env the config already documents.

Do not `page.goto` a heavy flow in `beforeEach` if the test only needs one screen. Mock a third party at the network boundary the project already uses. Do not mock the application under test.

## A bug fix

Reproduce the bug with a test that fails for the right reason. Then change the product code. The test stays. If you cannot reproduce it, say what you tried. Do not write a test that passes against the broken behavior.

## Mistakes to avoid

- `waitForTimeout` or a brittle CSS chain.
- An assertion that never retries, so the test passes before the UI updates.
- Shared mutable auth or data across workers.
- A test that passes when the feature is broken because it only checks that a locator exists.
- An upgrade of Playwright bundled into a single new spec.
- `page.$` when a `getByRole` locator can see the control.

## What changed in this major

Playwright 1.65 adds the failures reporter, exclusive locks, and a Bun runner. Use them only when that version is installed.

## Deprecated APIs to never generate

`page.$` and `page.$$` are in Playwright's deprecated list. Use `page.locator()`.

## Commands

Run `npx playwright test` on the new spec.

## Example

```ts
await expect(page.getByRole("button", { name: "Save" })).toBeVisible()
```
## Agent tooling

Playwright publishes an MCP server (`@playwright/mcp`) and, for coding agents, a CLI plus skills that spend fewer tokens than the full accessibility tree. See https://playwright.dev/docs/getting-started-mcp .
