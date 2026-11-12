---
name: "svelte-code-review"
description: "Review a Svelte or SvelteKit change for runes, load and action boundaries, and Kit 2 versus Kit 3 config. Use for a Svelte code review. Do not use for a Svelte 4 pattern pasted into a runes component, or a non-Svelte repository."
paths:
  - "**/*.svelte"
  - "**/*.svelte.ts"
  - "src/routes/**/*.ts"
  - "src/lib/**/*.ts"
  - "src/hooks*.ts"
  - "vite.config.ts"
  - "vite.config.js"
---

# Svelte Code Review Skill for Cursor

Cursor skill `svelte-code-review` for Svelte. Run it with `/svelte-code-review`, or let Agent select it when the request matches. `paths` only limits automatic surfacing.

## When to run

Run this review for a Svelte component, a SvelteKit load or action, or a config change.

## When to leave it

Stop for a non-Svelte repository. Do not upgrade Svelte or Kit unless the user asked.

## Steps

1. Read the Svelte and Kit majors. On Kit 3, a new `svelte.config.js`, an import from `$app/stores`, or a `$lib` import is a high finding. On Kit 2 those are still valid. Do not flag them there. Svelte 4 syntax in a rune component is a high finding.
2. Search for module-level mutable state in server code. User data stored there is a high finding.
3. Check `+page.ts` and `.svelte` files for a server-only import. That is a high finding.
4. Check `{@html}`, form actions that trust a hidden user id, and `$effect` loops.
5. Look for a hydration hazard: `window` or `Math.random` during init.
6. Run the project's test command only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the boundary that broke, and a fix. Include both majors.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: `src/routes/notes/+page.ts` imports `page` from `$app/state` and reads `page.params.id`.
Output: high | src/routes/notes/+page.ts:1 | a load function cannot read `page` | export `load({ params })` and use `params.id`. In a `.svelte` component, `$app/state` and `$derived` are the right read.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to convert the whole app to runes or to Kit 3 in one review.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
