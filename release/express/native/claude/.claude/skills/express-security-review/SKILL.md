---
name: "express-security-review"
description: "Review an Express app for middleware order, Express 5 route syntax, validation, and auth. Use for an Express security review. Do not use for a Fastify or NestJS app, or to forward errors twice."
---

# Express Security Review Skill for Claude Code

Claude Code skill `express-security-review` for Express. The command is `/express-security-review`. Leave the normal permission prompts on.

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

## Stop

Stop when the user asks you to remove auth middleware to debug a route.
