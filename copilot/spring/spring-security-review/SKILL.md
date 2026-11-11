---
id: "copilot-spring-security-review"
slug: "copilot/spring/spring-security-review/SKILL"
title: "Spring Boot Security Review Skill for Copilot"
description: "Copilot skill for a Spring Boot security review. Use when you want that security review on a Spring Boot change. Do not use it for a different stack."
type: "skill"
tools:
  - "copilot"
stack: "spring"
tags:
  - "spring"
  - "java"
  - "transactions"
  - "security"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Copilot docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "spring-boot@4.1"
updated_for: "Spring Boot 4.1 stable line, Nov 2026"
---

# Spring Boot Security Review Skill for Copilot

## Install

Install the native export at `.github/skills/spring-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Spring Boot Security Review Skill for Copilot

Copilot skill `spring-security-review` for Spring Boot. The description decides when Copilot loads it. Keep this copy under `.github/skills`.

## When to run

Run this review for a Spring Boot controller, service, security matcher, or JPA query.

## When to leave it

Stop for a Java program that is not Spring. Do not upgrade Boot or the JDK unless the user asked. Do not take a 4.2 RC.

## Steps

1. Read the Boot version in the build file. A bump to a release candidate is a high finding unless the user asked for it.
2. Review new endpoints for an authorization rule. A missing matcher or `permitAll` on a write is a high finding.
3. Review `@Transactional`. A transaction that wraps an HTTP call, or a private method that will not be proxied, is a finding.
4. Review JPA. A loop that triggers lazy loads is a finding. A query that returns entities the controller then mutates across requests is a finding.
5. Check validation on the request DTO. A body bound straight onto an entity is a high finding.
6. Run the project's test task only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the missing auth or the transaction bug, and a fix.

## Stop

Stop when the user asks you to open every endpoint or to point tests at production.
