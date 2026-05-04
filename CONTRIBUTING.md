# Contributing to presets.dev

This repository contains all preset content for [presets.dev](https://presets.dev) — a community collection of rules, instructions, agents, and skills for AI coding tools.

## Repository structure

```
presets.dev/          ← this repo (content only)
├── copilot/          GitHub Copilot agents, instructions, skills
├── cursor/           Cursor rules, agents
├── claude/           Claude Code agents, instructions, skills
├── windsurf/         Windsurf rules, agents
├── cline/            Cline rules
├── codex/            Codex rules
└── antigravity/      Antigravity rules
```


---

## How to contribute

### 1. Fork and clone

```bash
git clone https://github.com/beel-collab/presets.dev.git
cd presets.dev
```

### 2. Find the right tool folder

Pick the tool your preset is for (`copilot`, `cursor`, `claude`, etc.) and navigate into it.

### 3. Find or create a technology directory

Each tool folder is organized by technology (e.g., `react/`, `python/`, `nextjs/`). Create one if it doesn't exist yet.

### 4. Add your file

#### Rules / Instructions (`.md` or `.mdc`)

```
cursor/python/my-rule.md
copilot/react/react-expert.instructions.md
windsurf/nextjs/my-rule.mdc
```

#### Agents (`.agent.md`)

```
cursor/typescript/typescript-expert.agent.md
copilot/devops/ci-cd-expert.agent.md
```

#### Skills (directory with `SKILL.md`)

```
claude/skills/python/my-skill/SKILL.md
claude/skills/python/my-skill/references/template.md
```

---

## File format

Every file must have YAML frontmatter:

```markdown
---
title: "Your Preset Title"
description: "What this preset does"
tags:
  - TypeScript
  - React
author:
  name: "Your Name"
  url: "https://github.com/yourusername"
---

# Your content here
```

| Field | Required | Notes |
|-------|----------|-------|
| `title` | Yes | Shown in the UI |
| `description` | Yes | Shown in the UI |
| `tags` | Yes | Used for filtering |
| `author.name` | No | Defaults to "Community" |
| `author.url` | No | Your GitHub profile |
| `libs` | No | Related libraries |
| `also_for` | No | Other tools this works with e.g. `["cursor", "cline"]` |

---

## Naming conventions

- Lowercase, hyphens only: `my-preset-name.md`
- No spaces, dots, `+`, `#`, or other special characters in filenames
- Be descriptive: `react-performance-optimization.md` not `rules.md`

---

## Submitting

1. Create a branch: `git checkout -b add-react-performance-preset`
2. Add your file
3. Commit: `git commit -m "Add React performance optimization rules for Cursor"`
4. Push and open a pull request

---

## What we accept

- Any technology, framework, or practice that helps developers
- Rules, instructions, agents, or skills for any supported tool
- Improvements to existing presets

## What we don't accept

- Content that violates responsible AI principles
- Security exploits or malicious instructions
- Discriminatory or harmful content
- Generic filler content with no real guidance

---

## Questions?

Open an issue on this repository.

## License

By contributing, you agree your work is licensed under the MIT License.
