# Native install map

Generated from `masters/*/stack.json`. Install the native file, not the catalog source.
Catalog frontmatter is presets.dev metadata.

Windsurf ships the same text to `.devin/` (current Devin) and `.windsurf/` (legacy Cascade).
Codex and Gemini CLI standards are sections to append. Do not replace `AGENTS.md` or `GEMINI.md`.
Install one skill per checkout. Shared `.agents/skills` names collide across Cursor, Codex, and Gemini CLI.

| Stack | Tool | Role | Catalog | Install |
| --- | --- | --- | --- | --- |
| nextjs | cursor | standards | `cursor/nextjs/nextjs-rules.mdc` | `release/nextjs/native/cursor/.cursor/rules/nextjs-rules.mdc` |
| nextjs | cursor | skill | `cursor/nextjs/nextjs-code-review/SKILL.md` | `release/nextjs/native/cursor/.cursor/skills/nextjs-code-review/SKILL.md` |
| nextjs | copilot | standards | `copilot/nextjs/nextjs-rules.instructions.md` | `release/nextjs/native/copilot/.github/instructions/nextjs.instructions.md` |
| nextjs | copilot | skill | `copilot/nextjs/nextjs-code-review/SKILL.md` | `release/nextjs/native/copilot/.github/skills/nextjs-code-review/SKILL.md` |
| nextjs | claude | standards | `claude/nextjs/nextjs-rules.md` | `release/nextjs/native/claude/.claude/rules/nextjs-rules.md` |
| nextjs | claude | skill | `claude/skills/nextjs/nextjs-code-review/SKILL.md` | `release/nextjs/native/claude/.claude/skills/nextjs-code-review/SKILL.md` |
| nextjs | windsurf | standards | `windsurf/nextjs/nextjs-rules.md` | `release/nextjs/native/windsurf/.devin/rules/nextjs-rules.md` |
| nextjs | windsurf | standards | `windsurf/nextjs/nextjs-rules.md` | `release/nextjs/native/windsurf/.windsurf/rules/nextjs-rules.md` |
| nextjs | windsurf | skill | `windsurf/nextjs/nextjs-code-review/SKILL.md` | `release/nextjs/native/windsurf/.devin/skills/nextjs-code-review/SKILL.md` |
| nextjs | windsurf | skill | `windsurf/nextjs/nextjs-code-review/SKILL.md` | `release/nextjs/native/windsurf/.windsurf/skills/nextjs-code-review/SKILL.md` |
| nextjs | cline | standards | `cline/nextjs/nextjs-rules.md` | `release/nextjs/native/cline/.clinerules/nextjs-rules.md` |
| nextjs | cline | skill | `cline/nextjs/nextjs-code-review/SKILL.md` | `release/nextjs/native/cline/.cline/skills/nextjs-code-review/SKILL.md` |
| nextjs | codex | standards | `codex/nextjs/nextjs-rules.md` | `release/nextjs/native/codex/AGENTS.nextjs-section.md` |
| nextjs | codex | skill | `codex/nextjs/nextjs-code-review/SKILL.md` | `release/nextjs/native/codex/.agents/skills/nextjs-code-review/SKILL.md` |
| nextjs | gemini-cli | standards | `gemini-cli/nextjs/nextjs-rules.md` | `release/nextjs/native/gemini-cli/GEMINI.nextjs-section.md` |
| nextjs | gemini-cli | skill | `gemini-cli/nextjs/nextjs-code-review/SKILL.md` | `release/nextjs/native/gemini-cli/.gemini/skills/nextjs-code-review/SKILL.md` |
