---
id: "codex-angular-code-review"
slug: "codex/angular/angular-code-review/SKILL"
title: "Angular Code Review Skill for Codex"
description: "Review an Angular change for standalone components, signals, zoneless updates, and Signal Forms. Use for an Angular code review. Do not use for a new NgModule-first app or a non-Angular repository."
type: "skill"
tools:
  - "codex"
stack: "angular"
tags:
  - "angular"
  - "typescript"
  - "signals"
  - "code-review"
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
  - "@angular/core@22.2.6"
updated_for: "Angular 22.2.6, Nov 2026"
---

# Angular Code Review Skill for Codex

## Install

Install the native export at `.agents/skills/angular-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Angular Code Review Skill for Codex

Codex skill `angular-code-review` for Angular. Call it with `$angular-code-review` or `/skills`. Do not install the other tools' copies beside it.

## When to run

Run this review for an Angular change: a component, a form, a route, or "is this still the old style".

## When to leave it

Stop for a non-Angular repository. Do not upgrade Angular or delete NgModules the user did not name.

## Steps

1. Read the installed `@angular/core` major. A new NgModule, `NgModule` imports, or `zone.js` added on v21 or later is a high finding unless the file is existing legacy you were told to keep.
2. Review signals. An `effect` that writes another signal used by the same effect is a high finding. A template that reads a stale plain copy of a signal is a finding.
3. Review the form. Submitting an invalid form, or mixing Signal Forms with a `FormGroup` in one new form, is a finding.
4. Search for `bypassSecurityTrust` and `innerHTML`. Unsanitized user content is a high finding.
5. Note whether a test covers the new branch. Run the project's Angular test target only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the outdated or unsafe pattern, and the current replacement. Include the Angular version.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: a new Angular 22 service uses `@Service()` and `private http = inject(HttpClient)`.
Output: No findings. Constructor injection on a new `@Service()` is the finding.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to turn Zone back on globally to match a blog post.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
