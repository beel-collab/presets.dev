# Django sources

Fetched 12 November 2026.

- Registry: https://pypi.org/pypi/Django/json reports 6.1.3.
- https://docs.djangoproject.com/en/6.1/releases/6.1/ documents `FETCH_PEERS` and `FETCH_RAISE`.
- https://docs.djangoproject.com/en/6.1/ref/models/querysets/#delete says `QuerySet.delete()` emits `pre_delete` and `post_delete` for deleted objects, including cascaded deletions, and does not call `delete()` on the models. Signals are not sent when `DB_CASCADE` is used. `update()` writes SQL and emits no save signals.
- https://docs.djangoproject.com/en/6.1/ref/csrf/ documents `csrf_exempt`. A browser form should not use it.
- https://docs.djangoproject.com/en/6.1/ref/utils/ documents `mark_safe`. Do not mark user text safe.
