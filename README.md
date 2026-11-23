# presets.dev

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/beel-collab/presets.dev/actions/workflows/ci.yml/badge.svg)](https://github.com/beel-collab/presets.dev/actions/workflows/ci.yml)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

presets.dev is a public catalog of AI coding presets. A preset is a rule, instruction, agent, or skill that shapes an assistant while you write software. The catalog covers GitHub Copilot, Cursor, Claude Code, Windsurf, Cline, OpenAI Codex, and Antigravity CLI. Antigravity CLI replaced Gemini CLI for personal accounts and uses the `antigravity` id.

This repository is the content source for [presets.dev](https://presets.dev). A file under a tool directory is a preset.

## Install

Install a stack from your project directory with the [`presets-dev`](https://www.npmjs.com/package/presets-dev) CLI (Node.js 22+):

```bash
npx presets-dev list
npx presets-dev add nextjs --tool cursor
npx presets-dev add nextjs typescript --tool claude,codex --dry-run
```

The CLI reads `release/original-2026-11/stacks.json` from this repository and writes each tool's native files. Contributed rules, instructions, and skills are installable by their preset IDs. Without `--tool`, it detects tools from your project.

To install by hand, copy the native file into the path named in `release/README.md`. Append Codex sections to `AGENTS.md` and Antigravity CLI sections to `GEMINI.md`. Do not replace a file the repo already has. Windsurf installs only the `.devin/` copy.

## Originality

A preset is accepted when presets.dev or a named contributor wrote it.

Write it from your own testing and wording. A copy of another repository, a documentation site, or another preset collection is outside this project. That includes text under MIT, CC BY, and CC0.

The clean-room rule, the frontmatter schema, and the starters are in [CONTRIBUTING.md](CONTRIBUTING.md).

## Layout

| Folder | Tool | Filenames |
| --- | --- | --- |
| `copilot/` | GitHub Copilot | `.instructions.md`, `.agent.md`, `SKILL.md` |
| `cursor/` | Cursor | `.md`, `.mdc`, `AGENTS.md`, `SKILL.md` |
| `claude/` | Claude Code | `CLAUDE.md`, agents, `skills/<topic>/<name>/SKILL.md` |
| `windsurf/` | Windsurf | `.md`, `AGENTS.md`, `SKILL.md` |
| `cline/` | Cline | `.md`, `SKILL.md` |
| `codex/` | OpenAI Codex | `AGENTS.md`, `SKILL.md`, and standards files that install as an `AGENTS.md` section |
| `antigravity/` | Antigravity CLI | standards files that install as a `GEMINI.md` or `AGENTS.md` section, `SKILL.md` |

## Original release

`masters/` holds one standards file and one skill file for each of 30 stacks. `python scripts/assemble_release.py` writes 420 catalog entries (seven tools, two files each) and the native install files under `release/<stack>/native/`.

The install index at `release/original-2026-11/stacks.json` includes the original stacks and standalone contributions.

## Contributing

1. Read [CONTRIBUTING.md](CONTRIBUTING.md).
2. Copy a starter from [`templates/`](templates/).
3. Run the release assembler and include the generated install files and index.
4. Sign off every commit with `git commit -s`.
5. Open a pull request. The template asks you to confirm the preset is original.

## License

[MIT](LICENSE). Copyright (c) presets.dev and contributors.
