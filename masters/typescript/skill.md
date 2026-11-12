## When to run

Run this review on a TypeScript change, a pull request, or a request to "check the types". Look for holes in the checker and for runtime data that was never parsed.

## When to leave it

Stop for a repository without TypeScript, or for a formatting-only diff. Do not upgrade the compiler unless the user asked.

## Steps

1. Read the installed `typescript` version and whether `strict` is on. A script that imports compiler APIs from the 7.0 `typescript` package is a high finding: 7.0 does not ship that API. Point it at `@typescript/typescript6`, or wait for a real 7.1 API. A plan to jump majors without a request is a finding, not a task you start.
2. Search the diff for `any`, `as `, `!`, and `@ts-ignore` or `@ts-expect-error` without a reason. Each one at a boundary is a finding. An assertion immediately after a proper parse can stay.
3. Find functions that accept `unknown` or external JSON and return a typed value without a parser. That is a finding.
4. Check unions. A `switch` that falls through to a default which returns `any` is a finding. An exhaustive switch can stay.
5. If the diff touches a script that imports `typescript` as a library, confirm the calls exist on the installed major. Missing methods are a high finding.
6. Run the project's typecheck when the user asked for a check. Record the command. Otherwise write `not run`.

## Output

Findings first, with file, line, the unsafe construct, and a narrower type or a parser. Then the compiler version and `no file edits` unless a fix was requested.

## Stop

Stop when the project is not TypeScript, or when the user asks you to disable `strict` to get a green build.
