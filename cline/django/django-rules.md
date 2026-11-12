---
id: "cline-django-rules"
slug: "cline/django/django-rules"
title: "Django Cline Rules: ORM, Permissions and Migrations"
description: "Cline rules for Django: ORM, Permissions and Migrations. Structure, data, errors, security, performance, and tests. Django 6.1.3, Nov 2026."
type: "rule"
tools:
  - "cline"
stack: "django"
tags:
  - "django"
  - "python"
  - "orm"
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
  - "django@6.1.3"
updated_for: "Django 6.1.3, Nov 2026"
---

# Django Cline Rules: ORM, Permissions and Migrations

## Install

Install the native export at `.clinerules/django-rules.md` (do not also copy it to `.cline/rules/`).
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Django Cline Rules: ORM, Permissions and Migrations

Conditional Cline rule for Django. Install it under `.clinerules/` only.

## Updated for Django 6.1.3, Nov 2026

## Project shape

An app owns its models, forms, and views. A view checks permission, validates input, and calls a function or a model method. Business rules do not pile up in the view. Settings come from environment-backed settings, not a new hardcoded secret.

Use the project's auth decorators or mixins. A class-based view and a function view follow the one the app already uses.

## ORM

`select_related` and `prefetch_related` match the template or serializer that walks relations. A loop that queries per row is an N+1. Assert the query count in a test when the project already does that.

A queryset is filtered before it is evaluated. Do not `list(Model.objects.all())` and filter in Python. `QuerySet.update()` is SQL. It does not call `save()` and it does not send signals. `QuerySet.delete()` does send `pre_delete` and `post_delete`, including for rows Django cascades in Python. It does not call your model's `delete()` method, so an override there does not run. A database `ON DELETE CASCADE` is separate: the database removes the row and Django does not send a signal for that child. If the override must run, iterate instances and call `delete()` on each.

```python
Note.objects.filter(tenant=tenant).delete()  # signals fire, Note.delete() does not
for note in Note.objects.filter(tenant=tenant):
    note.delete()  # the override runs
```

Fetch modes in 6.1 are explicit. `FETCH_RAISE` is how you stop a lazy query you did not expect. Do not add it blindly to every relation. Read what the view actually touches.

## Forms, auth, and migrations

A form or a serializer lists the fields it accepts. `fields = "__all__"` on a model form that faces the user is a review. Permission checks happen before the write, including for a custom action. Do not trust a user id in the POST body.

Migrations are additive and reviewed. A data migration is idempotent. Do not edit a migration that has shipped. A destructive column drop is its own change after the code has stopped reading the column.

## Async and tests

A sync ORM call does not run directly inside an async view. Use the project's `sync_to_async` or keep the view synchronous. Do not mix them ad hoc.

The test client covers an anonymous user, a user without the permission, and the owner. `assertNumQueries` guards the page you changed. Run the project's test command. Record the output.

## Mistakes to avoid

- An N+1 in a list view.
- Assuming `QuerySet.delete()` runs `Model.delete()`, or that a database cascade sends `post_delete`.
- `fields = "__all__"` on a public form.
- A sync query inside an async view.
- A shipped migration rewritten in place.

## What changed in this major

Django 6.1 adds `FETCH_PEERS` and `FETCH_RAISE`. `QuerySet.delete()` sends delete signals and skips `Model.delete()`.

## Deprecated APIs to never generate

Do not generate `mark_safe` on user text, or `@csrf_exempt` on a browser form.

## Commands

Run `python manage.py test` for the app you changed.

## Example

The `Note.objects.filter(...).delete()` example above sends signals and skips `Note.delete()`.
