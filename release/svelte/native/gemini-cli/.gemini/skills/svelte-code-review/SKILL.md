---
name: "svelte-code-review"
description: "Review a Svelte or SvelteKit change for runes, load and action boundaries, and Kit 2 versus Kit 3 config. Use for a Svelte code review. Do not use for a Svelte 4 pattern pasted into a runes component, or a non-Svelte repository."
---

# Svelte Code Review Skill for Gemini CLI

Gemini CLI skill `svelte-code-review` for Svelte. Activation calls `activate_skill` and waits for consent. Keep this copy under `.gemini/skills`.

## When to run

Run this review for a Svelte component, a SvelteKit load or action, or a config change.

## When to leave it

Stop for a non-Svelte repository. Do not upgrade Svelte or Kit unless the user asked.

## Steps

1. Read the Svelte and Kit majors. Svelte 4 syntax in a rune component, or a Kit 2 config key on Kit 3, is a high finding.
2. Search for module-level mutable state in server code. User data stored there is a high finding.
3. Check `+page.ts` and `.svelte` files for a server-only import. That is a high finding.
4. Check `{@html}`, form actions that trust a hidden user id, and `$effect` loops.
5. Look for a hydration hazard: `window` or `Math.random` during init.
6. Run the project's test command only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the boundary that broke, and a fix. Include both majors.

## Stop

Stop when the user asks you to convert the whole app to runes or to Kit 3 in one review.
