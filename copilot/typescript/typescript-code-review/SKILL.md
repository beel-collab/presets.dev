---
id: "copilot-typescript-code-review"
slug: "copilot/typescript/typescript-code-review/SKILL"
title: "TypeScript Code Review Skill for Copilot"
description: "Review a TypeScript change for unsafe assertions, missing runtime checks, and compiler-API assumptions. Use for a TypeScript code review. Do not use for a non-TypeScript repository or to turn on a new compiler unasked."
type: "skill"
tools:
  - "copilot"
stack: "typescript"
tags:
  - "typescript"
  - "strict"
  - "validation"
  - "code-review"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Copilot docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "typescript@7.0.2"
updated_for: "TypeScript 7.0.2, Nov 2026"
---

# TypeScript Code Review Skill for Copilot

## Install

Install the native export at `.github/skills/typescript-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# TypeScript Code Review Skill for Copilot

Copilot skill `typescript-code-review` for TypeScript. The description decides when Copilot loads it. Keep this copy under `.github/skills`.

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
