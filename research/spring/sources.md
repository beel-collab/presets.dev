# Spring Boot sources

Fetched 12 November 2026.

- https://api.github.com/repos/spring-projects/spring-boot/releases lists stable `v4.1.2` (22 October 2026) and prerelease `v4.2.0-RC2` (5 November 2026). Stay on the 4.1 line. Do not add an M, RC, or SNAPSHOT version.
- The release index is https://github.com/spring-projects/spring-boot/releases.
- https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html documents the proxy: a self-invocation (`this.method()`) does not run `@Transactional` or `@Async` on the callee.
- https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide says `@MockBean` and `@SpyBean` were removed in favor of `@MockitoBean` and `@MockitoSpyBean`. https://docs.spring.io/spring-security/site/docs/5.8.12/api/org/springframework/security/config/annotation/web/configuration/WebSecurityConfigurerAdapter.html marks `WebSecurityConfigurerAdapter` deprecated in 5.8. The class is absent from the Spring Security 6.0.0 configuration package (https://docs.spring.io/spring-security/site/docs/6.0.0/api/org/springframework/security/config/annotation/web/configuration/package-summary.html) and the source file 404s at tag 6.0.0, so it was removed in Spring Security 6. Declare a `SecurityFilterChain` bean. https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html documents `requestMatchers`.
