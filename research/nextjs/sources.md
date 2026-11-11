# Next.js sources

Checked 11 November 2026.

- npm `latest` for `next` was 16.4.6. Engines require Node `>=20.9.0`. The React peer includes React 19.
- GitHub release `v16.4.6` (9 November 2026) is a bugfix backport.
- GitHub release `v16.4.5` (3 November 2026) and the Next.js post "November 2026 Security Release" name the patched versions 16.4.5 and 15.5.29. The advisories cover cross-tenant `use cache` leaks, binary cache arguments, shared fallback shells, forwarded responses, Edge cookie headers, and SVG image optimization.
- Docs checked the same day: `use cache`, `next/root-params`, `cacheTag`, `updateTag`, and `revalidateTag` with a cache profile.
- `node --test fixtures/nextjs/tenant-cache/policy.test.mjs` locks the version floor used by the review skill. It does not boot Next.js.
- Cursor, Copilot, Claude Code, Windsurf, Devin, Cline, Codex, and Gemini CLI were not launched. Format notes are in the install section of each catalog file.
