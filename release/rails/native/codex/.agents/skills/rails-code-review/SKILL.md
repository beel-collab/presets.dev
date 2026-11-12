---
name: "rails-code-review"
description: "Review a Rails change for authorization, strong parameters, query counts, and job retries. Use for a Rails code review. Do not use for a non-Rails Ruby script or to migrate production."
---

# Rails Code Review Skill for Codex

Codex skill `rails-code-review` for Rails. Call it with `$rails-code-review` or `/skills`. Do not install the other tools' copies beside it.

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

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: a job comment says `include ActiveJob::Continuable` makes the import idempotent.
Output: medium | app/jobs/process_import_job.rb:3 | continuations resume the last step; they do not dedupe side effects | make each step safe to run again, separately from the continuation.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to skip CSRF or to permit every column.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
