# Rust sources

Fetched 12 November 2026.

- https://raw.githubusercontent.com/rust-lang/rust/master/RELEASES.md opens with Version 1.100.0 (2026-11-12) and lists stabilization of the never type and custom allocators.
- https://releases.rs/docs/1.100.0/ is the same changelog, fetched the same day. The Rust blog index at https://blog.rust-lang.org/ did not yet list a 1.100.0 announcement post, and https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/ returned 404.
- https://docs.rs/tokio/latest/tokio/sync/struct.Mutex.html documents `tokio::sync::Mutex` as the lock that may be held across `.await`. `std::sync::Mutex` may not.
- A crate keeps the MSRV in its manifest. `unsafe` is not a borrow-checker bypass.
