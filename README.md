# presets.dev

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/beel-collab/presets.dev/actions/workflows/ci.yml/badge.svg)](https://github.com/beel-collab/presets.dev/actions/workflows/ci.yml)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

presets.dev is a public catalog of AI coding presets. A preset is a rule, instruction, agent, or skill that shapes an assistant while you write software. The catalog covers GitHub Copilot, Cursor, Claude Code, Windsurf, Cline, OpenAI Codex, Gemini CLI, and Antigravity. Gemini CLI uses the `gemini-cli` id. Antigravity is a separate target.

This repository is the content source for [presets.dev](https://presets.dev). A file under a tool directory is a preset.

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
| `gemini-cli/` | Gemini CLI | standards files that install as a `GEMINI.md` section, `SKILL.md` |
| `antigravity/` | Antigravity | `AGENTS.md`, `SKILL.md` |

## Demo

<!-- Placeholder: add a short screen recording at docs/demo.gif. -->

![Demo of presets.dev](docs/demo.gif)

The recording is not in the repository yet. Put it at `docs/demo.gif` and the image above will show it.

## Contributing

1. Read [CONTRIBUTING.md](CONTRIBUTING.md).
2. Copy a starter from [`templates/`](templates/).
3. Sign off every commit with `git commit -s`.
4. Open a pull request. The template asks you to confirm the preset is original.

## License

[MIT](LICENSE). Copyright (c) presets.dev and contributors.
