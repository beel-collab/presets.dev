---
paths:
  - "**/*.php"
---

# Laravel Claude Code Rules: Requests, Policies and Eloquent

Path-scoped Claude Code rule for Laravel. It loads when a matching file is read. It does not replace `CLAUDE.md`.

## Updated for Laravel 13, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

Laravel 13 requires PHP 8.3 through 8.5. Read `composer.json` and stay inside that range. Do not add a package that only supports an older PHP, and do not bump Laravel unless the task asks. Use the app's existing structure: controllers, Form Requests, policies, and jobs.

## Project shape

A controller method authorizes, takes a Form Request, and calls an action or a model. Validation does not live in the controller as a hand-rolled `if`. A Form Request owns the rules and `authorize` when that is the local pattern. Policies own model authorization. Do not duplicate the same check as a gate, a policy, and an inline `if` that can drift.

## Eloquent

List the fillable or guarded fields. `$request->all()` passed to `create` or `update` is mass assignment. Pass `$request->validated()`.

A list page eager-loads the relations it displays. A loop that queries is an N+1. Paginate. A global scope that hides rows is documented, because it also hides them from jobs.

## Jobs and errors

A job that retries is idempotent. The database write uses a unique key or a transaction so a second run does not double-charge. `SerializesModels` already stores the model identifier and reloads the row when the job runs. Passing the model is the normal shape. Do not rewrite it into a hand-rolled id unless the job must not use that trait.

Exceptions render through the project's handler. Do not `dd()` or return a stack to the user. Log the context without the password or the token.

## Security and tests

Every state-changing route has middleware and a policy. A route missing `auth` is a review. CSRF stays on for session forms. On Laravel 13 the middleware class is `PreventRequestForgery`. `ValidateCsrfToken` and `VerifyCsrfToken` are deprecated aliases. Do not generate the aliases. Do not disable the middleware for a web route to make a test pass.

Feature tests hit the endpoint as a guest, as the wrong user, and as the owner. Assert the status and the database. Run `php artisan test` or the project's Pest command for the file you touched. Record the output.

## Mistakes to avoid

- `$request->all()` into `create`.
- A missing policy on a new write.
- An N+1 on a list.
- A job that is not safe to run twice.
- A package that does not support the project's PHP.

## What changed in this major

Laravel 13 runs on PHP 8.3 through 8.5. CSRF middleware is `PreventRequestForgery`.

## Deprecated APIs to never generate

`ValidateCsrfToken` and `VerifyCsrfToken` are deprecated aliases of `PreventRequestForgery`. Generate `PreventRequestForgery`.

## Commands

Run `php artisan test` for the file you changed.

## Example

```php
Note::create($request->validated());
```
## Agent tooling

Laravel Boost (`composer require laravel/boost --dev`, then `php artisan boost:install`) installs guidelines and an MCP server. It edits only its own block in an existing `AGENTS.md`. See https://laravel.com/docs/13.x/boost .
