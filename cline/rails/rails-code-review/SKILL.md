---
id: "cline-rails-code-review"
slug: "cline/rails/rails-code-review/SKILL"
title: "Rails Code Review Skill for Cline"
description: "Cline skill for a Rails code review. Use when you want that code review on a Rails change. Do not use it for a different stack."
type: "skill"
tools:
  - "cline"
stack: "rails"
tags:
  - "rails"
  - "ruby"
  - "jobs"
  - "code-review"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Cline docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "rails@8.1.4.1"
updated_for: "Rails 8.1.4.1, Nov 2026"
---

# Rails Code Review Skill for Cline

## Install

Install the native export at `.cline/skills/rails-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Rails Code Review Skill for Cline

Cline skill `rails-code-review` for Rails. `/rails-code-review` forces it. A global skill of the same name overrides this project file.

## When to run

Run this review for a Rails model, controller, migration, or job.

## When to leave it

Stop for Ruby that is not Rails. Do not upgrade Rails or migrate production.

## Steps

1. Read the Rails version in the Gemfile. A 7.x app receiving 8.1-only job APIs is a high finding unless the user asked to upgrade.
2. Review strong params and authorization on each write. `permit!` or a missing `authorize` is a high finding.
3. Review includes and indexes for new associations.
4. Review jobs for a second execution. A non-idempotent mail or charge is a high finding.
5. Run the test file only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the missing permit or the query, and a fix. Production was not migrated.

## Stop

Stop when the user asks you to skip CSRF or to permit every column.
