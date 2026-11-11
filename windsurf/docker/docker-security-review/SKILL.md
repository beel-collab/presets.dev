---
id: "windsurf-docker-security-review"
slug: "windsurf/docker/docker-security-review/SKILL"
title: "Docker Security Review Skill for Windsurf"
description: "Windsurf skill for a Docker security review. Use when you want that security review on a Docker change. Do not use it for a different stack."
type: "skill"
tools:
  - "windsurf"
stack: "docker"
tags:
  - "docker"
  - "containers"
  - "supply-chain"
  - "security"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Devin and Cascade docs 2026-11-11; not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "docker-engine@29"
updated_for: "Docker Engine 29, Nov 2026"
---

# Docker Security Review Skill for Windsurf

## Install

Install the native export at `.devin/skills/docker-security-review/SKILL.md` and `.windsurf/skills/docker-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Docker Security Review Skill for Windsurf

Skill `docker-security-review` for Devin CLI and the legacy Windsurf skills folder. Invoke it with `/docker-security-review`. This file is not a subagent.

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
