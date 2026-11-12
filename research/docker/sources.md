# Docker sources

Fetched 12 November 2026.

- https://docs.docker.com/engine/release-notes/29/ is the Engine 29 notes. The newest patch on that page is 29.9.3, dated 3 November 2026. Engine, BuildKit, and Compose stay on separate version lines.
- https://docs.docker.com/build/building/secrets/ documents BuildKit secrets. Do not pass a secret as `ARG` or `ENV`.
- The standards also reject a `latest` base tag, a root runtime user, and a mounted Docker socket. Those are operating rules, not a 29.9.3 language change.
- https://docs.docker.com/reference/compose-file/version-and-name/ says the top-level `version` property is obsolete. Compose warns if you set it and still uses the current schema.
