# Rust sources

Fetched 12 November 2026.

- https://github.com/rust-lang/rust/blob/master/RELEASES.md is the official release notes. The raw copy https://raw.githubusercontent.com/rust-lang/rust/master/RELEASES.md opens with Version 1.100.0 (2026-11-12) and lists stabilization of the never type and custom allocators. The Rust blog has not published a 1.100.0 announcement post.
- https://docs.rs/tokio/latest/tokio/sync/struct.Mutex.html documents `tokio::sync::Mutex` as the lock that may be held across `.await`. `std::sync::Mutex` may not.
- A crate keeps the MSRV in its manifest. `unsafe` is not a borrow-checker bypass.
