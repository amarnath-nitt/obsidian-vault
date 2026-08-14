# Current Java and Spring Backend Standards

**Reviewed:** 13 August 2026  
**Purpose:** Use this note to separate durable interview knowledge from version-specific details.

## Default Versions for New Learning Projects

| Concern | Default | Why it matters in interviews |
|---|---|---|
| JDK | Java 25 LTS | The current LTS release; use it as the target for new sample projects. |
| Compatibility baseline | Java 21 LTS | Still widely deployed; know its features, especially virtual threads. |
| Latest feature release | Java 26 | Learn the headline changes, but do not make preview APIs your default production answer. |
| Spring Boot | Spring Boot 4.1.x | The current stable line. It requires Java 17+ and supports up to Java 26. |
| Build | Maven or Gradle | Be comfortable reading both; use the wrapper (`mvnw` or `gradlew`) in projects. |
| Persistence | Spring Data JPA / Hibernate with SQL knowledge | Explain SQL and transaction behavior rather than relying only on repository methods. |

Oracle lists Java 8, 11, 17, 21, and 25 as LTS releases; Java 25 is the current LTS and Java 26 is a non-LTS release. [Oracle Java SE support roadmap](https://www.oracle.com/in/java/technologies/java-se-support-roadmap.html)

Spring Boot 4.1 requires Java 17 or later, supports through Java 26, and explicitly supports Maven 3.6.3+ and Gradle 8.14+/9.x. [Spring Boot system requirements](https://docs.spring.io/spring-boot/system-requirements.html)

## What to Use in Interview Examples

- Use Java 21 or 25 syntax unless the question specifies an older project.
- Prefer records for immutable request/response data; use normal classes when a framework or domain model needs mutability, inheritance, or an ORM-friendly entity.
- Prefer `switch` expressions, pattern matching, text blocks, `List.of`, `Map.of`, and `java.time` where they make code clearer.
- Use virtual threads for many blocking, mostly I/O-bound tasks. They do not make CPU-bound work faster and they do not remove database, HTTP-client, or downstream capacity limits.
- Use `ExecutorService`, `CompletableFuture`, structured cancellation concepts, back pressure, and bounded concurrency deliberately. Do not answer "virtual threads replace all pools".
- Use `try-with-resources` for cleanup. Do not recommend finalization; it is deprecated for removal.
- For Spring Boot 3+ and 4+, use `jakarta.*` APIs, not legacy `javax.*` APIs.

## Modern Java Feature Status

| Feature | Status to communicate | Interview-ready guidance |
|---|---|---|
| Records | Permanent | Excellent for immutable data carriers; they are shallowly immutable. |
| Sealed classes | Permanent | Model a closed hierarchy and make `switch` handling safer. |
| Pattern matching for `instanceof` and `switch` | Permanent | Reduces casts and makes type-based branching clearer. |
| Virtual threads | Permanent in Java 21 | Use for high-concurrency blocking I/O after load testing. |
| Sequenced collections | Permanent in Java 21 | Know `getFirst`, `getLast`, `reversed`, and their collection interfaces. |
| Foreign Function and Memory API | Permanent in Java 22 | Relevant when safely interoperating with native libraries; not a routine Spring service concern. |
| Stream Gatherers | Permanent in Java 24 | Know the use case: custom intermediate stream operations. |
| Preview / incubator APIs | Explicitly version-dependent | Name the JDK and say they require `--enable-preview`; do not treat them as stable defaults. |

Java 26 is released, and primitive patterns in `instanceof` and `switch` are still a preview feature. [Java SE specifications](https://docs.oracle.com/javase/specs/)

## Spring Boot Expectations

For a production-style service, be able to explain and demonstrate:

1. Constructor injection and bean lifecycle; avoid field injection in application code.
2. Validation at API boundaries using `jakarta.validation` and a consistent error response.
3. Transaction boundaries, propagation, isolation, optimistic locking, and the N+1 query problem.
4. Authentication/authorization, secret handling, and never logging credentials or tokens.
5. Timeouts, retries only when operations are safe to retry, idempotency, and circuit breaking where appropriate.
6. Health checks, metrics, structured logs, tracing, and correlation IDs.
7. Database migrations, indexes, query plans, and connection-pool limits.
8. Container images that run as a non-root user and expose configuration through environment-specific mechanisms.

## Interview Priority by Experience Level

| Early career | Mid-level | Senior / lead |
|---|---|---|
| Core Java, collections, SQL joins, REST, Spring fundamentals, DSA | Concurrency, JPA performance, transactions, testing, Docker, caching, messaging | Trade-offs, distributed consistency, observability, failure modes, capacity, security, system design, and leadership stories |
| Explain code precisely | Explain operational behavior | Explain decisions and measurable outcomes |

## Migration Answer: Java 8/11 to Java 21/25

Use this order in an interview answer:

1. Inventory JDK, framework, build plugins, library compatibility, container image, and `javax` dependencies.
2. Upgrade and test on the existing behavior before refactoring application code.
3. Resolve illegal reflective access, removed APIs, and framework migrations; move to `jakarta.*` where required.
4. Add CI on the target JDK, run unit/integration/performance tests, and deploy progressively with observability.
5. Adopt records, pattern matching, and virtual threads only where they improve a measured concern.

## Source Refresh Routine

Before an interview, refresh version-sensitive claims from the official release and support pages above. The Java platform follows a six-month release cadence, so feature status can change; keep permanent, preview, and incubating APIs separate in your answer.
