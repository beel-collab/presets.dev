---
id: "cline-angular-code-review"
slug: "cline/angular/angular-code-review/SKILL"
title: "Angular Code Review Skill for Cline"
description: "Cline skill for a Angular code review. Use when you want that code review on a Angular change. Do not use it for a different stack."
type: "skill"
tools:
  - "cline"
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
  - "Cline docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "@angular/core@22.2.5"
updated_for: "Angular 22.2.5, Nov 2026"
---

# Angular Code Review Skill for Cline

## Install

Install the native export at `.cline/skills/angular-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Angular Code Review Skill for Cline

Cline skill `angular-code-review` for Angular. `/angular-code-review` forces it. A global skill of the same name overrides this project file.

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

## Stop

Stop when the user asks you to turn Zone back on globally to match a blog post.
