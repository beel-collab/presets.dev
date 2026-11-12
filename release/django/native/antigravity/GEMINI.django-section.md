<!-- Append this section to GEMINI.md. Do not replace the existing file. Antigravity CLI also loads AGENTS.md, so do not paste this section into both. /context lists the loaded files. -->

# Django Antigravity CLI Rules: ORM, Permissions and Migrations

Section to append to `GEMINI.md` for Django. Antigravity CLI loads every `GEMINI.md` and every `AGENTS.md` it finds. Do not put this same section in both files. Confirm with `/context`.

## Updated for Django 6.1.3, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

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
- `mark_safe` on user text, or `@csrf_exempt` on a browser form.

## What changed in this major

Django 6.1 adds the fetch modes `FETCH_PEERS` and `FETCH_RAISE`. `QuerySet.delete()` sending `pre_delete` and `post_delete` while skipping `Model.delete()` is older queryset behavior, not a 6.1 change.

## Deprecated APIs to never generate

In Django 6.1, `values_list(flat=True)` with no field name is deprecated. Pass the field, as in `values_list("pk", flat=True)`. `select_related()` with no arguments is deprecated. Name the relations, or use `FETCH_PEERS`.

## Commands

Run `python manage.py test` for the app you changed.

## Example

The `Note.objects.filter(...).delete()` example above sends signals and skips `Note.delete()`.
