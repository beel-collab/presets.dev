## When to run

Run this audit when a Node.js service is slow, timing out, or leaking work after the client disconnects. Also run it for "check the event loop" or "this handler blocks".

## When to leave it

Stop for a browser-only React bug, or a repository that does not run on Node. Do not upgrade Node as part of the audit.

## Steps

1. Read `engines` and the start script. Note the LTS line. A recommendation to move to a v27 alpha is not a finding you file as work. Flag it only if the diff already targets that alpha.
2. Find the handler the user named. If they did not name one, ask. Search that path for `readFileSync`, `execSync`, large `JSON.parse`, and unbounded `Buffer.concat`.
3. Check outbound calls for a timeout and an `AbortSignal` tied to the request. A retry without a cap is a high finding on a hot path.
4. Check streams and body limits. An upload with no size cap is a high finding.
5. Look for a process-global cache keyed without the user or tenant when the value contains their data.
6. Run the project's benchmark or test only if one exists and the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the blocking or unbounded call, and a bounded alternative. Include the Node line you read.

## Stop

Stop when the user asks you to load-test production or to print environment secrets.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.

## Output

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
