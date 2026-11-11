---
id: "cline-typescript-code-review"
slug: "cline/typescript/typescript-code-review/SKILL"
title: "TypeScript Code Review Skill for Cline"
description: "Cline skill for a TypeScript code review. Use when you want that code review on a TypeScript change. Do not use it for a different stack."
type: "skill"
tools:
  - "cline"
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
  - "Cline docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "typescript@7.0.2"
updated_for: "TypeScript 7.0.2, Nov 2026"
---

# TypeScript Code Review Skill for Cline

## Install

Install the native export at `.cline/skills/typescript-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# TypeScript Code Review Skill for Cline

Cline skill `typescript-code-review` for TypeScript. `/typescript-code-review` forces it. A global skill of the same name overrides this project file.

## When to run

Run this review on a TypeScript change, a pull request, or a request to "check the types". Look for holes in the checker and for runtime data that was never parsed.

## When to leave it

Stop for a repository without TypeScript, or for a formatting-only diff. Do not upgrade the compiler unless the user asked.

## Steps

1. Read the installed `typescript` version and whether `strict` is on. A 7.0 compiler API assumption in a 5.x or 6.x repo is a high finding. A plan to jump majors without a request is a finding, not a task you start.
2. Search the diff for `any`, `as `, `!`, and `@ts-ignore` or `@ts-expect-error` without a reason. Each one at a boundary is a finding. An assertion immediately after a proper parse can stay.
3. Find functions that accept `unknown` or external JSON and return a typed value without a parser. That is a finding.
4. Check unions. A `switch` that falls through to a default which returns `any` is a finding. An exhaustive switch can stay.
5. If the diff touches a script that imports `typescript` as a library, confirm the calls exist on the installed major. Missing methods are a high finding.
6. Run the project's typecheck when the user asked for a check. Record the command. Otherwise write `not run`.

## Output

Findings first, with file, line, the unsafe construct, and a narrower type or a parser. Then the compiler version and `no file edits` unless a fix was requested.

## Stop

Stop when the project is not TypeScript, or when the user asks you to disable `strict` to get a green build.
