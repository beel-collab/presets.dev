---
name: "laravel-security-review"
description: "Review a Laravel change for policies, Form Request validation, and mass assignment. Use for a Laravel security review. Do not use for a non-Laravel PHP script or to run a migration against production."
---

# Laravel Security Review Skill for Claude Code

Claude Code skill `laravel-security-review` for Laravel. The command is `/laravel-security-review`. Leave the normal permission prompts on.

## When to run

Run this review for a Laravel controller, Form Request, policy, Eloquent write, or job.

## When to leave it

Stop for PHP that is not Laravel. Do not upgrade Laravel or migrate production.

## Steps

1. Read the Laravel and PHP constraints in `composer.json`. An incompatible package is a high finding.
2. For each write, confirm a policy or gate and a Form Request. `$request->all()` passed to the model is a high finding.
3. Review list queries for missing eager loads.
4. Review jobs for a second-run story. A non-idempotent charge or email is a high finding.
5. Confirm CSRF and `auth` middleware still apply.
6. Run the project's test command only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the missing check, and a fix. Production was not migrated.

## Stop

Stop when the user asks you to turn CSRF off or to mass-assign for speed.
