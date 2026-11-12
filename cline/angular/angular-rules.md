---
id: "cline-angular-rules"
slug: "cline/angular/angular-rules"
title: "Angular Cline Rules: Standalone Components, Signals and Forms"
description: "Cline rules for Angular: Standalone Components, Signals and Forms. Structure, data, errors, security, performance, and tests. Angular 22.2.6, Nov 2026."
type: "rule"
tools:
  - "cline"
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
  - "Cline docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "@angular/core@22.2.6"
updated_for: "Angular 22.2.6, Nov 2026"
---

# Angular Cline Rules: Standalone Components, Signals and Forms

## Install

Install the native export at `.clinerules/angular-rules.md` (do not also copy it to `.cline/rules/`).
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# Angular Cline Rules: Standalone Components, Signals and Forms

Conditional Cline rule for Angular. Install it under `.clinerules/` only.

## Updated for Angular 22.2.6, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

## Project shape

New components are standalone. They declare `imports` for the directives they use. Templates use `@if`, `@for`, and `@switch`. That control flow has been the standard since v17. It is not a v22 feature. On v22, `OnPush` is the default change detection. The old `Default` strategy is named `Eager`. Do not set `ChangeDetectionStrategy.Default` on a new component. A feature is a set of standalone components and a route, not a new module, unless the repository is still on the module style and the task did not ask to convert it.

A new service uses `@Service()` and `inject()`. That decorator does not support constructor injection. Keep `@Injectable` when you need a constructor, `useClass`, or a non-root scope. `injectAsync` is the async form of `inject()` when the project is on a version that exports it. Do not generate a constructor-injected `@Service`.

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
- `*ngIf` or `*ngFor` in a new template. Use `@if` and `@for`.
- Constructor injection on a new `@Service()`. Use `inject()`.

## What changed in this major

Angular 22 defaults to OnPush (`Eager` is the old Default). New services use `@Service()` and `inject()`. Signal Forms are stable.

## Deprecated APIs to never generate

`*ngIf`, `*ngFor`, and `*ngSwitch` were deprecated in Angular 20. Use `@if`, `@for`, and `@switch`. Do not inject `ComponentFactoryResolver` to build a component. Use `ViewContainerRef.createComponent`. That factory change is from v13. Angular 22 did not delete the resolver class.

## Commands

Run `ng test` or the workspace test target.

## Example

```ts
@Service()
export class Notes {
  private http = inject(HttpClient)
}
```
## Agent tooling

The Angular CLI MCP server is `npx @angular/cli mcp`. It can search docs, list projects, and run targets. See https://angular.dev/ai/mcp .
