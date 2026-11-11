---
name: "spring-security-review"
description: "Review a Spring Boot change for authorization, transaction boundaries, and query shape. Use for a Spring Boot security review. Do not use for a non-Spring Java program or to adopt a Boot 4.2 release candidate."
---

# Spring Boot Security Review Skill for Cline

Cline skill `spring-security-review` for Spring Boot. `/spring-security-review` forces it. A global skill of the same name overrides this project file.

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
