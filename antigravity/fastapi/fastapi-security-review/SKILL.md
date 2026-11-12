---
id: "antigravity-fastapi-security-review"
slug: "antigravity/fastapi/fastapi-security-review/SKILL"
title: "FastAPI Security Review Skill for Antigravity CLI"
description: "Review a FastAPI change for Pydantic validation, auth dependencies, and blocking work in async routes. Use for a FastAPI security review. Do not use for a non-FastAPI Python script or to expose a hidden field in a response model."
type: "skill"
tools:
  - "antigravity"
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
  - "Antigravity CLI docs 2026-11-12; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "fastapi@0.162.5"
updated_for: "FastAPI 0.162.5, Nov 2026"
---

# FastAPI Security Review Skill for Antigravity CLI

## Install

Install the native export at `.agents/skills/fastapi-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# FastAPI Security Review Skill for Antigravity CLI

Antigravity CLI skill `fastapi-security-review` for FastAPI. The workspace path is `.agents/skills/fastapi-security-review/SKILL.md`. Reload skills before you expect the new command.

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

## What to check

- Injection: concatenated SQL, shell, or HTML.
- XSS: unescaped user text in HTML.
- CSRF: a browser state change with the framework check disabled.
- Secrets: a key in the repo or in a log line.
- IDOR: an id from the client with no owner or permission check.
- SSRF: a user-supplied URL fetched with no allow-list.

## Stop

Stop when the user asks you to disable auth on a route to make a test pass, or to point the suite at production.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
