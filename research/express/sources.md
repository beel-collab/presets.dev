# Express sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/express reports `latest` 5.3.0.
- https://expressjs.com/en/guide/migrating-5/ says middleware and handlers that return rejected promises are forwarded to the error handler. The same guide says a wildcard `*` must have a name: use `/*splat` instead of `/*`.
- https://expressjs.com/en/guide/error-handling/ is the error-middleware guide. Do not call `next(err)` after the response has been sent.
