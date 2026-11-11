## When to run

Run this review for a Vue 3 change: a component, a composable, a store binding, or "check this reactivity".

## When to leave it

Stop for a non-Vue repository, or a request to convert Vue 2 that the user did not make. Do not upgrade Vue as part of the review.

## Steps

1. Read the installed Vue major. A Vue 2 file edited with Vue 3-only syntax is a high finding unless the task is the migration.
2. Search the diff for a destructure of `reactive()` or of a store without `storeToRefs` or `toRefs`. That is a finding when the fields are used later as if they were reactive.
3. Search for `window`, `document`, and `localStorage` in setup on a component that also renders on the server. That is a high finding.
4. Check watchers for cleanup, props for mutation, and `v-html` for unsanitized input.
5. Look for a test that renders the component and updates the source of truth. Missing coverage on a new composable is a medium finding. Run the project's Vue test command only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the reactivity or SSR mistake, and a fix. Include the Vue version.

## Stop

Stop when the user asks you to rewrite the app from Options API to script setup without naming the files.
