---
id: "cursor-rust-code-review"
slug: "cursor/rust/rust-code-review/SKILL"
title: "Rust Code Review Skill for Cursor"
description: "Review a Rust change for unwrap on library paths, needless unsafe, and async cancellation. Use for a Rust code review. Do not use for a non-Rust repository or to raise the MSRV without a reason."
type: "skill"
tools:
  - "cursor"
stack: "rust"
tags:
  - "rust"
  - "ownership"
  - "async"
  - "code-review"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Cursor docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "rust@1.100"
updated_for: "Rust 1.100.0, Nov 2026"
---

# Rust Code Review Skill for Cursor

## Install

Install the native export at `.cursor/skills/rust-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# Rust Code Review Skill for Cursor

Cursor skill `rust-code-review` for Rust. Run it with `/rust-code-review`, or let Agent select it when the request matches. `paths` only limits automatic surfacing.

## When to run

Run this review for a Rust change: a public function, an async task, or a new `unsafe` block.

## When to leave it

Stop for a non-Rust repository. Do not bump the MSRV or the toolchain unless the user asked.

## Steps

1. Read the MSRV and the toolchain file. A feature from a newer Rust used without a bump, or a silent MSRV bump, is a high finding.
2. Search the diff for `unwrap`, `expect`, and `unsafe`. `unwrap` on I/O or parsed input is a high finding. `unsafe` without an invariant comment is a high finding.
3. Search for `.await` while a `std::sync::Mutex` or `parking_lot` guard is in scope, and for `std::thread::sleep` or blocking I/O inside an async function. Each is a high finding. A `tokio::sync::Mutex` held across `.await` is valid. Do not flag it.
4. Check that a spawned task can finish when the parent is canceled.
5. Run `cargo test` for the package only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the panic or safety hole, and a `Result`-based or safe alternative.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: an async function holds `std::sync::Mutex` across `.await`.
Output: high | src/worker.rs:31 | a std mutex guard must not be held across `.await` | drop the guard first, or use `tokio::sync::Mutex` when the guard must span the await.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to `allow` a clippy lint project-wide or to `unwrap` so the example is shorter.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
