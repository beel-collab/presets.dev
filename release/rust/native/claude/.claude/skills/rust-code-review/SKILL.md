---
name: "rust-code-review"
description: "Review a Rust change for unwrap on library paths, needless unsafe, and async cancellation. Use for a Rust code review. Do not use for a non-Rust repository or to raise the MSRV without a reason."
---

# Rust Code Review Skill for Claude Code

Claude Code skill `rust-code-review` for Rust. The command is `/rust-code-review`. Leave the normal permission prompts on.

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

## Stop

Stop when the user asks you to `allow` a clippy lint project-wide or to `unwrap` so the example is shorter.
