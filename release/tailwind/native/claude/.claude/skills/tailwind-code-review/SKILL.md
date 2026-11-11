---
name: "tailwind-code-review"
description: "Review a Tailwind change for version fit, detectable class names, and accessible layout. Use for a Tailwind code review. Do not use for a non-Tailwind repository or to convert a v3 project to v4 unasked."
---

# Tailwind CSS Code Review Skill for Claude Code

Claude Code skill `tailwind-code-review` for Tailwind CSS. The command is `/tailwind-code-review`. Leave the normal permission prompts on.

## When to run

Run this review for a Tailwind change: a new component, a theme edit, or "check the styles". Judge version fit, class detection, and accessibility.

## When to leave it

Stop when the project does not use Tailwind, or when the user asked for a v4 migration and you have not confirmed they want it. A v3 repo stays on v3.

## Steps

1. Read the installed `tailwindcss` major. Note v3 config versus v4 `@theme`. A mix of the two in one diff is a high finding.
2. Search the diff for class names built from variables or concatenated fragments. Each one that is not a complete static string is a finding.
3. Look for conflicting utilities on the same element, and for a one-off color that duplicates a token.
4. Check focus, labels on icon buttons, and error messages that are only a red class. Each gap is a finding.
5. Do not start a browser unless the user asked you to verify a screen. If you do, record the URL and the width.

## Output

Findings with severity, file, line, and the class or token to change. End with the Tailwind major and `no file edits` unless a fix was requested.

## Stop

Stop when the user asks you to upgrade v3 to v4 as part of an unrelated review.
