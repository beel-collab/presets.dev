# Next.js Cline Rules for Server Actions and Safe Caching

Cline rules for the Next.js App Router. A sampled "cline rules nextjs" autocomplete prefix did not return a relevant suggestion on 11 November 2026, so that phrase is an unverified hypothesis. The file still targets the same Next.js job as the rest of this stack: validated Server Actions and tenant-safe caching.

## Install

Put the native export in one directory only: `.clinerules/nextjs-app-router-caching.md`. Cline also reads `.cline/rules/`. Using both would load two copies. The VS Code rules panel creates workspace rules under `.clinerules/`, which is why that path is the one this release writes.

The native frontmatter is a `paths` list. An empty list never activates. YAML that does not parse fails open, and the raw frontmatter becomes part of the rule, so the export is checked before you install it. Workspace rules override a conflicting global rule. Toggle the file off in the Rules panel when you are not in the Next.js app.

`AGENTS.md` at the repo root is a different Cline input. This entry does not tell you to create one.

The audit procedure is the skill at `.cline/skills/nextjs-tenant-cache-audit/SKILL.md`. A same-named skill in the global skills directory wins over the project skill. Remove or rename the global copy if you expect this project file to run.

## What was checked

Cline's rules and skills documents were read on 11 November 2026, including the fail-open note for malformed conditional YAML. Cline was not opened. The decision table was run with the Node fixture named in the rule text.
