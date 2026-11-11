---
id: "windsurf-rails-rules"
slug: "windsurf/rails/rails-rules"
title: "Rails Windsurf Rules: Models, Strong Params and Jobs"
description: "Windsurf rules for Rails: Models, Strong Params and Jobs. Structure, data, errors, security, performance, and tests. Rails 8.1.4.1, Nov 2026."
type: "rule"
tools:
  - "windsurf"
stack: "rails"
tags:
  - "rails"
  - "ruby"
  - "jobs"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Devin and Cascade docs 2026-11-11; not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "rails@8.1.4.1"
updated_for: "Rails 8.1.4.1, Nov 2026"
---

# Rails Windsurf Rules: Models, Strong Params and Jobs

## Install

Install the native export at `.devin/rules/rails-rules.md` and, for legacy Cascade, `.windsurf/rules/rails-rules.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Rails Windsurf Rules: Models, Strong Params and Jobs

Rule for Rails on current Devin (`.devin/rules`) and legacy Cascade (`.windsurf/rules`). The trigger is model decision. Use `rails-code-review` for a review.

## Updated for Rails 8.1.4.1, Nov 2026

Rails 8.1.4.1 is the security release the November 2026 notes describe. Stay on the version in the Gemfile. 8.1's job continuations, structured events, and local CI are available when the app is already on 8.1. Do not upgrade a 7.x app as a side effect. Read an existing model and controller before you add one.

## Project shape

A controller authorizes, permits parameters, and calls a model or a service object the app already uses. Fat controllers that contain queries and mailers are not the pattern to extend. Views do not query.

Strong parameters list the keys. `permit!` is a bug on a public action. A nested attribute is permitted only when the user may set it.

## Models and queries

Validations protect invariants. A database unique index backs a uniqueness validation. Associations that a page walks are included or preloaded. A bullet or a query-count test is how you see an N+1. An unindexed foreign key on a big table is a review.

A callback that hides a write is hard to test. Prefer an explicit method when the project does not already use that callback.

## Jobs

A job that retries must be safe to run twice. Use a continuation or an idempotency key when 8.1 continuations fit the existing job style. Do not enqueue a job with a huge Active Record object if the project passes ids. Structured events follow the logger the app already configured.

## Security and tests

`authorize` or the app's policy runs before `update` and `destroy`. A missing check is not saved by a hidden button. CSRF stays on. Do not skip authenticity tokens for a browser form.

A request spec covers a guest, the wrong user, and the owner. A job spec runs the job twice when it charges or sends. Run the project's test command. Record the output. Do not run a production migration.

## Mistakes to avoid

- `permit!` or an unlisted attribute.
- An N+1 and a missing index on a new association.
- A job that double-sends when retried.
- Authorization only in the view.
- A Rails upgrade inside an unrelated bugfix.
