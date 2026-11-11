---
name: "prisma-code-review"
description: "Review a Prisma schema, migration, or query for data loss, N+1 reads, and unsafe raw SQL. Use for a Prisma code review. Do not use to apply a migration to production or to upgrade onto the Prisma 8 release candidate."
---

# Prisma Code Review Skill for Cline

Cline skill `prisma-code-review` for Prisma. `/prisma-code-review` forces it. A global skill of the same name overrides this project file.

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

## Stop

Stop when the user asks for `migrate reset`, a production deploy, or a silent jump to Prisma 8.
