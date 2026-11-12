---
name: "express-security-review"
description: "Review an Express app for middleware order, Express 5 route syntax, validation, and auth. Use for an Express security review. Do not use for a Fastify or NestJS app, or to forward errors twice."
---

# Express Security Review Skill for Windsurf

Devin skill `express-security-review` for Express. Invoke it with `/express-security-review`. Install only `.devin/skills`. This file is not a subagent.

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

- Injection: SQL or a shell command built by concatenating `req.body` or `req.query`.
- XSS: `res.send` of user HTML with no escape.
- CSRF: a cookie-session write with no CSRF check and a reflected `Origin`.
- Secrets: `process.env` values written to the response or the log.
- IDOR: `req.params.id` loaded with no owner check after auth.
- SSRF: `fetch(req.body.url)` with no host allow-list.

## Stop

Stop when the user asks you to remove auth middleware to debug a route.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
