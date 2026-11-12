---
id: "codex-fastapi-rules"
slug: "codex/fastapi/fastapi-rules"
title: "FastAPI Codex Instructions: Pydantic Models, Dependencies and Async"
description: "Codex instructions for FastAPI: Pydantic Models, Dependencies and Async. Append to AGENTS.md. Structure, security, and tests. FastAPI 0.162.5, Nov 2026."
type: "rule"
tools:
  - "codex"
stack: "fastapi"
tags:
  - "fastapi"
  - "python"
  - "pydantic"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Codex docs 2026-11-11; CLI not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "fastapi@0.162.5"
updated_for: "FastAPI 0.162.5, Nov 2026"
---

# FastAPI Codex Instructions: Pydantic Models, Dependencies and Async

## Install

Install the native export at `AGENTS.md` as an appended section, not a replacement and not a custom agent.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# FastAPI Codex Instructions: Pydantic Models, Dependencies and Async

Section to append to `AGENTS.md` for FastAPI. This is project guidance, not a custom agent.

## Updated for FastAPI 0.162.5, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

## Project shape

Routers are split by resource. A route function is thin: it takes dependencies, calls a function that does the work, and returns a response model. Settings, the lifespan, and the database session live where the app already creates them. Do not build a new global client at import time.

## Models

Every request body and every response has a Pydantic model. The response model is a subset. A field the client must not see, such as a password hash or an internal flag, is not on the response model. Do not `response_model_exclude` as the only protection if you can omit the field.

Validate constraints on the model: length, bounds, and enums. Do not re-check them with a pile of `if` statements that drift from the schema. Extra fields are ignored or rejected the way the project already configured. Do not pass `dict(body)` into an ORM create. Copy the fields you intend to write.

## Dependencies and auth

Auth is a dependency that returns the current user or raises. A route that writes declares that dependency. Do not trust a user id in the path or body. Load the row and check the owner.

Database sessions are yielded from a dependency and closed in `finally`. A long-lived session stored on `app.state` without a scope is a bug. Lifespan replaces the old startup event in new code. Do not add `@app.on_event("startup")` beside a lifespan.

## Async

An `async def` route does not call a blocking database driver, `time.sleep`, or `requests`. Use the async driver, or move the blocking call the way the project already does. Do not define a route as `def` and `async def` inconsistently for the same style of I/O.

## Errors, security, and tests

Raise `HTTPException` with a status and a short detail. A 500 path logs the exception and returns a generic message. Do not include a SQL string or a secret in `detail`.

CORS allows the origins the project listed. Do not set `*` with credentials. Rate limits and body size follow the app's existing middleware.

Test with the project's `TestClient` or async client. Cover a missing token, a forbidden owner, a body that fails validation, and a response that does not contain the hidden field. Run pytest. Record the output.

## Mistakes to avoid

- Pydantic v1 decorators in a v2 app.
- A response model that includes a secret column.
- `body.model_dump()` spread into a database write.
- Blocking I/O in an `async def` route.
- A route with no auth dependency that still changes data.

## What changed in this major

FastAPI 0.162 requires Pydantic v2 and AnyIO >= 4.1. `orm_mode` and v1 `@validator` are deprecated, not removed: use `from_attributes` and `@field_validator`.

## Deprecated APIs to never generate

`@validator` is deprecated. Use `@field_validator`. `orm_mode = True` is deprecated. Use `model_config = ConfigDict(from_attributes=True)`.

## Commands

Run `pytest` for the changed routes.

## Example

```python
from pydantic import BaseModel, ConfigDict, Field

class NoteIn(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    body: str = Field(min_length=1, max_length=2000)
```
