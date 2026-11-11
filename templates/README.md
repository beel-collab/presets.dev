# Preset starters

These files are copy-paste starters for new presets. They are not published presets, and the ids are reserved for the starters.

| Type | File |
| --- | --- |
| Rule | [rule.md](rule.md) |
| Instruction | [instruction.md](instruction.md) |
| Agent | [agent.md](agent.md) |
| Skill | [skill/SKILL.md](skill/SKILL.md) |

Copy a starter into the tool directory, then change `id`, `slug`, `author`, `tools`, and the body. CI checks that these starters still match the frontmatter schema.

Gemini CLI presets live under `gemini-cli/`, not `antigravity/`. A task preset for the second catalog slot is a `SKILL.md` skill. Codex and Gemini CLI standards stay `type: rule` in this catalog when the installed file is an `AGENTS.md` or `GEMINI.md` section.
