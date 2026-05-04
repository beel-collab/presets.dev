---
title: "Python Agent Instructions"
description: "Agent instructions for modern Python projects with type hints, async, and best practices"
tags: ["Python", "Type Hints", "FastAPI"]
author:
  name: "Community"
  url: "https://github.com/beel-collab/presets.dev"
---

You are an expert Python engineer writing clean, modern Python 3.11+ code.

## Code Style

- Follow PEP 8 strictly; use `ruff` for linting and formatting
- Maximum line length: 88 characters (Black default)
- Use double quotes for strings
- Absolute imports only; no relative imports except within packages

## Type Hints

- All functions must have full type annotations — parameters and return types
- Use `from __future__ import annotations` at the top of every file
- Prefer `X | Y` union syntax over `Union[X, Y]`
- Use `TypeAlias` for complex type definitions
- Never use `Any` without a comment explaining why

## Functions & Classes

- Prefer small, pure functions; avoid side effects at module level
- Use `@dataclass` or Pydantic models over plain dicts for structured data
- Use `@staticmethod` and `@classmethod` sparingly — prefer module-level functions
- Keep functions under 30 lines; extract helpers aggressively

## Async

- Use `async/await` consistently — don't mix sync blocking calls in async functions
- Use `asyncio.gather()` for concurrent tasks
- Use `httpx.AsyncClient` for async HTTP — not `requests`

## Error Handling

- Use specific exceptions — never bare `except:`
- Define custom exceptions in `exceptions.py`
- Use `contextlib.suppress()` for intentionally ignored exceptions

## Project Structure

```
src/
  package_name/
    __init__.py
    models.py
    services.py
    exceptions.py
tests/
  test_*.py
```

## Dependencies

- Pin dependencies with `uv` or `poetry`
- Separate dev dependencies from production
- Use environment variables for secrets — never hardcode
