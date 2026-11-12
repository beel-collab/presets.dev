# PR #2 review fixes: master checklist (two independent reviews, 12 Nov 2026)

Rule: work ONE ITEM AT A TIME. For each item: (1) verify against the official source (fetch it, record URL), (2) if valid, fix it in masters/ or the generator, (3) regenerate, (4) tick it here with status (fixed / partially valid / rejected-invalid), the source URL, and the files changed. Nothing may be skipped silently. If an item is invalid after checking, record why with the source.

## A. Factual errors (fix first)

- [x] A1 MCP: **fixed.** `@modelcontextprotocol/sdk` 1.32.2 does not speak 2026-07-28; v2 `@modelcontextprotocol/server` 2.4.0 does, via `serveStdio` / `createMcpHandler`. `initialize` and `Mcp-Session-Id` are removed. Sources: https://modelcontextprotocol.io/specification/2026-07-28/changelog and https://ts.sdk.modelcontextprotocol.io/v2/migration/upgrade-to-v2 . Files: `masters/mcp/standards.md`, `masters/mcp/skill.md`, `masters/mcp/stack.json`, `research/mcp/sources.md`, regenerated catalog. targets 2026-07-28 spec with @modelcontextprotocol/sdk 1.32, which does not support it. Spec support is in v2 split packages (@modelcontextprotocol/server, /client, /node etc; createMcpHandler, serveStdio). initialize/initialized handshake and Mcp-Session-Id sessions are REMOVED in 2026-07-28 (server/discover, _meta per request, MRTR, resultType, subscriptions/listen). Remove "legacy handshake" language that assumes initialize exists. Src: https://modelcontextprotocol.io/specification/2026-07-28/changelog , https://ts.sdk.modelcontextprotocol.io/v2/migration/upgrade-to-v2
- [ ] A2 MCP: a "confirm" tool argument is model-written, so it is not user consent. Require host/client-side human approval (elicitation / input_required, host UI) for destructive tools.
- [ ] A3 Prisma: claims 7.x but omits v7 changes: prisma.config.ts, required driver adapters, new generator (prisma-client, output path), etc. Accelerate URLs retire 2026-12-01 (verify). Prisma query-rule globs never load (fix globs).
- [ ] A4 Supabase: anon/service_role key names being deprecated in favour of publishable/secret keys (verify, then document both). WITH CHECK is invalid on DELETE policies; UPDATE falls back to USING when WITH CHECK omitted. Review per operation (INSERT checks new rows, DELETE filters existing, UPDATE both). Realtime filter is NOT a security boundary (RLS/Realtime authorization is). Add a valid delete + safe update as must-not-flag cases. Src: postgresql CREATE POLICY docs, Supabase RLS docs.
- [ ] A5 TypeScript: says 7.0 has a new compiler API. Verify what 7.0 actually ships re programmatic API and state it accurately.
- [ ] A6 Vue: since 3.5, destructuring defineProps() in <script setup> stays reactive (compiler transform). Keep warning for reactive()/store destructuring (storeToRefs). Skill must not flag correct 3.5 props destructuring.
- [ ] A7 SwiftUI: only the .task {} modifier is cancelled when the view disappears; plain Task {} is unstructured. Keep handle + cancel, cooperative cancellation.
- [ ] A8 NestJS: flags correct Nest 12 @Body({ schema }) validation as high. Verify Nest 12 feature and fix.
- [ ] A9 Go: json/v2 is stable in 1.27 and backs encoding/json (GOEXPERIMENT=nojsonv2 opt-out). SIMD remains experimental. Src https://go.dev/doc/go1.27
- [ ] A10 Rails: job continuations are not an idempotency mechanism. Passing records to jobs (GlobalID) is idiomatic; don't advise against it.
- [ ] A11 Laravel: CSRF middleware is ValidateCsrfToken (Laravel 11+), not VerifyCsrfToken. SerializesModels already serializes only model identifiers; fix the job-serialization advice.
- [ ] A12 Svelte: names Kit 3 but describes Kit 2. Kit 3: svelte.config.js unsupported (config in sveltekit() Vite plugin), $app/stores removed (use $app/state), $lib replaced by #lib via package.json imports with explicit extensions, min Node 22.17/TS 6/Vite 8. Src https://svelte.dev/docs/kit/migrating-to-sveltekit-3
- [ ] A13 Angular: v22 OnPush is default (Default renamed Eager), @Service decorator (inject() only), injectAsync, signal forms stable. Control flow @if/@for/@switch is standard since v17 (NOT new in 22) — include as baseline. Src https://angular.dev/guide/components/advanced-configuration , https://angular.dev/guide/di/creating-and-using-services
- [ ] A14 Next.js: middleware.ts is now proxy.ts (Next 16+). Update wording.
- [ ] A15 Nuxt: remove "rune" (Svelte term).
- [ ] A16 Rust: "don't hold a lock across .await" is wrong for tokio::sync::Mutex; scope it to std/parking_lot guards.
- [ ] A17 Spring: add the @Transactional/@Async self-invocation (proxy) bug.
- [ ] A18 Version headers outdated: Rust 1.100 and Flutter 3.50 reportedly shipped this week — verify every stack's version header against official release pages on the day you edit.
- [ ] A19 React Native: a stack screen does NOT unmount on navigate-away; use useFocusEffect for focus-owned work, effect cleanup for unmount. Src reactnavigation.org navigation-lifecycle.
- [ ] A20 Django: QuerySet.delete() DOES emit pre_delete/post_delete (incl. Django-managed cascades) but bypasses model delete() overrides; update() emits no signals; DB-level cascade separate. Add small example.
- [ ] A21 Next.js fixture/standards: cache tags are for invalidation, not isolation; cache key (args/captured values) provides tenant isolation. Fix policy.mjs and standards; add safe (shared tag, tenant in key) and unsafe examples; severity tied to real consequence.
- [ ] A22 Terraform: wildcard Resource "*" is required for some AWS actions without resource-level permissions; flag permissions broader than needed, not the "*" character alone.
- [ ] A23 Python: skill forces `uv run`; detect and use the repo's documented test command (poetry, pip venv, hatch, tox); uv only when uv owns the project. Fix "for a review" line.
- [ ] A24 Django and Laravel security-review skills: rework to cover injection (SQL/ORM raw), XSS, CSRF, secrets, IDOR/authorization, SSRF, mass assignment, file upload.

## B. Fixes across all 30 stacks (template/generator)

- [ ] B1 Every rules file gets: "What changed in this major" (exact import/config names), "Deprecated APIs to never generate", and one line of lint/type/test/security commands.
- [ ] B2 Every skill gets: severity scale, output template, explicit "no findings" case, at least one worked input/output example, and a valid-code case it must NOT flag.
- [ ] B3 All security-review skills get real checks: injection, XSS, CSRF, secrets, IDOR, SSRF (+ stack-specific).
- [ ] B4 Fix globs: too broad (**/*.ts for MCP, NestJS, Express — scope to real paths/files, e.g. *.controller.ts, *.module.ts, server files); too narrow (Prisma query code never loads — include files importing @prisma/client patterns/paths; Docker must include docker-compose*.yml/yaml and Dockerfile.*). Audit all 30.
- [ ] B5 Catalog skill descriptions: use native_skill_description text, not "Use when you want that code review…".
- [ ] B6 Add agent tooling references where real: Next.js bundled docs/AGENTS.md, MCP servers for Next.js, Laravel Boost, Playwright (incl. Playwright test agents), Angular, Svelte. Verify each exists with official URL.
- [ ] B7 research/*/sources.md: real URLs for every version and behaviour claim; read release notes/migration guides, not only the latest version number. Remove "did not re-fetch" notes by actually fetching.
- [ ] B8 Cleanups: remove dated "npm latest checked…" text from rule bodies (keep date in updated_for metadata); remove skill-install boilerplate from rules files; fix Python "for a review" line.
- [ ] B9 Tools: Gemini CLI stopped serving personal accounts on 18 Jun 2026; Antigravity CLI replaces it (reads GEMINI.md, imports skills). Replace gemini-cli target with Antigravity CLI using Antigravity CLI's documented paths (verify at https://antigravity.google/docs/cli/ ); update schema, CONTRIBUTING, README, counts, stacks.json. Keep existing antigravity/ legacy dir semantics consistent — decide and document whether Antigravity CLI shares the antigravity tool id.
- [ ] B10 Windsurf: install to ONE target (.devin/ current, or .windsurf/ legacy per current docs), not both.
- [ ] B11 Add worked code examples to standards where they clarify a rule (currently only Next.js has one).
- [ ] B12 Add a release check that every release entry would get a generated page (index check), and keep tested_with honest.
- [ ] B13 README: short section on the original release, the 30 stacks, where native install files live, how to install one.

## C. Website (separate repo, NOT this PR — list in the PR description as companion work)

- [ ] C1 Copy/download must serve release/<stack>/native payloads (catalog skills lack native `name`).
- [ ] C2 Index the new tool and Claude rules layout (claude/<stack>/<stack>-rules.md); 90 entries currently skipped.
- [ ] C3 Append-only install for AGENTS.md/GEMINI.md/CLAUDE.md.

## D. Retirement (document only)

- [ ] D1 Main has 854 entries / 97 technologies; release has 420 / 30, zero agents, no AWS/Azure/Kubernetes/accessibility. Produce release/original-2026-11/retirement-map.json mapping each old preset to a new preset or explicit "retire" with redirect target. Do not delete anything.

## Not checked by me (verify before fixing)

A3 Accelerate date, A4 key deprecation, A5 TS7 API, A8 Nest 12 @Body({schema}), A18 Rust 1.100 / Flutter 3.50, B6 each MCP server/tool.
