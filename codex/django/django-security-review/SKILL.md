---
id: "codex-django-security-review"
slug: "codex/django/django-security-review/SKILL"
title: "Django Security Review Skill for Codex"
description: "Review a Django change for permission checks, ORM query shape, and migration behavior. Use for a Django security review. Do not use for a non-Django project or to assume a database cascade runs Django signals."
type: "skill"
tools:
  - "codex"
stack: "django"
tags:
  - "django"
  - "python"
  - "orm"
  - "security"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Codex docs 2026-11-11; CLI not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "django@6.1.3"
updated_for: "Django 6.1.3, Nov 2026"
---

# Django Security Review Skill for Codex

## Install

Install the native export at `.agents/skills/django-security-review/SKILL.md` (one file shared with Antigravity CLI).
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Django Security Review

Shared skill `django-security-review` for Django. Codex and Antigravity CLI both read `.agents/skills/django-security-review/SKILL.md`. Install this one file. Codex calls it with `$django-security-review` or `/skills`. Do not also copy the Cursor skill to that path.

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

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: a comment says `Note.objects.filter(tenant=t).delete()` will run `Note.delete()`.
Output: high | notes/services.py:18 | `QuerySet.delete()` skips `Model.delete()` and still emits `pre_delete`/`post_delete` | call `note.delete()` when the override must run.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to migrate production or to disable auth tests.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
