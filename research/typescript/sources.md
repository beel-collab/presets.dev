# TypeScript sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/typescript reports `latest` 7.0.2. `next` is a 7.1 dev build and is not the target.
- https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/ says TypeScript 7.0 is the native compiler and does not ship a programmatic API. Tooling that needs the API stays on TypeScript 6 through `@typescript/typescript6`. The team expects a different API in 7.1.
- https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/ says TypeScript 7 turns these deprecations into hard errors: `target: es5`, `downlevelIteration`, `moduleResolution: node/node10`, `moduleResolution: classic`, and `baseUrl`. Replacements are `es2015` or later, deleting `downlevelIteration`, `nodenext` or `bundler`, and `paths` relative to the project root.
