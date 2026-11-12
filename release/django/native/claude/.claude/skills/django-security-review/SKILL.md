---
name: "django-security-review"
description: "Review a Django change for permission checks, ORM query shape, and migration behavior. Use for a Django security review. Do not use for a non-Django project or to assume a database cascade runs Django signals."
---

# Django Security Review Skill for Claude Code

Claude Code skill `django-security-review` for Django. The command is `/django-security-review`. Leave the normal permission prompts on.

## When to run

Run this review for a Django view, model, form, or migration.

## When to leave it

Stop for a non-Django repository. Do not upgrade Django or run a migration against production.

## What to check

- Injection: `raw()`, `extra()`, and `.raw` SQL built with f-strings or `%` formatting. Parameters are the safe form.
- XSS: `|safe`, `mark_safe`, and `format_html` on user text without escaping.
- CSRF: a state-changing view that is `@csrf_exempt` without a documented machine client.
- Secrets: a key or password in settings committed to the tree, or logged on the request.
- IDOR: a queryset that loads by the posted id and never checks the owner or a permission.
- SSRF: a view that `requests.get`s a URL the user supplied, with no host allow-list.
- Mass assignment: a model form with `fields = "__all__"` facing the browser.
- Uploads: a file stored with the original name and no type or size check.

## Steps

1. Read the installed Django version. A 6.1-only fetch mode or delete option on an older install is a high finding.
2. Review permission checks on every changed write. A missing check is a high finding. A form with `fields = "__all__"` facing users is a high finding.
3. Review querysets for per-row queries. `update()` sends no signals. `QuerySet.delete()` sends `pre_delete` and `post_delete` but skips `Model.delete()`. A database `ON DELETE CASCADE` sends nothing. Flag a comment or a test that assumes the wrong one of those three. Do not flag `QuerySet.delete()` itself for "no signals".
4. Review migrations for edits to shipped files and for destructive drops bundled with unrelated code.
5. Check async views for a direct ORM call.
6. Run the app's tests only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the permission or query issue, and a fix. State that production was not migrated.

## Stop

Stop when the user asks you to migrate production or to disable auth tests.
