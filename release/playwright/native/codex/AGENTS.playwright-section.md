<!-- Append this section to AGENTS.md. Do not replace the existing file. This is project guidance, not a custom agent. -->

# Playwright Codex Instructions: Locators, Fixtures and Assertions

Section to append to `AGENTS.md` for Playwright. This is project guidance, not a custom agent.

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
