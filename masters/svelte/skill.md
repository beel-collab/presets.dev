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
Input: a SvelteKit 3 load function imports `page` from `$app/stores`.
Output: high | src/routes/notes/+page.ts:1 | `$app/stores` is removed in Kit 3 | import from `$app/state`.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to convert the whole app to runes or to Kit 3 in one review.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
