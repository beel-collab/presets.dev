---
name: "nuxt-performance-audit"
description: "Audit a Nuxt app for duplicate SSR fetches, unstable payload keys, and private runtime config leaking to the client. Use for a Nuxt performance audit. Do not use for a non-Nuxt Vue app or to enable experimental routeTypedFetch unasked."
---

# Nuxt Performance Audit Skill for Codex

Codex skill `nuxt-performance-audit` for Nuxt. Call it with `$nuxt-performance-audit` or `/skills`. Do not install the other tools' copies beside it.

## When to run

Run this audit when a Nuxt page is slow, double-fetches, hydrates badly, or might be leaking config.

## When to leave it

Stop for a Vue app that is not Nuxt. Do not upgrade Nuxt or enable experimental flags unless the user asked.

## Steps

1. Read the installed Nuxt major. A Nuxt 3-only config key on Nuxt 4 is a finding.
2. Search setup blocks for bare `fetch` or `$fetch` used for data that `useAsyncData` should own. A duplicate server-then-client fetch is a high finding.
3. Check `useAsyncData` keys. A key that ignores a route param is a high finding.
4. Read `runtimeConfig`. A secret outside `public` that is referenced from a client component is a high finding. `routeTypedFetch` turned on without a request is a finding.
5. Look for `window` during setup.
6. Run the project's test or a single page load only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the extra fetch or the leaked key, and a fix. Do not print secret values.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: `nuxt.config.ts` sets `runtimeConfig.public.apiSecret`.
Output: high | nuxt.config.ts:6 | a secret under `public` is sent to the browser | keep `apiSecret` outside `public`.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to log `runtimeConfig` or to disable SSR to hide a hydration bug.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
