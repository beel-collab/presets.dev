---
id: "cline-express-security-review"
slug: "cline/express/express-security-review/SKILL"
title: "Express Security Review Skill for Cline"
description: "Review an Express app for middleware order, Express 5 route syntax, validation, and auth. Use for an Express security review. Do not use for a Fastify or NestJS app, or to forward errors twice."
type: "skill"
tools:
  - "cline"
stack: "express"
tags:
  - "express"
  - "nodejs"
  - "middleware"
  - "security"
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
  - "express@5.3.0"
updated_for: "Express 5.3.0, Nov 2026"
---

# Express Security Review Skill for Cline

## Install

Install the native export at `.cline/skills/express-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Express Security Review Skill for Cline

Cline skill `express-security-review` for Express. `/express-security-review` forces it. A global skill of the same name overrides this project file.

## When to run

Run this review for an Express router, middleware order, or an Express 4 to 5 migration.

## When to leave it

Stop for Fastify, Nest, or another framework. Do not upgrade Express unless the user asked.

## Steps

1. Read the installed Express major. On 5, an old `/*` wildcard or a regex route copied from 4 is a high finding. On 4, do not introduce 5-only syntax.
2. Walk middleware order. Auth after the route, or a body parser after the handler, is a high finding.
3. For each write, confirm a schema and an auth check. A missing one is a high finding.
4. Search for `next(err)` on a path that also sends a response. Double-send is a high finding.
5. Confirm `express.json` has a limit.
6. Run the test script only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the route, and a fix. Include the Express major.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: an Express 5 router still has `app.get('/*', handler)`.
Output: high | src/app.ts:22 | Express 5 rejects an unnamed `*` wildcard | use `/*splat`.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## What to check

- Injection: concatenated SQL, shell, or HTML.
- XSS: unescaped user text in HTML.
- CSRF: a browser state change with the framework check disabled.
- Secrets: a key in the repo or in a log line.
- IDOR: an id from the client with no owner or permission check.
- SSRF: a user-supplied URL fetched with no allow-list.

## Stop

Stop when the user asks you to remove auth middleware to debug a route.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
