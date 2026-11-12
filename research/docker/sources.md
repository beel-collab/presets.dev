# Docker sources

Fetched 12 November 2026.

- https://docs.docker.com/engine/release-notes/29/ is the Engine 29 notes. The newest patch on that page is 29.9.3, dated 3 November 2026. It includes Engine, SwarmKit, and BuildKit security fixes. Engine, BuildKit, and Compose stay on separate version lines.
- The standards reject `latest` base tags, a root runtime user, secrets in `ARG` or `ENV`, and a mounted Docker socket. Those are operating rules, not a 29.9.3 language change.
