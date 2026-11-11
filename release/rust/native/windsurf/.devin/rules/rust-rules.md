---
description: "Rust standards for Ownership, Errors and Async. Use when editing this stack. Rust 1.99 stable line, Nov 2026."
trigger: "model_decision"
---

# Rust Windsurf Rules: Ownership, Errors and Async

Rule for Rust on current Devin (`.devin/rules`) and legacy Cascade (`.windsurf/rules`). The trigger is model decision. Use `rust-code-review` for a review.

## Updated for Rust 1.99, Nov 2026

Stay on the rust-toolchain and the MSRV in `Cargo.toml`. The 1.99 stable line adds C-ABI variadics and raw-pointer layout APIs. Those are for FFI and layout code, not a reason to rewrite safe Rust. Do not raise the MSRV, and do not depend on a 1.100 feature that is not in the toolchain. Read `Cargo.toml` before you add a crate.

## Project shape

A library crate returns `Result`. A binary's `main` decides how to exit. Modules follow the existing tree. `unsafe` lives in the smallest block that needs it, with a comment that states the invariant. Do not use `unsafe` to avoid the borrow checker.

Prefer borrowing. Clone when the ownership story is actually a copy, and say why if the clone is on a hot path.

## Errors

Library code does not `unwrap` or `expect` on a path a caller can trigger. `expect` is for a bug in the program, with a message that explains the broken invariant. Use the project's error type. `?` propagates. A `match` that drops the error and returns a default hides a failure.

## Async

An async function is cancel-safe at its await points, or it documents that it is not. Do not hold a lock across an `.await`. A spawned task has a join handle or a structured scope. Blocking work does not run on the async runtime. Use the project's `spawn_blocking` helper.

A timeout cancels the inner work. Dropping a future should release the resources it holds.

## FFI, security, and tests

A new `unsafe` or a C-ABI variadic is reviewed as FFI. Pointer layout APIs are not a shortcut around lifetimes. Input from the network is validated before it becomes a length or an index.

Tests live next to the code or in `tests/` as the crate already does. Cover the error variant, not only the happy path. Run `cargo test` for the package. Record the output. `cargo clippy` follows the project's lints.

## Mistakes to avoid

- `unwrap` on input or I/O.
- `unsafe` to silence the borrow checker.
- A lock held across `.await`.
- A blocking call on the async executor.
- An MSRV bump hidden in an unrelated change.
