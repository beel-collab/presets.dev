<!-- Append this section to GEMINI.md. Do not replace the existing file. Antigravity CLI also loads AGENTS.md, so do not paste this section into both. /context lists the loaded files. -->

# Docker Antigravity CLI Rules: Images, Runtime Users and Build Secrets

Section to append to `GEMINI.md` for Docker. Antigravity CLI loads every `GEMINI.md` and every `AGENTS.md` it finds. Do not put this same section in both files. Confirm with `/context`.

## Updated for Docker Engine 29, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

Keep Engine, BuildKit, and Compose versions as the project already pins them. Engine 29 is the current major to write for when the host is already on it. Do not assume a Compose feature from a newer file works on an older plugin. Read the existing Dockerfile before you add a stage.

## Image shape

A multi-stage build compiles in one stage and copies the artifact into a small runtime stage. The runtime stage does not include the compiler, the package manager cache, or the tests. Pin the base image by digest or by a version tag the project already updates on purpose. Do not use `latest`.

`.dockerignore` excludes `.git`, secrets, and local env files. A `COPY . .` of a context that contains `.env` bakes the secret into a layer.

## Build secrets and runtime

A secret needed at build time uses a BuildKit secret mount. It does not use `ARG` or `ENV` for a token, because those stay in history. The final image does not contain the secret file.

The runtime process has a `USER` that is not root. Files it writes live in a directory that user owns. A healthcheck hits the app's ready endpoint. The process handles `SIGTERM` so a stop is not a kill ten seconds later.

## Compose and privileges

Compose declares the same user, a read-only root filesystem when the app can live with it, and no extra capabilities. Do not mount `/var/run/docker.sock` into an application container. Do not set `privileged: true` to fix a permission error. Fix the user or the volume.

Ports bind to the interface the project intends. A database port is not published on the public interface for a local convenience that will be copied to production.

## Checks

Build the image and scan the history for `ENV` secrets and a root user when the user asked you to build. `docker history` and a config linter are the evidence. Record the command. Do not push the image.

## Mistakes to avoid

- `latest` as a base tag.
- A token in `ARG` or `ENV`.
- A root `USER` in the runtime stage.
- The Docker socket mounted into the app.
- A single-stage image that ships the toolchain.

## What changed in this major

Engine 29 is the current major. BuildKit secrets and a non-root `USER` are the defaults to write.

## Deprecated APIs to never generate

Do not write a top-level `version:` key in a Compose file. Current Compose treats that key as obsolete and ignores it.

## Commands

Run `docker build` only when asked. Do not push.

## Example

```dockerfile
FROM node:22-bookworm-slim
USER node
```
