---
name: "angular-code-review"
description: "Review an Angular change for standalone components, signals, zoneless updates, and Signal Forms. Use for an Angular code review. Do not use for a new NgModule-first app or a non-Angular repository."
paths:
  - "**/*.ts"
  - "**/*.html"
---

# Angular Code Review Skill for Cursor

Cursor skill `angular-code-review` for Angular. Run it with `/angular-code-review`, or let Agent select it when the request matches. `paths` only limits automatic surfacing.

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
Input: a one-line change that matches a rule in the standards.
Output: either one finding with file and line, or "No findings" when the change is the valid pattern named in the standards.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to turn Zone back on globally to match a blog post.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
