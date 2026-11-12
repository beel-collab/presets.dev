## Updated for Rust 1.100.0, Nov 2026

Stay on the rust-toolchain and the MSRV in `Cargo.toml`. Rust 1.100.0 shipped on 12 November 2026 and stabilizes the never type and custom allocators. The 1.99 C-ABI variadics and raw-pointer layout APIs are already stable. Those FFI and layout APIs are not a reason to rewrite safe Rust. Do not raise the MSRV just because 1.100 exists. Read `Cargo.toml` before you add a crate.

## Project shape

A library crate returns `Result`. A binary's `main` decides how to exit. Modules follow the existing tree. `unsafe` lives in the smallest block that needs it, with a comment that states the invariant. Do not use `unsafe` to avoid the borrow checker.

Prefer borrowing. Clone when the ownership story is actually a copy, and say why if the clone is on a hot path.

## Errors

Library code does not `unwrap` or `expect` on a path a caller can trigger. `expect` is for a bug in the program, with a message that explains the broken invariant. Use the project's error type. `?` propagates. A `match` that drops the error and returns a default hides a failure.

## Async

An async function is cancel-safe at its await points, or it documents that it is not. Do not hold a `std::sync::Mutex` or a `parking_lot` guard across an `.await`. Those guards are not cancel-safe and can poison or stall the runtime. `tokio::sync::Mutex` is the lock you may hold across `.await`. A spawned task has a join handle or a structured scope. Blocking work does not run on the async runtime. Use the project's `spawn_blocking` helper.

A timeout cancels the inner work. Dropping a future should release the resources it holds.

## FFI, security, and tests

A new `unsafe` or a C-ABI variadic is reviewed as FFI. Pointer layout APIs are not a shortcut around lifetimes. Input from the network is validated before it becomes a length or an index.

Tests live next to the code or in `tests/` as the crate already does. Cover the error variant, not only the happy path. Run `cargo test` for the package. Record the output. `cargo clippy` follows the project's lints.

## Mistakes to avoid

- `unwrap` on input or I/O.
- `unsafe` to silence the borrow checker.
- A `std::sync::Mutex` or `parking_lot` guard held across `.await`.
- A blocking call on the async executor.
- An MSRV bump hidden in an unrelated change.

## What changed in this major

Rust 1.100 stabilizes the never type and custom allocators. `unwrap` on I/O is still a bug.

## Deprecated APIs to never generate

Do not generate `unwrap()` on `Result` from I/O, or `unsafe` to skip the borrow checker.

## Commands

Run `cargo test -p` for the package you changed.

## Example

```rust
fn read_port(raw: &str) -> Result<u16, ParseError> {
    raw.parse().map_err(|_| ParseError::Port)
}
```
