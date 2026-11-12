# Contributing to presets.dev

presets.dev publishes rules, instructions, agents, and skills for AI coding tools. This repository is the content behind the site.

## Clean-room originality

Write each preset in a clean room. Close other preset repositories, rule files, and documentation pages before you draft. Use your own structure, your own examples, and your own wording.

A paraphrase of someone else's preset is still a copy. Text taken from another repository, a docs site, a blog, or a preset collection is outside this project. MIT, CC BY, CC0, and public-domain terms do not make a copy acceptable here. Those texts stay in the project that published them.

You can check a library's official documentation for a fact, then describe the practice in your own words with an example you ran.

Presets.dev and the named author are the copyright holders of what you submit. The repository license is MIT, copyright presets.dev and contributors.

## Developer Certificate of Origin

Every commit needs a sign-off under the [Developer Certificate of Origin](https://developercertificate.org/):

```text
Signed-off-by: Your Name <you@example.com>
```

`git commit -s` adds the line from your Git author name and email. CI rejects a commit that is missing it.

## How to add a preset

1. Copy the starter for the type from [`templates/`](templates/).
2. Move it to the path in the layout table below.
3. Replace `id`, `slug`, `title`, `description`, `author`, `tools`, `tags`, and the body.
4. Set `tested_with` to the tool build you actually tried.
5. Open a pull request. The template has an originality checkbox. Tick it only when it is true.

## Repository layout

```text
copilot/        GitHub Copilot
cursor/         Cursor
claude/         Claude Code
windsurf/       Windsurf
cline/          Cline
codex/          OpenAI Codex
antigravity/    Antigravity CLI
```

`antigravity` is Antigravity CLI. Gemini CLI stopped serving personal accounts on 18 June 2026, and Antigravity CLI reads `GEMINI.md` and `AGENTS.md`. Workspace skills install once at `.agents/skills/<name>/SKILL.md`. Codex and Antigravity CLI share that file. Do not add a separate `gemini-cli` directory.

| Type | Where to put it |
| --- | --- |
| Rule | `<tool>/<topic>/<name>.md`, or `<name>.mdc` for a scoped Cursor rule |
| Instruction | `copilot/<topic>/<name>.instructions.md`, or `claude/instructions/<topic>/CLAUDE.md` |
| Agent | `copilot/<topic>/<name>.agent.md`, `<tool>/<topic>/AGENTS.md`, or `claude/agents/<topic>/<name>.md` |
| Skill | `<tool>/<topic>/<skill-name>/SKILL.md` |

Claude skills are the exception to that skill path. Put them at `claude/skills/<topic>/<skill-name>/SKILL.md`.

A skill file is a skill: `SKILL.md` with `type: skill`. Do not use a second instruction file as a stand-in for that slot.

Optional notes that support a skill live in `references/` next to `SKILL.md`. Those files are not separate catalog entries. Write them yourself. `assets/` and `scripts/` are the same kind of supporting file.

File names are lowercase, with hyphens. The filenames `SKILL.md`, `AGENTS.md`, and `CLAUDE.md` stay in that conventional case.

## Frontmatter

New presets, and any preset a pull request edits, start with YAML frontmatter that matches [`schema/preset.frontmatter.schema.json`](schema/preset.frontmatter.schema.json).

| Field | Value |
| --- | --- |
| `id` | Unique kebab-case id, 3 to 80 characters. Not a path. |
| `slug` | Repository path with the trailing `.md` or `.mdc` removed. |
| `title` | Short name shown to people. |
| `description` | One or two sentences, 20 to 400 characters. |
| `type` | `rule`, `instruction`, `agent`, or `skill`. |
| `tools` | One or more of `copilot`, `cursor`, `claude`, `windsurf`, `cline`, `codex`, `antigravity`. Include the directory the file lives in. `antigravity` is Antigravity CLI. |
| `tags` | One to twelve short tags. |
| `author` | Object. `name` is required and is the person or organization who wrote the preset (`Community` is rejected). `github` is optional: a GitHub username, or `https://github.com/<username>`. The site indexer reads `author.name`. |
| `license` | `MIT` |
| `origin` | `original` |
| `version` | Semver, such as `1.0.0`. |
| `tested_with` | A run you actually made. Either say the client was not run, name a fixture, or use `client: Cursor; version: 2.1.0; date: 2026-11-12; result: pass`. |
| `created` | `YYYY-MM-DD` |
| `updated` | `YYYY-MM-DD`, same day or later than `created`. |

`slug` examples:

| File | slug |
| --- | --- |
| `cursor/typescript/strict-rules.md` | `cursor/typescript/strict-rules` |
| `cursor/typescript/strict-rules.mdc` | `cursor/typescript/strict-rules` |
| `copilot/react/hooks.instructions.md` | `copilot/react/hooks.instructions` |
| `cursor/typescript/hooks/SKILL.md` | `cursor/typescript/hooks/SKILL` |

Filename and `type` stay in step: `SKILL.md` is `skill`, `AGENTS.md` and `*.agent.md` are `agent`, `CLAUDE.md` and `*.instructions.md` are `instruction`, `*.mdc` is `rule`.

Optional fields, when you need them:

| Field | Use |
| --- | --- |
| `globs`, `alwaysApply` | Scoped Cursor `.mdc` rules. |
| `libs` | Libraries the preset assumes. |
| `model` | A model hint for an agent. |
| `also_for` | Other tools the same text was tried on. |
| `stack` | Short kebab-case stack id, such as `nextjs`. |
| `updated_for` | The versions the preset was written against. Keep `version` as semver. |

Catalog frontmatter is for this repository. It is not the file a product loads. Cursor rules, Copilot instructions, Cline rules, and skill files each have their own small frontmatter. Rebuild that native file from the export map under `release/` instead of copying catalog keys such as `tools` or `author` into the install path. An `AGENTS.md` or `GEMINI.md` install target is still project guidance: do not set `type: agent` only because the install filename is `AGENTS.md`.

Files already in the tree are not failed for this schema until a pull request edits them. An edit has to bring that file up to the schema in the same pull request.

## Templates

Copy the file. The copies in `templates/` are what CI checks, and the same text is below so this guide stands alone. Change the frontmatter before you open the pull request. The starter ids are reserved.

### Rule

Path after you copy it: `<tool>/<topic>/<name>.md` or `.mdc`. Starter: [`templates/rule.md`](templates/rule.md).

```markdown
---
id: template-rule
slug: templates/rule
title: Rule preset starter
description: Starter for a rule preset. Say which language or framework it covers and what the assistant should change.
type: rule
tools:
  - cursor
tags:
  - starter
author:
  name: Your Name
  github: your-name
license: MIT
origin: original
version: 1.0.0
tested_with:
  - Cursor 2.1
created: 2026-11-11
updated: 2026-11-11
---

# Rule preset starter

Copy this file to `<tool>/<topic>/<name>.md` (Cursor and Windsurf rules) or `<tool>/<topic>/<name>.mdc` (scoped Cursor rules). Then replace `id`, `slug`, `author`, `tools`, and the body. The `slug` is the path with `.md` or `.mdc` removed.

For a scoped Cursor rule, add `globs` and `alwaysApply` to the frontmatter.

## When this applies

Name the files or the task this rule is for.

## Write this way

- State the behavior you want in a sentence the assistant can follow.
- Give one small example you wrote yourself.
- Name the case the assistant should leave alone.

## Avoid

- Pasted excerpts from framework docs or from another rules file.
- A long list of preferences that you have not tried in the tool under `tested_with`.
```

### Instruction

Path after you copy it: `copilot/<topic>/<name>.instructions.md` or `claude/instructions/<topic>/CLAUDE.md`. Starter: [`templates/instruction.md`](templates/instruction.md).

```markdown
---
id: template-instruction
slug: templates/instruction
title: Instruction preset starter
description: Starter for an instruction preset that sets how the assistant behaves in a repository.
type: instruction
tools:
  - copilot
tags:
  - starter
author:
  name: Your Name
  github: your-name
license: MIT
origin: original
version: 1.0.0
tested_with:
  - GitHub Copilot
created: 2026-11-11
updated: 2026-11-11
---

# Instruction preset starter

Copy this file to `copilot/<topic>/<name>.instructions.md`, or to `claude/instructions/<topic>/CLAUDE.md` for Claude Code. Update `slug` so it matches the new path with `.md` removed, and set `tools` to include that directory.

## Repository facts

List the commands, directories, and conventions the assistant needs. Write them from this repository, not from a generic guide.

## How to respond

- Read the files that the task touches before editing them.
- Keep a change limited to the request.
- Show the command you expect a person to run when a check exists.

## Stop and ask

Name the situations where the assistant should ask instead of guessing. Examples: a missing product decision, or a migration that deletes data.
```

### Agent

Starter: [`templates/agent.md`](templates/agent.md).

| Tool | Path |
| --- | --- |
| GitHub Copilot | `copilot/<topic>/<name>.agent.md` |
| Cursor, Windsurf, Codex, Antigravity | `<tool>/<topic>/AGENTS.md` |
| Claude Code | `claude/agents/<topic>/<name>.md` |

```markdown
---
id: template-agent
slug: templates/agent
title: Agent preset starter
description: Starter for an agent preset with a single job, a boundary, and a way to check its work.
type: agent
tools:
  - claude
tags:
  - starter
author:
  name: Your Name
  github: your-name
license: MIT
origin: original
version: 1.0.0
tested_with:
  - Claude Code
created: 2026-11-11
updated: 2026-11-11
---

# Agent preset starter

Copy this file to the path your tool expects:

| Tool | Path |
| --- | --- |
| GitHub Copilot | `copilot/<topic>/<name>.agent.md` |
| Cursor, Windsurf, Codex, Antigravity | `<tool>/<topic>/AGENTS.md` |
| Claude Code | `claude/agents/<topic>/<name>.md` |

Set `type: agent`. Set `slug` to that path with `.md` removed.

## Job

One sentence: who the agent helps and what it produces.

## Boundary

What this agent leaves to someone else. An agent that tries to do every job is harder to test.

## Steps

1. Restate the task in one sentence.
2. Inspect the files that the task depends on.
3. Make the change.
4. Run the check named in `tested_with` and report the result.

## Voice

Short, specific, and willing to say when the task is out of scope.
```

### Skill

Starter: [`templates/skill/SKILL.md`](templates/skill/SKILL.md). Copy the directory to `<tool>/<topic>/<skill-name>/SKILL.md`. Claude skills go to `claude/skills/<topic>/<skill-name>/SKILL.md`.

```markdown
---
id: template-skill
slug: templates/skill/SKILL
title: Skill preset starter
description: Starter for a skill preset. Describe the request that should trigger it and the steps it runs.
type: skill
tools:
  - cursor
tags:
  - starter
author:
  name: Your Name
  github: your-name
license: MIT
origin: original
version: 1.0.0
tested_with:
  - Cursor 2.1
created: 2026-11-11
updated: 2026-11-11
---

# Skill preset starter

Copy this directory to `<tool>/<topic>/<skill-name>/SKILL.md`. Claude skills go under `claude/skills/<topic>/<skill-name>/SKILL.md`. The filename stays `SKILL.md`. Set `slug` to the directory path plus `/SKILL`.

Supporting notes belong in `references/` next to this file. Those files are not separate catalog presets. Write them yourself too.

## Use this skill when

Name the request, in the user's words, that should trigger the skill. Name one nearby request that should not.

## Steps

1. Confirm the inputs (paths, names, flags) are present.
2. Do the work in the order below. Keep each step to one action.
3. Stop if a step fails and report the command output.
4. Summarize what changed and how you checked it.

## Example

Write a short before-and-after that you produced by running the skill. Replace this paragraph.

## Limits

Record the tool version you tried and anything the skill will not do.
```

## What CI checks

GitHub Actions runs [`.github/workflows/ci.yml`](.github/workflows/ci.yml) on pull requests and on pushes to `main`.

| Check | Scope |
| --- | --- |
| Frontmatter schema | Preset files added or modified in the pull request, plus the starters in `templates/`. Other existing files are left alone. |
| `id` and `slug` uniqueness | The whole repository. A new id that repeats an existing one fails. Two untouched legacy files that happen to share an id do not fail the build. |
| Markdown lint | Markdown added or modified in the pull request. |
| Length | 40,000 characters for a changed preset or supporting file under a tool directory. `README.md` and `CONTRIBUTING.md` are exempt. |
| Secret scan | Files added or modified in the pull request. Private keys and common live token shapes fail the check. A line that is clearly an example is ignored. |
| DCO | Every non-merge commit in the pull request has `Signed-off-by` matching the commit author. |
| Release counts | Each stack listed as complete in `release/original-2026-11/stacks.json` has 14 catalog entries: one standards file and one `SKILL.md` for each of the seven release tools, including `antigravity`. The index is not named `manifest.json` because that filename is gitignored. |
| Native export | `scripts/assemble_release.py --check` rebuilds catalog files and native install files from `masters/` and fails on drift. |
| Similarity | Release prose is compared with the copied catalog. A long shared run, or a very high shingle overlap, fails the check. |
| Next.js fixture | `node --test fixtures/nextjs/tenant-cache/policy.test.mjs` runs the decision table used by the Next.js audit skill. |

Markdown rules in force: no trailing whitespace (MD009), no hard tabs (MD010), no stacked blank lines (MD012), a space after `#` in headings (MD018), fenced code blocks closed, and a single trailing newline (MD047). Use Unix line endings.

Install the same checker locally with `pip install -r requirements-ci.txt`, then run:

```text
python scripts/lint_presets.py
python scripts/check_dco.py
python scripts/assemble_release.py --check
python scripts/check_release_counts.py
python scripts/check_similarity.py
node --test fixtures/nextjs/tenant-cache/policy.test.mjs
```

## Pull requests

The pull request template is [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md). It includes an originality checkbox. Leave that box unchecked when the change is docs only, and say so in the summary.

## Issues

| Template | Use |
| --- | --- |
| New preset | Propose an original preset. Originality is a required checkbox. |
| Bug | A preset or a doc behaves incorrectly. |

## Labels

Create these labels in the GitHub repository. The names, colors, and descriptions are in [`.github/labels.yml`](.github/labels.yml).

| Label | When to use it |
| --- | --- |
| `preset` | A new or updated preset. |
| `rule` | The preset type is rule. |
| `instruction` | The preset type is instruction. |
| `agent` | The preset type is agent. |
| `skill` | The preset type is skill. |
| `bug` | A preset or doc behaves incorrectly. |
| `originality` | A question about whether content is original. |
| `documentation` | Docs, templates, schema, or CI only. |
| `needs-review` | A maintainer review is requested. |

Issue templates already request `preset`, `needs-review`, and `bug`. Those labels have to exist on the repository before GitHub will attach them.

## Code owners

[`.github/CODEOWNERS`](.github/CODEOWNERS) requests a review from `@beel-collab` for every pull request.

## Conduct

Submit presets you would run on your own repository. Instructions that ship exploits, malware, or attacks on people are rejected.
