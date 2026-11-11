---
name: "rails-code-review"
description: "Review a Rails change for authorization, strong parameters, query counts, and job retries. Use for a Rails code review. Do not use for a non-Rails Ruby script or to migrate production."
---

# Rails Code Review Skill for Gemini CLI

Gemini CLI skill `rails-code-review` for Rails. Activation calls `activate_skill` and waits for consent. Keep this copy under `.gemini/skills`.

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
