# presets.dev

This repository is the central hub for community-contributed data that powers [presets.dev](https://presets.dev). It provides high-quality, specialized configurations designed to extend and customize the capabilities of GitHub Copilot for specific development workflows.

## Data Organization

We use a **technology-first** flat structure. This ensures that all presets related to a specific language, framework, or tool are easily discoverable within their own dedicated directory.

```
.
├── react/                  # React-specific agents and instructions
├── nextjs/                 # Next.js-specific presets
├── python/                 # Python-specific workflows
└── ...
```

## Types of Presets

Totaling three distinct resource types, these presets allow for granular control over the GitHub Copilot experience:

1. **Agents** (`.agent.md`): Deeply configured chat personas that transform GitHub Copilot into a domain-specific expert or project assistant.
2. **Instructions** (`.instructions.md`): Custom rules and coding guidelines that ensure GitHub Copilot adheres to your project's specific conventions and best practices.
3. **Skills** (`/skill-folder/SKILL.md`): Reusable capabilities and automated workflows that allow GitHub Copilot to interact with external tools and processes.

## Contributing

We welcome community contributions to help expand the reach of specialized AI assistance. To add your own presets:

1. **Review the [Contributing Guide](CONTRIBUTING.md)** for detailed formatting and quality standards.
2. **Select a Technology Folder**: Locate the relevant directory or create a new one to house your preset.
3. **Submit a Pull Request**: Once approved, your contribution will be indexed and showcased on [presets.dev](https://presets.dev).

---
*Empowering developers through community-driven AI configurations.*

