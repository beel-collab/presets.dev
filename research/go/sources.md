# Go sources

Fetched 12 November 2026.

- Registry: https://go.dev/dl/?mode=json lists stable `go1.27.4` and `go1.26.11`.
- https://go.dev/doc/go1.27 documents `encoding/json/v2`. The notes say compatibility problems with the new implementation can be disabled with `GOEXPERIMENT=nojsonv2`, which restores the v1 implementation. SIMD is a separate package enabled only by `GOEXPERIMENT=simd`. Do not set that as a default, and do not flag ordinary `encoding/json` use.
