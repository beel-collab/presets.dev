---
id: "claude-angular-rules"
slug: "claude/angular/angular-rules"
title: "Angular Claude Code Rules: Standalone Components, Signals and Forms"
description: "Claude Code rules for Angular: Standalone Components, Signals and Forms. Structure, data, errors, security, performance, and tests. Angular 22.2.5, Nov 2026."
type: "rule"
tools:
  - "claude"
stack: "angular"
tags:
  - "angular"
  - "typescript"
  - "signals"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Claude Code docs 2026-11-11; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "@angular/core@22.2.5"
updated_for: "Angular 22.2.5, Nov 2026"
---

# Angular Claude Code Rules: Standalone Components, Signals and Forms

## Install

Install the native export at `.claude/rules/angular-rules.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Angular Claude Code Rules: Standalone Components, Signals and Forms

Path-scoped Claude Code rule for Angular. It loads when a matching file is read. It does not replace `CLAUDE.md`. Use `angular-code-review` for a review.

## Updated for Angular 22.2.5, Nov 2026

`@angular/core` 22.2.5 is the npm `latest` release checked on 11 November 2026. Signal Forms are stable in v22. Zoneless change detection has been the default since v21. Read the installed major before you generate a component. Do not scaffold a new NgModule-first app. Do not add `zone.js` back because an old example imported it.

## Project shape

New components are standalone. They declare `imports` for the directives they use. A feature is a set of standalone components and a route, not a new module, unless the repository is still on the module style and the task did not ask to convert it.

Routes are lazy where the app already lazy-loads. Provide services at the route or the root the project already chose. Do not provide the same stateful service in every component.

## Signals and templates

Own state in a `signal`. Derive with `computed`. Use `input()` and `output()` on a new component when the project is on a version that has them. An `effect` is for a side effect, and it must not write a signal that retriggers itself. If the effect loops, move the value into a `computed`.

The template calls signals as functions. Do not read a signal once in the constructor and cache the plain value for the life of the component.

## Forms

On v22, a new form uses Signal Forms when the project has already adopted them. Follow the existing form helper if the app has not migrated. Do not mix a new Signal Form and a legacy `FormGroup` in the same form.

Validate at the form boundary. Show the message next to the control. A submit handler does not trust the raw value without reading the form's validity.

## Zoneless updates

Async work that should refresh the view updates a signal or uses the project's change-detection API. Do not call `detectChanges` in a loop. A third-party widget that mutates the DOM outside Angular needs the bridge the project already uses, not a new `NgZone` wrapper copied from a v12 post.

## Errors, security, and tests

Use the HTTP interceptor and error handler the app already has. Map a failed request to a signal the template can show. Do not swallow it.

Bind user content as text. `innerHTML` and `bypassSecurityTrust*` need a documented sanitizer and a review. Do not trust a URL from the query string into a redirect.

Test with the project's TestBed or the newer test API it already uses. A component test sets the input, detects the view the way the suite does, and asserts the text. Cover an invalid form and a failed HTTP call when you add them.

## Mistakes to avoid

- A new app generated as NgModules because the snippet was old.
- An effect that writes a signal and retriggers itself.
- `zone.js` added back to silence a stale example.
- A form value submitted while invalid.
- `bypassSecurityTrustHtml` on a user string.
