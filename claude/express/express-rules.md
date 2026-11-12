---
id: "claude-express-rules"
slug: "claude/express/express-rules"
title: "Express Claude Code Rules: Middleware, Routing and Validation"
description: "Claude Code rules for Express: Middleware, Routing and Validation. Structure, data, errors, security, performance, and tests. Express 5.3.0, Nov 2026."
type: "rule"
tools:
  - "claude"
stack: "express"
tags:
  - "express"
  - "nodejs"
  - "middleware"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Claude Code docs 2026-11-11; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "express@5.3.0"
updated_for: "Express 5.3.0, Nov 2026"
---

# Express Claude Code Rules: Middleware, Routing and Validation

## Install

Install the native export at `.claude/rules/express-rules.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# Express Claude Code Rules: Middleware, Routing and Validation

Path-scoped Claude Code rule for Express. It loads when a matching file is read. It does not replace `CLAUDE.md`.

## Updated for Express 5.3.0, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

## Project shape

Middleware is an ordered list. Security headers, body parsing, and auth run before the route that needs them. A router mounts on a path. Do not register a catch-all before a more specific route and then wonder why the specific route never runs.

An async handler either uses the project's wrapper or relies on Express 5's rejection forwarding. It does not do both. Do not `catch` a rejection, send a response, and also call `next(err)`.

## Validation and bodies

Validate params, query, and body with the project's schema. Reject unknown fields on a write. Cap the JSON body size in the parser. A route that reads `req.body` with no schema is a review.

## Auth and errors

A route that changes data has auth middleware. Do not check auth only in the UI. After auth, check that the resource belongs to the caller. A client-supplied user id is not identity.

The error middleware has four arguments and sits last. It logs the error and sends a status and a short body. It does not send a stack in production. Headers are not written twice.

## Security and tests

`helmet` or the project's header middleware stays enabled. CORS lists origins. Do not reflect any `Origin` with credentials. Rate-limit the login route the project already protects.

A test hits the route with supertest or the project's client. Cover no token, a bad body, and a body larger than the limit if you changed the limit. Run the test script. Record the output.

## Mistakes to avoid

- An Express 4 wildcard left in an Express 5 router.
- `next(err)` after the response was already sent.
- A write route with no auth and no schema.
- An unbounded `express.json()` body.
- A second error handler that runs after the first already sent the body.

## What changed in this major

Express 5 forwards rejected promises. Replace Express 4 `/*` wildcards. Do not call `next(err)` after `res.send`.

## Deprecated APIs to never generate

Express 5 uses path-to-regexp v8. `app.get('/*')` throws at startup because the `*` has no name. Write `app.get('/*splat', ...)`.

## Commands

Run the package test script.

## Example

```ts
app.use(express.json({ limit: "100kb" }))
```
