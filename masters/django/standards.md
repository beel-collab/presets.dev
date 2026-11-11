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
