---
id: "copilot-supabase-security-review"
slug: "copilot/supabase/supabase-security-review/SKILL"
title: "Supabase Security Review Skill for Copilot"
description: "Copilot skill for a Supabase security review. Use when you want that security review on a Supabase change. Do not use it for a different stack."
type: "skill"
tools:
  - "copilot"
stack: "supabase"
tags:
  - "supabase"
  - "postgres"
  - "rls"
  - "auth"
  - "security"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Copilot docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "@supabase/supabase-js@2.119.0"
updated_for: "supabase-js 2.119.0, Nov 2026"
---

# Supabase Security Review Skill for Copilot

## Install

Install the native export at `.github/skills/supabase-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

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
