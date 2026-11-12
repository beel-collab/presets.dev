<!-- Append this section to AGENTS.md. Do not replace the existing file. This is project guidance, not a custom agent. -->

# Node.js Codex Instructions: ESM, Cancellation and Streams

Section to append to `AGENTS.md` for Node.js. This is project guidance, not a custom agent.

## Updated for Node.js 26.13.1 LTS, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

Node.js 26.13.1 Lithium is the active LTS on nodejs.org. The newest dist tag is a v27 alpha. Do not target the alpha. Read `engines` and `.nvmrc` and stay on the line the project already runs. Do not bump Node because a newer LTS exists unless the task asks.

## Project shape

Match the module system. A project with `"type": "module"` is ESM. Do not add a `require` in an ESM file or an `import` in a CommonJS file without the interop the project already uses. File extensions in ESM imports follow the local style.

Scripts, the test command, and the start command come from `package.json`. The lockfile is committed. Do not mix npm, pnpm, and yarn in one change.

## Requests and cancellation

Every outbound call takes a timeout and an `AbortSignal`. When the request that triggered the work is aborted, abort the downstream calls. Do not retry without a cap, a delay, and a check that the signal is still active. A retry of a non-idempotent POST needs an explicit reason.

Handle `unhandledRejection` by failing the process or by catching at the boundary. An empty `catch` hides a broken request.

## Streams and the event loop

A stream has a consumer that respects backpressure. Do not `read()` an unbounded upload into a single buffer. Pipe errors are handled on both sides.

Do not run CPU-heavy work, `readFileSync` on a large file, or a tight JSON parse of a huge payload on the request path. Move it off the request or bound the size. `fs` sync methods do not belong in a server handler.

## Errors and security

Validate body size, content type, and schema before you use the payload. Return a status and a small error body. Do not put a stack trace in the response.

Secrets come from the environment. Do not log `Authorization` headers or cookies. A child process does not interpolate user input into a shell string.

## Performance

Keep dependencies that run at startup small. A connection pool has a max and an idle timeout. Cache a computed value only when it is safe to share across requests. Do not cache a response that includes a user's data under a process-global key.

## Tests

Use the runner the project already has. Cover a timeout, an aborted request, and a payload that is too large. Run the test command and record the output. Do not claim a run you did not do.

## Mistakes to avoid

- ESM and CommonJS mixed in a new file.
- A retry loop with no cancellation and no cap.
- A swallowed rejection.
- A synchronous filesystem or CPU call inside a request handler.
- Targeting the v27 alpha, or upgrading the LTS line unasked.

## What changed in this major

Stay on the 26.13 LTS line. Do not target the v27 alpha. `AbortSignal` and timeouts are the cancellation tools.

## Deprecated APIs to never generate

`url.parse` is deprecated. Use the WHATWG `URL` class. An unbounded retry is a missing cancellation, not a removed API.

## Commands

Run the package test script. Do not target the v27 alpha.

## Example

```ts
const res = await fetch(url, { signal: AbortSignal.timeout(5_000) })
```
