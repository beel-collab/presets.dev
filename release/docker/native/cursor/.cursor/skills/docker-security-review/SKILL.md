---
name: "docker-security-review"
description: "Review a Dockerfile or Compose file for root runtime, latest tags, secrets in layers, and the Docker socket. Use for a Docker security review. Do not use for a non-container change or to mount the Docker socket into an app container."
paths:
  - "**/Dockerfile"
  - "**/Dockerfile.*"
  - "**/docker-compose*.yml"
  - "**/docker-compose*.yaml"
  - "**/compose.yml"
  - "**/compose.yaml"
---

# Docker Security Review Skill for Cursor

Cursor skill `docker-security-review` for Docker. Run it with `/docker-security-review`, or let Agent select it when the request matches. `paths` only limits automatic surfacing.

## When to run

Run this review for a Dockerfile, a Compose file, or a request to "check the image".

## When to leave it

Do not upgrade dependencies or the framework version unless the user asked.

Stop for a change that does not touch containers. Do not push an image or log into a registry.

## Steps

1. Read the base image reference. `latest`, or no pin at all, is a high finding.
2. Search for `ARG` and `ENV` values that look like tokens, and for `COPY` of `.env`. A secret in a layer is a high finding. Recommend a BuildKit secret mount.
3. Confirm the runtime stage sets `USER` to a non-root user. Root is a high finding unless the comment explains a hard requirement.
4. Search Compose for `privileged`, `docker.sock`, and published database ports. Each is a high finding in an app service.
5. Confirm a healthcheck and that the process can receive `SIGTERM`.
6. Build only if the user asked and the daemon is local. Otherwise write `not run`. Do not push.

## Output

Findings with severity, file, line, the insecure instruction, and the replacement. No registry credentials in the report.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: a runtime stage ends with `USER root` and `ENV DATABASE_URL=postgres://app:secret@db/app`.
Output: high | Dockerfile:18 | the process runs as root and the database URL is baked into the image | `USER node`. Pass `DATABASE_URL` when the container starts, from Compose, Kubernetes, or the runtime environment. A BuildKit secret mount exists only during the build. Use it for a build-time credential, not for this URL.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## What to check

- Image: a `latest` base tag, or a runtime stage that copies a secret file into the image.
- Secrets: a token in `ARG`, `ENV`, or a committed `.env` in the build context.
- User: the runtime stage leaves the process as root.
- Socket: the Docker socket is mounted into a container.
- Privileges: `--privileged` or a broad capability with no written reason.

## Stop

Stop when the user asks you to mount the Docker socket or to commit a `.env` into the build context.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
