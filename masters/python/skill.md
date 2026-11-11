## When to run

Run this when the user asks for tests, a regression case, or coverage for a Python change. Write pytest tests against the behavior, using the project's uv environment.

## When to leave it

Stop for a non-Python repository, or when the user asked for production code and said not to add tests. Do not upgrade Python or add a new test framework.

## Steps

1. Read `pyproject.toml`, the lockfile, and an existing test so the style matches. Note the interpreter constraint. Do not change it.
2. Name the behavior that is missing. One test, one behavior. Include the failure case: empty input, a missing row, or a dependency error.
3. Reuse fixtures. Build only the data the assertion needs. Call the real function. Assert the return value, the raised error, or the persisted row.
4. If the bug is not reproduced by the new test, stop and say so. Do not weaken the assertion to go green.
5. Run the narrowest pytest command through `uv run`, then Ruff if the project configures it. Record both outputs. If a command cannot run, write `not run` and the reason.

## Output

List the test files, the behavior each one locks, the commands, and the results. A failing test stays failing until the code is fixed, and only when the user asked for the fix too.

## Stop

Stop when there is no Python project, when adding a test would require a new framework, or when the user asks you to mark tests passed without running them.
