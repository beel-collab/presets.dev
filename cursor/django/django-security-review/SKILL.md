---
id: "cursor-django-security-review"
slug: "cursor/django/django-security-review/SKILL"
title: "Django Security Review Skill for Cursor"
description: "Cursor skill for a Django security review. Use when you want that security review on a Django change. Do not use it for a different stack."
type: "skill"
tools:
  - "cursor"
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
  - "Cursor docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "django@6.1.3"
updated_for: "Django 6.1.3, Nov 2026"
---

# Django Security Review Skill for Cursor

## Install

Install the native export at `.cursor/skills/django-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Django Security Review Skill for Cursor

Cursor skill `django-security-review` for Django. Run it with `/django-security-review`, or let Agent select it when the request matches. `paths` only limits automatic surfacing.

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
