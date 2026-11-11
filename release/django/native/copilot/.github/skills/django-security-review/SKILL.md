---
name: "django-security-review"
description: "Review a Django change for permission checks, ORM query shape, and migration behavior. Use for a Django security review. Do not use for a non-Django project or to assume a database cascade runs Django signals."
---

# Django Security Review Skill for Copilot

Copilot skill `django-security-review` for Django. The description decides when Copilot loads it. Keep this copy under `.github/skills`.

## When to run

Run this review for a Django view, model, form, or migration.

## When to leave it

Stop for a non-Django repository. Do not upgrade Django or run a migration against production.

## Steps

1. Read the installed Django version. A 6.1-only fetch mode or delete option on an older install is a high finding.
2. Review permission checks on every changed write. A missing check is a high finding. A form with `fields = "__all__"` facing users is a high finding.
3. Review querysets for per-row queries and for `update` or `delete` that the author thinks will run signals. A database cascade treated as a Django signal is a high finding when the code depends on that signal.
4. Review migrations for edits to shipped files and for destructive drops bundled with unrelated code.
5. Check async views for a direct ORM call.
6. Run the app's tests only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the permission or query issue, and a fix. State that production was not migrated.

## Stop

Stop when the user asks you to migrate production or to disable auth tests.
