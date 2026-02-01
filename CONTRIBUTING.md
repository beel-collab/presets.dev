# Contributing to presets.dev

Thank you for your interest in contributing to presets.dev! We welcome contributions from the community to help expand our collection of GitHub Copilot agents, instructions, and prompts.

## How to Contribute

We welcome contributions directly to this repository!

> **Note:** You can also contribute to the official [awesome-copilot](https://github.com/github/awesome-copilot) repository. We periodically sync content from there. If you want your changes to appear faster or if they are specific to presets.dev, please contribute directly here.

### Adding Agents

Agents are chat mode configurations that transform GitHub Copilot into a domain-specific assistant.

1. **Create your agent file**: Add a new `.agent.md` file in the `src/data/copilot/agents/` directory
2. **Follow the naming convention**: Use descriptive, lowercase filenames with hyphens (e.g., `react-performance-expert.agent.md`)
3. **Include frontmatter**: Add metadata at the top of your file
4. **Test your agent**: Ensure the agent provides helpful, accurate responses in its domain

#### Example agent format

```markdown
---
description: "Brief description of the agent and its purpose"
tags: ["React", "TypeScript", "Performance"]
author:
  name: "Your Name"
  url: "https://github.com/yourusername"
  avatar: "https://github.com/yourusername.png"
---

# Agent Title

You are an expert [domain/role] with deep knowledge in [specific areas].

## Your Expertise

- Specific skill 1
- Specific skill 2
- Specific skill 3

## Your Approach

- How you help users
- Your communication style
- What you prioritize

## Guidelines

- Specific instructions for responses
- Constraints or limitations
- Best practices to follow
```

### Adding Instructions

Instructions help customize GitHub Copilot's behavior for specific technologies, coding practices, or domains.

1. **Create your instruction file**: Add a new `.instructions.md` file in the `src/data/copilot/instructions/` directory
2. **Follow the naming convention**: Use descriptive, lowercase filenames with hyphens (e.g., `python-django.instructions.md`)
3. **Structure your content**: Start with a clear heading and organize your instructions logically
4. **Test your instructions**: Make sure your instructions work well with GitHub Copilot

#### Example instruction format

```markdown
---
description: "Instructions for customizing GitHub Copilot behavior for specific technologies"
tags: ["Python", "Django", "Web Development"]
author:
  name: "Your Name"
  url: "https://github.com/yourusername"
---

# Technology/Framework Name

## Guidelines

- Provide clear, specific guidance for GitHub Copilot
- Include best practices and conventions
- Use bullet points for easy reading

## Code Style

- Formatting rules
- Naming conventions
- Project structure preferences

## Examples

Include code examples where helpful.
```

### Adding Prompts

Prompts are ready-to-use templates for specific development scenarios and tasks.

1. **Create your prompt file**: Add a new `.prompt.md` file in the `src/data/copilot/prompts/` directory
2. **Follow the naming convention**: Use descriptive, lowercase filenames with hyphens (e.g., `react-component-generator.prompt.md`)
3. **Include frontmatter**: Add metadata at the top of your file
4. **Structure your prompt**: Provide clear context and specific instructions

#### Example prompt format

```markdown
---
description: "Brief description of what this prompt does"
tags: ["React", "Components", "TypeScript"]
author:
  name: "Your Name"
  url: "https://github.com/yourusername"
---

# Prompt Title

Your goal is to...

## Specific Instructions

- Clear, actionable instructions
- Include examples where helpful
- Define expected output format
```

### Adding Skills

Skills are capabilities that allow GitHub Copilot to perform specific tasks, often contacting external services or managing complex workflows.

1. **Create your skill directory**: Create a new directory in `src/data/copilot/skills/` with your skill name (e.g., `github-issues`).
2. **Add SKILL.md**: Create a `SKILL.md` file inside that directory. This is the main entry point.
3. **Include frontmatter**: Add metadata at the top of `SKILL.md`.
4. **Include references**: If your skill needs extra templates or scripts, put them in a `references/` subdirectory.

#### Example skill format (`src/data/copilot/skills/my-skill/SKILL.md`)

```markdown
---
description: "Description of what this skill allows Copilot to do"
tags: ["GitHub", "Issues", "Workflow"]
author:
  name: "Your Name"
  url: "https://github.com/yourusername"
---

# Skill Name

## Description

Detailed description of the skill.

## Available Tools

| Tool | Purpose |
|------|---------|
| `tool_name` | What it does |
```


## Submitting Your Contribution

1. **Fork this repository** at [github.com/beel-collab/presets.dev](https://github.com/beel-collab/presets.dev)
2. **Create a new branch** for your contribution:
   ```bash
   git checkout -b add-my-agent-name
   ```
3. **Add your file** following the guidelines above
4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add [agent/instruction/prompt] for [technology]"
   ```
5. **Push to your fork**:
   ```bash
   git push origin add-my-agent-name
   ```
6. **Submit a pull request** with:
   - A clear title describing your contribution
   - A brief description of what your agent/instruction/prompt does
   - Any relevant context or usage notes

## Required Frontmatter Fields

All contributions must include YAML frontmatter at the top of the file:

| Field | Required | Description |
|-------|----------|-------------|
| `description` | ✅ Yes | Brief description of what this does |
| `tags` | ✅ Yes | Array of relevant tags for filtering |
| `author.name` | ❌ Optional | Your name or username |
| `author.url` | ❌ Optional | Link to your profile |
| `author.avatar` | ❌ Optional | URL to your avatar image |
| `libs` | ❌ Optional | Array of related libraries |

## What We Accept

We welcome contributions covering any technology, framework, or development practice that helps developers work more effectively with GitHub Copilot:

- 💻 Programming languages and frameworks
- 🏗️ Architecture patterns and design principles
- 🧪 Testing strategies and quality assurance
- 🚀 DevOps and deployment practices
- ♿ Accessibility and inclusive design
- ⚡ Performance optimization techniques
- 🔒 Security best practices

## What We Don't Accept

To maintain a safe, responsible, and constructive community, we will **not accept** contributions that:

- ❌ Violate Responsible AI Principles
- ❌ Compromise security or enable malicious activities
- ❌ Exploit vulnerabilities in platforms or services
- ❌ Promote harmful, discriminatory, or inappropriate content
- ❌ Circumvent platform terms of service

## Quality Guidelines

- **Be specific**: Generic instructions are less helpful than specific, actionable guidance
- **Test your content**: Ensure your instructions or prompts work well with GitHub Copilot
- **Follow conventions**: Use consistent formatting and naming
- **Keep it focused**: Each file should address a specific technology, framework, or use case
- **Write clearly**: Use simple, direct language
- **Promote best practices**: Encourage secure, maintainable, and ethical development

## Tags Reference

Use these common tags to help users find your contribution:

**Frameworks**: `Next.js`, `React`, `Vue`, `Angular`, `Svelte`, `Django`, `FastAPI`, `Rails`, `Laravel`

**Languages**: `TypeScript`, `JavaScript`, `Python`, `Go`, `Rust`, `Java`, `C#`, `Ruby`, `PHP`

**Tools**: `Tailwind CSS`, `Prisma`, `Docker`, `Terraform`, `AWS`, `Azure`, `GCP`

**Categories**: `Testing`, `Security`, `Performance`, `Accessibility`, `Documentation`, `DevOps`

## Questions or Suggestions?

If you have questions about contributing or suggestions for improving the contribution process, please [open an issue](https://github.com/beel-collab/presets.dev/issues/new).

## License

By contributing to this repository, you agree that your contributions will be licensed under the MIT License.
