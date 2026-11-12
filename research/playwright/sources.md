# Playwright sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/playwright reports `latest` 1.65.0. `next` is a 1.66 alpha and is not the target.
- https://playwright.dev/docs/release-notes Version 1.65 adds the Bun runner (`bunx --bun playwright test`), the `failures` reporter, and the built-in `-exclusive-` test lock. Use those only when 1.65 is installed.
- https://playwright.dev/docs/locators is the locator guide. Prefer `getByRole` over `page.$` and `waitForTimeout`.
- https://playwright.dev/docs/getting-started-mcp is the Playwright MCP server (`@playwright/mcp`).
- https://playwright.dev/docs/api/class-page lists `page.$` and `page.$$` under Deprecated and says to use `page.locator()`.
