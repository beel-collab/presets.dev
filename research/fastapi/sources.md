# FastAPI sources

Fetched 12 November 2026.

- Registry: https://pypi.org/pypi/fastapi/json reports 0.162.5.
- https://fastapi.tiangolo.com/release-notes/ lists 0.162.5 on 11 November 2026 and 0.162.4 on 10 November 2026. Both are patch notes. The presets follow 0.162.5.
- https://raw.githubusercontent.com/fastapi/fastapi/master/pyproject.toml requires `pydantic>=2.9.0` and `anyio>=4.1.0`. The project classifiers say Pydantic 2.
- https://pydantic.dev/docs/validation/latest/get-started/migration/ is the Pydantic v1 to v2 migration. `orm_mode` and v1 `@validator` are not the v2 API.
