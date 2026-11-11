---
id: "windsurf-django-rules"
slug: "windsurf/django/django-rules"
title: "Django Windsurf Rules: ORM, Permissions and Migrations"
description: "Windsurf rules for Django: ORM, Permissions and Migrations. Structure, data, errors, security, performance, and tests. Django 6.1.3, Nov 2026."
type: "rule"
tools:
  - "windsurf"
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
  - "Devin and Cascade docs 2026-11-11; not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "django@6.1.3"
updated_for: "Django 6.1.3, Nov 2026"
---

# Django Windsurf Rules: ORM, Permissions and Migrations

## Install

Install the native export at `.devin/rules/django-rules.md` and, for legacy Cascade, `.windsurf/rules/django-rules.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Django Windsurf Rules: ORM, Permissions and Migrations

Rule for Django on current Devin (`.devin/rules`) and legacy Cascade (`.windsurf/rules`). The trigger is model decision. Use `django-security-review` for a review.

## Updated for Django 6.1.3, Nov 2026

Django 6.1.3 is the PyPI version checked on 11 November 2026. Django 6.1 adds fetch modes such as `FETCH_PEERS` and `FETCH_RAISE`, database-level delete options, and `MAILERS`. Use a 6.1 API only when the installed Django is 6.1. Read `settings` and an existing view before you add one. Do not upgrade Django as a side effect.

## Project shape

An app owns its models, forms, and views. A view checks permission, validates input, and calls a function or a model method. Business rules do not pile up in the view. Settings come from environment-backed settings, not a new hardcoded secret.

Use the project's auth decorators or mixins. A class-based view and a function view follow the one the app already uses.

## ORM

`select_related` and `prefetch_related` match the template or serializer that walks relations. A loop that queries per row is an N+1. Assert the query count in a test when the project already does that.

A queryset is filtered before it is evaluated. Do not `list(Model.objects.all())` and filter in Python. `update()` and `delete()` on a queryset are SQL. They do not run model `save()` or signals unless the project is on a path that does. A database `ON DELETE CASCADE` does not run Django's `delete()` signals. If you need the signal, delete through the model instance or the collector the project uses.

Fetch modes in 6.1 are explicit. `FETCH_RAISE` is how you stop a lazy query you did not expect. Do not add it blindly to every relation. Read what the view actually touches.

## Forms, auth, and migrations

A form or a serializer lists the fields it accepts. `fields = "__all__"` on a model form that faces the user is a review. Permission checks happen before the write, including for a custom action. Do not trust a user id in the POST body.

Migrations are additive and reviewed. A data migration is idempotent. Do not edit a migration that has shipped. A destructive column drop is its own change after the code has stopped reading the column.

## Async and tests

A sync ORM call does not run directly inside an async view. Use the project's `sync_to_async` or keep the view synchronous. Do not mix them ad hoc.

The test client covers an anonymous user, a user without the permission, and the owner. `assertNumQueries` guards the page you changed. Run the project's test command. Record the output.

## Mistakes to avoid

- An N+1 in a list view.
- Assuming a database cascade runs `post_delete`.
- `fields = "__all__"` on a public form.
- A sync query inside an async view.
- A shipped migration rewritten in place.
