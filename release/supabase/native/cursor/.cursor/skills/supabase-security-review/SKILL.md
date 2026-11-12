---
name: "supabase-security-review"
description: "Review a Supabase change for RLS gaps, service-role keys in clients, and auth that trusts a caller-supplied user id. Use for a Supabase security review. Do not use for a non-Supabase repository or to apply SQL against production."
paths:
  - "**/*supabase*"
  - "**/*.sql"
---

# Supabase Security Review Skill for Cursor

Cursor skill `supabase-security-review` for Supabase. Run it with `/supabase-security-review`, or let Agent select it when the request matches. `paths` only limits automatic surfacing.

## When to run

Run this review for a Supabase change: a new table, a policy, a client call, or a request to "check auth" or "review RLS".

## When to leave it

Stop for a repository that does not use Supabase. Do not run SQL against a hosted production database. Do not print keys.

## Steps

1. Read the installed `@supabase/supabase-js` version. Note where the browser client and the server client are constructed.
2. Search the diff for `service_role`, `sb_secret_`, and a database connection string. A hit in client code or a committed env file is a high finding. A publishable or `anon` key in the browser, paired with RLS, is not a finding.
3. For each new or changed table, confirm row level security is on. Read policies by command. An `INSERT` without `WITH CHECK`, or a `DELETE` that uses `WITH CHECK`, is a high finding. An `UPDATE` that sets `USING` and omits `WITH CHECK` is valid: Postgres applies `USING` to the new row. A `DELETE` policy of `USING (auth.uid() = user_id)` is valid. Do not flag either. A policy of `using (true)` on private data is a high finding.
4. For each client write, confirm the user and tenant come from the session. A body field named `user_id` or `tenant_id` that is stored is a high finding.
5. For each realtime subscription, confirm cleanup. A filter is not a security control. Missing RLS or Realtime authorization on a private table is a high finding. A payload that includes a token is a high finding.
6. Look for a test or a local reproduction with two users. Missing coverage on a new policy is a medium finding. Do not apply a migration to production to "see if it works".

## Output

Findings with severity, file, line, the policy or key path, and a fix. End with `no file edits` unless a fix was requested, and never include a secret in the report.

## Stop

Stop when the user asks you to disable RLS, to use the service role in the browser, or to run against production.
