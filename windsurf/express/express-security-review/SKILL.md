---
id: "windsurf-express-security-review"
slug: "windsurf/express/express-security-review/SKILL"
title: "Express Security Review Skill for Windsurf"
description: "Windsurf skill for a Express security review. Use when you want that security review on a Express change. Do not use it for a different stack."
type: "skill"
tools:
  - "windsurf"
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
  - "Devin and Cascade docs 2026-11-11; not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "express@5.3.0"
updated_for: "Express 5.3.0, Nov 2026"
---

# Express Security Review Skill for Windsurf

## Install

Install the native export at `.devin/skills/express-security-review/SKILL.md` and `.windsurf/skills/express-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Express Security Review Skill for Windsurf

Skill `express-security-review` for Devin CLI and the legacy Windsurf skills folder. Invoke it with `/express-security-review`. This file is not a subagent.

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
