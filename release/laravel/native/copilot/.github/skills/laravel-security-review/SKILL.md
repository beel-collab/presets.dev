---
name: "laravel-security-review"
description: "Review a Laravel change for policies, Form Request validation, and mass assignment. Use for a Laravel security review. Do not use for a non-Laravel PHP script or to run a migration against production."
---

# Laravel Security Review Skill for Copilot

Copilot skill `laravel-security-review` for Laravel. The description decides when Copilot loads it. Keep this copy under `.github/skills`.

## When to run

Run this review for a Laravel controller, Form Request, policy, Eloquent write, or job.

## When to leave it

Stop for PHP that is not Laravel. Do not upgrade Laravel or migrate production.

## What to check

- Injection: `DB::raw`, `whereRaw`, and `selectRaw` with concatenated user input. Bindings are the safe form.
- XSS: `{!! !!}` on user text.
- CSRF: a web route that disables `ValidateCsrfToken`.
- Secrets: a key in `.env` that was committed, or a token written to the log.
- IDOR: a route-model binding or `find($id)` that never calls a policy.
- SSRF: `Http::get($request->input('url'))` with no allow-list.
- Mass assignment: `$request->all()` into `create` or `update`, or a model `$guarded = []` on a public write.
- Uploads: `storeAs` with the client filename and no mime or size rule.

## Steps

1. Read the Laravel and PHP constraints in `composer.json`. An incompatible package is a high finding.
2. For each write, confirm a policy or gate and a Form Request. `$request->all()` passed to the model is a high finding.
3. Review list queries for missing eager loads.
4. Review jobs for a second-run story. A non-idempotent charge or email is a high finding.
5. Confirm CSRF and `auth` middleware still apply.
6. Run the project's test command only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the missing check, and a fix. Production was not migrated.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: a controller does `Note::create($request->all())`.
Output: high | app/Http/Controllers/NoteController.php:16 | mass assignment from the whole request | `Note::create($request->validated())`.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to turn CSRF off or to mass-assign for speed.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
