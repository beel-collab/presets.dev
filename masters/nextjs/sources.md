## Sources checked on 11 November 2026

- npm `latest` for `next` resolved to 16.4.6. The registry record lists Node `>=20.9.0` and a React 19 peer.
- GitHub release `v16.4.6` (9 November 2026) is a bugfix backport and does not add the Cache Components model by itself.
- GitHub release `v16.4.5` (3 November 2026) lists the security fixes.
- The Next.js post "November 2026 Security Release" names the patched versions 16.4.5 and 15.5.29 and describes the tenant, binary-argument, shell, response-framing, Edge cookie, and SVG issues. Advisory ids cited in the preset body were taken from that post and the matching GitHub advisories.
- Next.js docs for `use cache`, `next/root-params`, `cacheTag`, and revalidation, fetched the same day: explicit `cacheLife`, tags, `updateTag` inside Server Actions, `revalidateTag` with a cache profile, and the ban on `cookies()`, `headers()`, and `searchParams` inside a cached call stack.
- The decision table was executed with `node --test fixtures/nextjs/tenant-cache/policy.test.mjs` in this repository. Cursor, Copilot, Claude Code, Windsurf, Devin, Cline, Codex, and Gemini CLI were not launched.
