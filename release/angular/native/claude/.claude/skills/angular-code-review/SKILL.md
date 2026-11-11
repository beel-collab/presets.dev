---
name: "angular-code-review"
description: "Review an Angular change for standalone components, signals, zoneless updates, and Signal Forms. Use for an Angular code review. Do not use for a new NgModule-first app or a non-Angular repository."
---

# Angular Code Review Skill for Claude Code

Claude Code skill `angular-code-review` for Angular. The command is `/angular-code-review`. Leave the normal permission prompts on.

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
