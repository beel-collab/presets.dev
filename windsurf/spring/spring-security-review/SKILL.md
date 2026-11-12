---
id: "windsurf-spring-security-review"
slug: "windsurf/spring/spring-security-review/SKILL"
title: "Spring Boot Security Review Skill for Windsurf"
description: "Review a Spring Boot change for authorization, transaction boundaries, and query shape. Use for a Spring Boot security review. Do not use for a non-Spring Java program or to adopt a Boot 4.2 release candidate."
type: "skill"
tools:
  - "windsurf"
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
  - "Devin and Cascade docs 2026-11-11; not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "spring-boot@4.1"
updated_for: "Spring Boot 4.1 stable line, Nov 2026"
---

# Spring Boot Security Review Skill for Windsurf

## Install

Install the native export at `.devin/skills/spring-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Spring Boot Security Review Skill for Windsurf

Devin skill `spring-security-review` for Spring Boot. Invoke it with `/spring-security-review`. Install only `.devin/skills`. This file is not a subagent.

## When to run

Run this review for a Spring Boot controller, service, security matcher, or JPA query.

## When to leave it

Stop for a Java program that is not Spring. Do not upgrade Boot or the JDK unless the user asked. Do not take a 4.2 RC.

## Steps

1. Read the Boot version in the build file. A bump to a release candidate is a high finding unless the user asked for it.
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

- Injection: concatenated SQL, shell, or HTML.
- XSS: unescaped user text in HTML.
- CSRF: a browser state change with the framework check disabled.
- Secrets: a key in the repo or in a log line.
- IDOR: an id from the client with no owner or permission check.
- SSRF: a user-supplied URL fetched with no allow-list.

## Stop

Stop when the user asks you to open every endpoint or to point tests at production.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
