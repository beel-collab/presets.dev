# Next.js Cline Skill for a Tenant Cache Audit

A Cline skill that loads when a request matches its description, or when you run `/nextjs-tenant-cache-audit`. Rules stay in context. This skill does not. A sampled Cline autocomplete prefix for Next.js returned nothing relevant, so a "cline skills nextjs" keyword is a hypothesis, not a measured phrase.

## Install

The recommended project path is `.cline/skills/nextjs-tenant-cache-audit/SKILL.md`. `.clinerules/skills/` also works. Pick one. `name` matches the folder exactly. `description` is under the 1,024 character limit and includes the non-trigger, because a vague description is how Cline misses the skill or loads it for a CSS edit.

A global skill with the same name overrides the project skill. That is the opposite of Cline's rule precedence. If `/nextjs-tenant-cache-audit` runs the wrong text, look in `~/.cline/skills/` and the Documents Cline skills folder before editing the project file.

The skill can be toggled off in the Skills tab without deleting the folder. Leave it on for Next.js repos and off for other checkouts if you installed it globally by mistake. This release installs it as a project skill.

## What was checked

Cline's skills document was read on 11 November 2026, including slash invocation and the global-over-project rule. Cline was not opened. The decision table was run with the Node fixture only.
