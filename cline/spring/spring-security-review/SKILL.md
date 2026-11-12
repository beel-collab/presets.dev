---
id: "cline-spring-security-review"
slug: "cline/spring/spring-security-review/SKILL"
title: "Spring Boot Security Review Skill for Cline"
description: "Review a Spring Boot change for authorization, transaction boundaries, and query shape. Use for a Spring Boot security review. Do not use for a non-Spring Java program or to add an M, RC, or SNAPSHOT version."
type: "skill"
tools:
  - "cline"
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
  - "Cline docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "spring-boot@4.1"
updated_for: "Spring Boot 4.1 stable line, Nov 2026"
---

# Spring Boot Security Review Skill for Cline

## Install

Install the native export at `.cline/skills/spring-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# Spring Boot Security Review Skill for Cline

Cline skill `spring-security-review` for Spring Boot. `/spring-security-review` forces it. A global skill of the same name overrides this project file.

## When to run

Run this review for a Spring Boot controller, service, security matcher, or JPA query.

## When to leave it

Stop for a Java program that is not Spring. Do not upgrade Boot or the JDK unless the user asked. Do not add an M, RC, or SNAPSHOT version.

## Steps

1. Read the Boot version in the build file. A bump to an M, RC, or SNAPSHOT version is a high finding unless the user asked for it.
2. Review new endpoints for an authorization rule. A missing matcher or `permitAll` on a write is a high finding.
3. Review `@Transactional` and `@Async`. A transaction that wraps an HTTP call is a finding. A self-call (`this.method()`) onto a `@Transactional` or `@Async` method in the same class is a high finding, because the proxy never sees it.
4. Review JPA. A loop that triggers lazy loads is a finding. A query that returns entities the controller then mutates across requests is a finding.
5. Check validation on the request DTO. A body bound straight onto an entity is a high finding.
6. Run the project's test task only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the missing auth or the transaction bug, and a fix.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: `NoteService.create` is `@Transactional` and `NoteService.importAll` calls `this.create(row)`.
Output: high | NoteService.java:28 | self-invocation skips the proxy, so the transaction does not start | call `create` through the injected bean.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## What to check

- Injection: a native query built by concatenating a request parameter.
- XSS: a template renders user text with the escape disabled.
- CSRF: a browser state change with CSRF disabled on the security filter chain.
- Secrets: a password in `application.yml` that is committed.
- IDOR: a path id loaded with no authorization check.
- SSRF: `RestClient` calls a URL from the request with no allow-list.
- Transactions: `this.method()` on a `@Transactional` or `@Async` method, which skips the proxy.

## Stop

Stop when the user asks you to open every endpoint or to point tests at production.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
