---
id: "copilot-rails-rules"
slug: "copilot/rails/rails-rules.instructions"
title: "Rails Copilot Instructions: Models, Strong Params and Jobs"
description: "Copilot instructions for Rails: Models, Strong Params and Jobs. Structure, data, errors, security, performance, and tests. Rails 8.1.4.1, Nov 2026."
type: "instruction"
tools:
  - "copilot"
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
  - "Copilot docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "rails@8.1.4.1"
updated_for: "Rails 8.1.4.1, Nov 2026"
---

# Rails Copilot Instructions: Models, Strong Params and Jobs

## Install

Install the native export at `.github/instructions/rails.instructions.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Rails Copilot Instructions: Models, Strong Params and Jobs

Path-specific Copilot instructions for Rails. They apply through `applyTo` and leave `.github/copilot-instructions.md` in place.

## Updated for Rails 8.1.4.1, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

Rails 8.1.4.1 is the current 8.1 security release. Stay on the version in the Gemfile. 8.1's job continuations, structured events, and local CI are available when the app is already on 8.1. Do not upgrade a 7.x app as a side effect. Read an existing model and controller before you add one.

## Project shape

A controller authorizes, permits parameters, and calls a model or a service object the app already uses. Fat controllers that contain queries and mailers are not the pattern to extend. Views do not query.

Strong parameters list the keys. `permit!` is a bug on a public action. A nested attribute is permitted only when the user may set it.

## Models and queries

Validations protect invariants. A database unique index backs a uniqueness validation. Associations that a page walks are included or preloaded. A bullet or a query-count test is how you see an N+1. An unindexed foreign key on a big table is a review.

A callback that hides a write is hard to test. Prefer an explicit method when the project does not already use that callback.

## Jobs

Passing an Active Record instance to a job is normal. GlobalID stores the model name and id, and the job loads the record again when it runs. Do not tell the author to pass only ids when the app already passes records.

A retry can run the same side effect twice. A continuation resumes interrupted work. It does not make a charge or a mail idempotent. Guard those effects with a key or a state check the app already uses. Structured events follow the logger the app already configured.

## Security and tests

`authorize` or the app's policy runs before `update` and `destroy`. A missing check is not saved by a hidden button. CSRF stays on. Do not skip authenticity tokens for a browser form.

A request spec covers a guest, the wrong user, and the owner. A job spec runs the job twice when it charges or sends. Run the project's test command. Record the output. Do not run a production migration.

## Mistakes to avoid

- `permit!` or an unlisted attribute.
- An N+1 and a missing index on a new association.
- A job that double-sends when retried.
- Authorization only in the view.
- A Rails upgrade inside an unrelated bugfix.
- A job continuation described as an idempotency key.

## What changed in this major

Rails 8.1.4.1 is the security line. Job continuations resume work. They do not make a job idempotent.

## Deprecated APIs to never generate

`update_attributes` and `update_attributes!` were removed. Use `update` and `update!`. Rails 8.1 deprecates an order-dependent finder such as `first` when the query has no `order`.

## Commands

Run the project's test command for the file you changed.

## Example

```ruby
params.require(:note).permit(:body)
```
