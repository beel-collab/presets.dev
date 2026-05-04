# Contributing to presets.dev

This repository contains all preset content for [presets.dev](https://presets.dev) — a community collection of rules, instructions, agents, and skills for AI coding tools.

## Repository structure

```
presets.dev/
├── copilot/      GitHub Copilot — agents (.agent.md), instructions (.instructions.md), skills
├── cursor/       Cursor — rules (.md / .mdc), agents (AGENTS.md), skills
├── claude/       Claude Code — agents (.md), instructions (CLAUDE.md), skills
├── windsurf/     Windsurf — rules (.md), agents (AGENTS.md), skills
├── cline/        Cline — rules (.md), skills
├── codex/        OpenAI Codex — rules (AGENTS.md), skills
└── antigravity/  Antigravity — rules (AGENTS.md), skills
```

---

## Skills (all tools)

Skills are the same format for every tool — a named directory containing a `SKILL.md` file:

```
<tool>/<technology>/<skill-name>/SKILL.md
<tool>/<technology>/<skill-name>/references/   ← optional supporting files
```

Example:
```
copilot/github/create-issue/SKILL.md
cursor/typescript/refactor-to-composable/SKILL.md
claude/python/django-api-developer/SKILL.md
```

`SKILL.md` frontmatter:

```markdown
---
title: "Skill Name"
description: "What this skill does"
tags:
  - Python
  - Django
author:
  name: "Your Name"
  url: "https://github.com/yourusername"
---

# Skill Name

## Description
...
```

---

## File formats by tool

### GitHub Copilot

| Type | File format | Example |
|------|-------------|---------|
| Instructions | `name.instructions.md` | `react-expert.instructions.md` |
| Agents | `name.agent.md` | `ci-cd-expert.agent.md` |
| Skills | `skill-name/SKILL.md` | `create-issue/SKILL.md` |

```
copilot/react/react-expert.instructions.md
copilot/devops/ci-cd-expert.agent.md
copilot/github/create-issue/SKILL.md
```

---

### Cursor

| Type | File format | Example |
|------|-------------|---------|
| Rules | `name.md` or `name.mdc` | `typescript-rules.md` |
| Agents | `AGENTS.md` | `AGENTS.md` |
| Skills | `skill-name/SKILL.md` | `refactor-helper/SKILL.md` |

```
cursor/typescript/typescript-rules.md
cursor/python/AGENTS.md
cursor/typescript/refactor-helper/SKILL.md
```

> `.mdc` supports `globs` and `alwaysApply` frontmatter fields for scoped rules.

---

### Claude Code

| Type | File format | Example |
|------|-------------|---------|
| Instructions | `CLAUDE.md` or `name.md` | `CLAUDE.md` |
| Agents | `name.md` (in `agents/` subfolder) | `api-architect.md` |
| Skills | `skill-name/SKILL.md` | `django-api-developer/SKILL.md` |

```
claude/instructions/react/CLAUDE.md
claude/agents/ai-agents/api-architect.md
claude/skills/python/django-api-developer/SKILL.md
```

---

### Windsurf

| Type | File format | Example |
|------|-------------|---------|
| Rules | `name.md` | `nextjs-rules.md` |
| Agents | `AGENTS.md` | `AGENTS.md` |
| Skills | `skill-name/SKILL.md` | `deploy-helper/SKILL.md` |

```
windsurf/nextjs/nextjs-rules.md
windsurf/python/AGENTS.md
windsurf/devops/deploy-helper/SKILL.md
```

---

### Cline

| Type | File format | Example |
|------|-------------|---------|
| Rules | `name.md` | `react-rules.md` |
| Skills | `skill-name/SKILL.md` | `test-runner/SKILL.md` |

```
cline/react/react-rules.md
cline/testing/test-runner/SKILL.md
```

---

### OpenAI Codex

| Type | File format | Example |
|------|-------------|---------|
| Rules / Agents | `AGENTS.md` | `AGENTS.md` |
| Skills | `skill-name/SKILL.md` | `pr-reviewer/SKILL.md` |

```
codex/typescript/AGENTS.md
codex/github/pr-reviewer/SKILL.md
```

---

### Antigravity

| Type | File format | Example |
|------|-------------|---------|
| Rules / Agents | `AGENTS.md` | `AGENTS.md` |
| Skills | `skill-name/SKILL.md` | `code-reviewer/SKILL.md` |

```
antigravity/nextjs/AGENTS.md
antigravity/general/code-reviewer/SKILL.md
```

---

## Required frontmatter

All files must include YAML frontmatter:

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

# Content here
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

For `.mdc` (Cursor) files, additional frontmatter:

| Field | Notes |
|-------|-------|
| `globs` | File patterns this rule applies to e.g. `"**/*.ts"` |
| `alwaysApply` | `true` to always include this rule |

---

## Naming conventions

- Lowercase, hyphens only: `my-preset-name.md`
- No spaces, dots, `+`, `#`, or other special characters in filenames
- Be descriptive: `react-performance-optimization.md` not `rules.md`

---

## How to contribute

1. Fork this repository
2. Find or create the technology directory under the right tool folder
3. Add your file following the format for that tool (see above)
4. Create a branch: `git checkout -b add-react-performance-preset`
5. Commit: `git commit -m "Add React performance optimization rules for Cursor"`
6. Push and open a pull request

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

## License

By contributing, you agree your work is licensed under the MIT License.
