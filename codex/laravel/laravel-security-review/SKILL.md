---
id: "codex-laravel-security-review"
slug: "codex/laravel/laravel-security-review/SKILL"
title: "Laravel Security Review Skill for Codex"
description: "Codex skill for a Laravel security review. Use when you want that security review on a Laravel change. Do not use it for a different stack."
type: "skill"
tools:
  - "codex"
stack: "laravel"
tags:
  - "laravel"
  - "php"
  - "eloquent"
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
  - "laravel@13"
updated_for: "Laravel 13, Nov 2026"
---

# Laravel Security Review Skill for Codex

## Install

Install the native export at `.agents/skills/laravel-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Laravel Security Review Skill for Codex

Codex skill `laravel-security-review` for Laravel. Call it with `$laravel-security-review` or `/skills`. Do not install the other tools' copies beside it.

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
