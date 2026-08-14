# Java Backend Interview Preparation

An interview-preparation vault for Java backend roles. Start with the roadmap, then learn a topic, practise it in code, and explain its trade-offs aloud.

> [!tip] Default study target
> Learn the fundamentals so you can work on any Java version, but write new examples with **Java 25 LTS** in mind. Keep **Java 21 LTS** fluent because it remains common in production and in interviews.

## Start Here

1. [🎯 Interview Preparation Master Plan](Interview-Preparation-Master-Plan.md) — **START HERE** · 45-day plan integrating DSA, Java, Spring, LLD, HLD
2. [Java Backend Interview Roadmap](Roadmap/Java-Backend-Interview-Roadmap.md)
3. [Current Java and Spring Backend Standards](Reference/Current-Java-and-Spring-Backend-Standards.md)
4. [Core Java Interview Questions](Interview-Guides/Core-Java-Interview-Questions.md)
5. [Java Coding Practice Plan](Practice/Java-Coding-Practice-Plan.md)

## Interview Guides

| Area | Study note |
|---|---|
| 🎯 Full interview preparation (45-day plan) | [Interview Preparation Master Plan](Interview-Preparation-Master-Plan.md) |
| Spring Boot, REST, JPA, transactions, security, testing | [Spring Boot Interview Questions](Interview-Guides/Spring-Boot-Interview-Questions.md) |
| Core Java, OOP, collections, concurrency, and JVM | [Core Java Interview Questions](Interview-Guides/Core-Java-Interview-Questions.md) |
| Lambdas, streams, `Optional`, and `CompletableFuture` | [Java 8 and Streams Interview Questions](Interview-Guides/Java-8-and-Streams-Interview-Questions.md) |
| Modules, records, sealed classes, and pattern matching | [Java 9 to 17 Features Interview Questions](Interview-Guides/Java-9-to-17-Features-Interview-Questions.md) |
| Java 21–26, including virtual threads and feature status | [Modern Java Interview Questions](Interview-Guides/Modern-Java-Interview-Questions.md) |
| SQL and database fundamentals | [SQL Interview Questions](Interview-Guides/SQL-Interview-Questions.md) |

> **HLD topics moved to their own folder:** [HLD](../HLD/00%20-%20Index.md) — System Design, Kafka, Docker

## Reference Sheets

- [Java Stream Creation Guide](Reference/Java-Stream-Creation-Guide.md) — stream sources for collections, arrays, `char[]`, I/O, ranges, and more.
- [Java and SQL Interview Quick Reference](Reference/Java-and-SQL-Interview-Quick-Reference.md)
- [Current Java and Spring Backend Standards](Reference/Current-Java-and-Spring-Backend-Standards.md)

## Practice

- [Code Snippet Practice](Practice/Code-Snippet-Practice/README.md) — predict output, then explain why.
- [Solved Exercises](Practice/Solved-Exercises/README.md) — Java streams, collections, concurrency, and JPA drills.
- [Java Coding Practice Plan](Practice/Java-Coding-Practice-Plan.md) — curated exercise order and links to every solution.

## Recommended Learning Order

1. Core Java: OOP, strings, collections, exceptions, generics, and JVM basics.
2. Java 8: functional interfaces, streams, collectors, `Optional`, and `CompletableFuture`.
3. Concurrency: Java Memory Model, executors, locks, `CompletableFuture`, and virtual threads.
4. Modern Java: records, sealed classes, pattern matching, modules, and Java 21+ features.
5. Backend: Spring Boot, REST, validation, persistence, SQL, security, caching, and messaging.
6. Production: Docker, observability, configuration, deployment, reliability, and system design.

## Interview Answer Framework

For a strong answer, give the definition, explain the mechanism, show a small example, state a trade-off, and connect it to a production scenario. Avoid reciting APIs without explaining when they are appropriate.

## Vault Conventions

- Descriptive filenames replace numeric prefixes.
- `Interview-Guides` contains theory and interview answers.
- `Reference` contains condensed standards and quick-reference material.
- `Practice` contains drills and solutions.
- Each standards-sensitive note should identify stable features separately from preview or incubating features.
