# Next.js Windsurf Rules for Server Actions and Safe Caching

Next.js standards for two different products that share a history. Legacy Cascade reads `.windsurf/rules/*.md`. Current Devin CLI reads `.devin/rules/*.md` and still loads `.windsurf/rules/*.md`. The native export ships both, with the same body, so the two files cannot give conflicting advice.

## Install

Devin is the preferred copy: `.devin/rules/nextjs-app-router-caching.md`. The legacy Cascade copy is `.windsurf/rules/nextjs-app-router-caching.md`. Frontmatter on both is `description` plus `trigger: model_decision`. Devin's rules document lists `always_on`, `manual`, `model_decision`, `agent`, and `glob`, and it shows `description` with `trigger`. It does not show a separate globs key, so this export does not invent one. `model_decision` asks the agent to pull the rule in when the description matches, instead of pinning it to every session.

Cascade's own rules page says workspace rules are tied to globs or to a natural-language description, and that each rule file is limited to 12,000 characters. The native body is checked against that limit. Cascade was not opened, and Devin CLI was not started.

Do not add an `AGENTS.md` for this entry. In Devin, `AGENTS.md` is always-on project guidance and a different mechanism. Do not invent a Windsurf agent profile.

The audit itself is the skill, installed for Devin at `.devin/skills/nextjs-tenant-cache-audit/SKILL.md` and for legacy layouts at `.windsurf/skills/nextjs-tenant-cache-audit/SKILL.md`.

## What was checked

Devin's rules document and the Cascade memories document were read on 11 November 2026. Neither client was executed. The decision table was run with the Node fixture named in the rule text.
