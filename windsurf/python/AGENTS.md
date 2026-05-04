---
title: "Python Project"
description: "Place at project root. Always-on conventions for Python 3.11+ projects using uv, Ruff, and pytest."
tags: ["python"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

# Python Project Conventions

## Environment & Tooling
- Python 3.11+ required
- `uv` for dependency management and virtual environments
- `ruff` for linting and formatting (replaces black, isort, flake8)
- `mypy --strict` for type checking
- `pytest` for testing

## Code Style
- Type hints required on all function signatures — parameters and return types
- Line length: 88 characters (ruff default)
- Imports: stdlib → third-party → local, sorted automatically by ruff
- Google-style docstrings for public API only — not private methods

## Naming
- `snake_case` for functions, variables, modules
- `PascalCase` for classes
- `UPPER_SNAKE_CASE` for module-level constants
- No abbreviations in names (`user_id` not `uid`, `connection` not `conn`)

## Patterns to Follow
```python
# ✅ pathlib over os.path
config_path = Path(__file__).parent / "config.yaml"

# ✅ dataclass for structured data
@dataclass
class OrderItem:
    product_id: str
    quantity: int
    price: Decimal

# ✅ specific exceptions with context
try:
    result = process(data)
except ValueError as e:
    raise ProcessingError("Invalid input format") from e
```

## Project Structure
```
src/
  mypackage/
    __init__.py     # Explicit __all__ defining public API
    core.py
    models.py
tests/
  conftest.py
  test_core.py
pyproject.toml      # All tool config lives here
```

## What to Avoid
- Never use `except:` or `except Exception:` without re-raising or logging
- No mutable default arguments: `def f(items=None)` not `def f(items=[])`
- No `import *`
- No `print()` for logging — use the `logging` module or `structlog`
