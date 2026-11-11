# Next.js native install map

These files are generated from `masters/nextjs`. Install the native file, not the catalog source.
Catalog frontmatter is presets.dev metadata and is not valid product frontmatter.

Windsurf ships two copies of the same text: `.devin/` for current Devin CLI and `.windsurf/` for legacy Cascade.
Codex and Gemini CLI standards are sections to append. Do not overwrite an existing `AGENTS.md` or `GEMINI.md`.
Install one tool's skill. Do not place every tool's copy in `.agents/skills` under the same name.

| Tool | Role | Catalog source | Install file |
| --- | --- | --- | --- |
| cursor | standards | `cursor/nextjs/app-router-caching.mdc` | `release/nextjs/native/cursor/.cursor/rules/nextjs-app-router-caching.mdc` |
| copilot | standards | `copilot/nextjs/app-router-caching.instructions.md` | `release/nextjs/native/copilot/.github/instructions/nextjs-app-router-caching.instructions.md` |
| claude | standards | `claude/nextjs/app-router-caching.md` | `release/nextjs/native/claude/.claude/rules/nextjs-app-router-caching.md` |
| windsurf | standards | `windsurf/nextjs/app-router-caching.md` | `release/nextjs/native/windsurf/.devin/rules/nextjs-app-router-caching.md` |
| windsurf | standards | `windsurf/nextjs/app-router-caching.md` | `release/nextjs/native/windsurf/.windsurf/rules/nextjs-app-router-caching.md` |
| cline | standards | `cline/nextjs/app-router-caching.md` | `release/nextjs/native/cline/.clinerules/nextjs-app-router-caching.md` |
| codex | standards | `codex/nextjs/app-router-caching.md` | `release/nextjs/native/codex/AGENTS.nextjs-section.md` |
| gemini-cli | standards | `gemini-cli/nextjs/app-router-caching.md` | `release/nextjs/native/gemini-cli/GEMINI.nextjs-section.md` |
| cursor | skill | `cursor/nextjs/nextjs-tenant-cache-audit/SKILL.md` | `release/nextjs/native/cursor/.cursor/skills/nextjs-tenant-cache-audit/SKILL.md` |
| copilot | skill | `copilot/nextjs/nextjs-tenant-cache-audit/SKILL.md` | `release/nextjs/native/copilot/.github/skills/nextjs-tenant-cache-audit/SKILL.md` |
| claude | skill | `claude/skills/nextjs/nextjs-tenant-cache-audit/SKILL.md` | `release/nextjs/native/claude/.claude/skills/nextjs-tenant-cache-audit/SKILL.md` |
| windsurf | skill | `windsurf/nextjs/nextjs-tenant-cache-audit/SKILL.md` | `release/nextjs/native/windsurf/.devin/skills/nextjs-tenant-cache-audit/SKILL.md` |
| windsurf | skill | `windsurf/nextjs/nextjs-tenant-cache-audit/SKILL.md` | `release/nextjs/native/windsurf/.windsurf/skills/nextjs-tenant-cache-audit/SKILL.md` |
| cline | skill | `cline/nextjs/nextjs-tenant-cache-audit/SKILL.md` | `release/nextjs/native/cline/.cline/skills/nextjs-tenant-cache-audit/SKILL.md` |
| codex | skill | `codex/nextjs/nextjs-tenant-cache-audit/SKILL.md` | `release/nextjs/native/codex/.agents/skills/nextjs-tenant-cache-audit/SKILL.md` |
| gemini-cli | skill | `gemini-cli/nextjs/nextjs-tenant-cache-audit/SKILL.md` | `release/nextjs/native/gemini-cli/.gemini/skills/nextjs-tenant-cache-audit/SKILL.md` |
