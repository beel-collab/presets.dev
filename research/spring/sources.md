# Spring Boot sources

Fetched 12 November 2026.

- https://api.github.com/repos/spring-projects/spring-boot/releases lists stable `v4.1.2` (22 October 2026) and prerelease `v4.2.0-RC2` (5 November 2026). Stay on the 4.1 line. Do not add the 4.2 release candidate.
- The release index is https://github.com/spring-projects/spring-boot/releases.
- https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html documents the proxy: a self-invocation (`this.method()`) does not run `@Transactional` or `@Async` on the callee.
