---
name: "docker-security-review"
description: "Review a Dockerfile or Compose file for root runtime, latest tags, secrets in layers, and the Docker socket. Use for a Docker security review. Do not use for a non-container change or to mount the Docker socket into an app container."
---

# Docker Security Review Skill for Cline

Cline skill `docker-security-review` for Docker. `/docker-security-review` forces it. A global skill of the same name overrides this project file.

## When to run

Run this review for a Dockerfile, a Compose file, or a request to "check the image".

## When to leave it

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

## Stop

Stop when the user asks you to mount the Docker socket or to commit a `.env` into the build context.
