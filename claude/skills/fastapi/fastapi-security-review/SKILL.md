---
id: "claude-fastapi-security-review"
slug: "claude/skills/fastapi/fastapi-security-review/SKILL"
title: "FastAPI Security Review Skill for Claude Code"
description: "Claude Code skill for a FastAPI security review. Use when you want that security review on a FastAPI change. Do not use it for a different stack."
type: "skill"
tools:
  - "claude"
stack: "fastapi"
tags:
  - "fastapi"
  - "python"
  - "pydantic"
  - "security"
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
  - "fastapi@0.162.4"
updated_for: "FastAPI 0.162.4, Nov 2026"
---

# FastAPI Security Review Skill for Claude Code

## Install

Install the native export at `.claude/skills/fastapi-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# FastAPI Security Review Skill for Claude Code

Claude Code skill `fastapi-security-review` for FastAPI. The command is `/fastapi-security-review`. Leave the normal permission prompts on.

## When to run

Run this review for a FastAPI route, a Pydantic model, or a request to "check the API auth".

## When to leave it

Stop for a Python script that is not a FastAPI app. Do not upgrade FastAPI or Pydantic unless the user asked.

## Steps

1. Read the FastAPI and Pydantic majors. v1 syntax in a v2 app is a high finding.
2. For each changed route, confirm a response model. A secret or password field on that model is a high finding. A `model_dump()` spread into a write is a high finding.
3. For each write, confirm an auth dependency and an owner check. A client-supplied user id that is stored is a high finding.
4. For each `async def`, confirm it does not call a blocking client. That is a high finding on a request path.
5. Look for CORS `*` with credentials. That is a high finding.
6. Note whether tests cover 401, 403, and an invalid body. Run pytest only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the route, and a fix. Do not include secrets from `.env`.

## Stop

Stop when the user asks you to disable auth on a route to make a test pass, or to point the suite at production.
