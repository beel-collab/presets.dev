---
name: "supabase-security-review"
description: "Review a Supabase change for RLS gaps, service-role keys in clients, and auth that trusts a caller-supplied user id. Use for a Supabase security review. Do not use for a non-Supabase repository or to apply SQL against production."
---

# Supabase Security Review Skill for Copilot

Copilot skill `supabase-security-review` for Supabase. The description decides when Copilot loads it. Keep this copy under `.github/skills`.

## When to run

Run this review for a Supabase change: a new table, a policy, a client call, or a request to "check auth" or "review RLS".

## When to leave it

Stop for a repository that does not use Supabase. Do not run SQL against a hosted production database. Do not print keys.

## Steps

1. Read the installed `@supabase/supabase-js` version. Note where the browser client and the server client are constructed.
2. Search the diff for the service-role key, `service_role`, and a database connection string. A hit in client code or a committed env file is a high finding.
3. For each new or changed table, confirm row level security is on. For each write policy, confirm `WITH CHECK`. A policy of `using (true)` on private data is a high finding.
4. For each client write, confirm the user and tenant come from the session. A body field named `user_id` or `tenant_id` that is stored is a high finding.
5. For each realtime subscription, confirm a filter and a cleanup. A payload that includes a token is a high finding.
6. Look for a test or a local reproduction with two users. Missing coverage on a new policy is a medium finding. Do not apply a migration to production to "see if it works".

## Output

Findings with severity, file, line, the policy or key path, and a fix. End with `no file edits` unless a fix was requested, and never include a secret in the report.

## Stop

Stop when the user asks you to disable RLS, to use the service role in the browser, or to run against production.
