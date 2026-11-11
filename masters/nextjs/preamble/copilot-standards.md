# Next.js Copilot Instructions for Server Actions and Caching

Path-specific Copilot instructions for Next.js. The searchable job is "copilot instructions nextjs": validated Server Actions and tenant-safe caching on the App Router.

## Install

Place the native export at `.github/instructions/nextjs-app-router-caching.instructions.md`. The native frontmatter is only `applyTo`. That glob list is `app` and `src/app` TypeScript files plus the Next config, comma-separated, which is the form in GitHub's path-specific instructions guide. Do not paste this catalog frontmatter into that file.

Leave `.github/copilot-instructions.md` in place. Repository-wide instructions and path-specific instructions are combined when both match. This file is the path-specific layer so Next.js cache rules are not injected into unrelated languages.

On GitHub.com, path-specific instructions are documented for the cloud agent and for code review. IDE support is a separate matrix. A pass in one Copilot surface does not prove the others. This preset was not run in any Copilot surface.

`AGENTS.md` is a different Copilot feature (agent instructions). This standards entry is the `.instructions.md` file.

## What was checked

The `applyTo` shape was compared with GitHub's repository custom-instructions guide on 11 November 2026. Copilot was not opened. The decision table was run with the Node fixture named in the instruction text.
