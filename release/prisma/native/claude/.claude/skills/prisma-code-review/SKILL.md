---
name: "prisma-code-review"
description: "Review a Prisma schema, migration, or query for data loss, N+1 reads, and unsafe raw SQL. Use for a Prisma code review. Do not use to apply a migration to production or to upgrade onto the Prisma 8 release candidate."
---

# Prisma Code Review Skill for Claude Code

Claude Code skill `prisma-code-review` for Prisma. The command is `/prisma-code-review`. Leave the normal permission prompts on.

## When to run

Run this review for a Prisma schema change, a migration, a query, or "is this safe to migrate".

## When to leave it

Stop if the user asks you to apply the migration to production or to reset a shared database. Review the files. Do not connect to production.

## Steps

1. Read the installed Prisma major. If the diff bumps to 8 while the app is on 7, that is a high finding unless the user asked for the RC. npm `latest` being an RC is not approval.
2. Read the new migration. A destructive drop, a required column without a default or backfill, or an edit to an old migration folder is a high finding.
3. Confirm no script points the shadow database or `migrate dev` at a production URL.
4. Review queries in the diff for per-row `findUnique`, unbounded `findMany`, and raw SQL built with string concatenation. Each is a finding, high when user input is concatenated.
5. Check that writes which must be atomic sit in a transaction, and that the transaction does not wrap a slow third-party call.
6. Do not run a migrate command. If a local disposable test exists and the user asked to run it, record the output. Otherwise write `not run`.

## Output

Findings with severity, file, line, the schema or query risk, and a safer change. State that production was not touched.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: `src/db.ts` on Prisma 7 does `new PrismaClient()` with no adapter.
Output: high | src/db.ts:4 | Prisma 7 requires a driver adapter | `import { PrismaClient } from "./generated/prisma/client"` and `import { PrismaPg } from "@prisma/adapter-pg"`, then `new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) })`. `prisma.config.ts` is only for the CLI.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks for `migrate reset`, a production deploy, or a silent jump to Prisma 8.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
