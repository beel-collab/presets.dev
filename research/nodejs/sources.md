# Node.js sources

Fetched 12 November 2026.

- Registry: https://nodejs.org/dist/index.json lists the newest LTS as v26.13.1 Lithium, dated 10 November 2026. The newest tag overall is v27.0.0-alpha.0.0.0, which is not a target.
- https://nodejs.org/api/url.html marks `url.parse` deprecated. Use the WHATWG `URL` API.
- https://nodejs.org/api/globals.html documents `AbortSignal.timeout`. Pass a signal into `fetch` and into retries.
