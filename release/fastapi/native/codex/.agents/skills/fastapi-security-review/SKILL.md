---
name: "fastapi-security-review"
description: "Review a FastAPI change for Pydantic validation, auth dependencies, and blocking work in async routes. Use for a FastAPI security review. Do not use for a non-FastAPI Python script or to expose a hidden field in a response model."
---

# FastAPI Security Review Skill for Codex

Codex skill `fastapi-security-review` for FastAPI. Call it with `$fastapi-security-review` or `/skills`. Do not install the other tools' copies beside it.

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
Input: `routes/notes.py` is `async def` and calls `time.sleep(2)` before returning.
Output: high | routes/notes.py:11 | a blocking call on the event loop | move the work to a thread or an async client.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## What to check

- Injection: a SQL string built with an f-string from a query param.
- XSS: an `HTMLResponse` that interpolates user text.
- CSRF: cookie-authenticated browser writes with no CSRF token. Bearer tokens are not that finding.
- Secrets: a password field on the response model, or a key in the repo.
- IDOR: a path user id stored with no owner check.
- SSRF: an outbound `httpx` call to a user-supplied URL with no allow-list.

## Stop

Stop when the user asks you to disable auth on a route to make a test pass, or to point the suite at production.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
