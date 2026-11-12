---
description: "Python standards for Environments, Types and pytest. Use when editing this stack. uv 0.13.7 and Ruff 0.17.4, Nov 2026."
trigger: "model_decision"
---

# Python Windsurf Rules: Environments, Types and pytest

Devin rule for Python. Install the `.devin/rules` file. The trigger is model decision. Do not also copy it into `.windsurf/rules`.

## Updated for uv 0.13.7 and Ruff 0.17.4, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

## Project shape

Read `pyproject.toml` and the lockfile first. The package layout is either a `src/` tree or a flat package. Follow the one that exists. Tests live where the project already puts them, usually `tests/`.

Entry points, scripts, and the test command come from the project config. Run them with `uv run` when uv owns the project. Do not invent a virtualenv beside an existing `.venv`.

## Types and boundaries

Type public functions and the data that crosses a process or a network. Prefer a typed model the project already uses, such as a dataclass or a Pydantic model, over a bare `dict`. `Any` is a hole. Use it only at a boundary you cannot name yet, and keep it off the return type.

Check optional values before you attribute them. A `# type: ignore` needs the error code and a reason. Do not blanket-ignore a file.

## Errors and I/O

Raise a specific exception the caller can catch. Do not `except Exception` and then `pass`. Add context with `raise ... from exc` when you translate an error.

Async functions do not call `time.sleep`, `requests`, or other blocking I/O. Use the async client the project already has. A sync library stays in a thread only when the project already does that and the call is bounded.

Close files and HTTP responses. A `with` block is the default.

## Security

Do not build SQL, shell commands, or HTML by concatenating user input. Use parameters and the project's escape path. Do not log secrets, tokens, or full request bodies. Read credentials from the environment the project already documents, not from a new committed file.

## Performance

Stream large files instead of `read()` into a string. Paginate a query that can grow. Do not hide an N+1 query inside a property that runs on every item. Cache a pure function only when a profile says it matters, and do not cache a value that includes a user id under a global key.

## Tests

pytest is the default when the repo already uses it. A test names the behavior: `test_rejects_empty_name`. Arrange the inputs, act once, assert the outcome. Use the existing fixtures. Do not mock the function you are testing.

Cover the failure path you touched: a bad input, a missing record, a dependency that raises. Run the test command the repo documents: `uv run pytest` only when uv owns the project, otherwise Poetry, Hatch, tox, or the venv the README names. Run Ruff when the project configures it. Paste the output. Do not claim a run you did not do.

## Mistakes to avoid

- A new package API you did not read in the installed version.
- A second environment created because the first command failed.
- Blocking I/O inside `async def`.
- A test that asserts a mock was called and never checks the result.
- An interpreter upgrade bundled into an unrelated fix.

## What changed in this major

No new language syntax is required here. uv 0.13 and Ruff 0.17 are the tools to use when the repo already uses them.

## Deprecated APIs to never generate

The `distutils` package was removed in Python 3.12. Use `setuptools`, or the standard-library module that replaced the function you needed.

## Commands

Run the documented test command and Ruff when configured.

## Example

```python
def parse_port(raw: str) -> int:
    port = int(raw)
    if not 1 <= port <= 65535:
        raise ValueError("port out of range")
    return port
```
