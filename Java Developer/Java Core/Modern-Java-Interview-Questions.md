# Modern Java Interview Questions: Java 21 to 26

Java 25 is the current LTS release. This guide focuses on production-relevant features introduced after Java 17 and labels preview APIs clearly. For records, sealed classes, modules, and earlier language features, see [Java 9 to 17 Features Interview Questions](Java-9-to-17-Features-Interview-Questions.md).

## Release Strategy

### 1. Which Java version should a new backend service use?

**Answer:** Default to Java 25 LTS for a new service unless the organisation standardises on Java 21 LTS. Know both. Java 26 is a feature release, so use it to evaluate new features but do not choose it for a long-lived service without a deliberate support plan.

Java 8, 11, 17, 21, and 25 are LTS releases. [Oracle Java SE support roadmap](https://www.oracle.com/in/java/technologies/java-se-support-roadmap.html)

### 2. How should you discuss preview and incubator APIs?

**Answer:** Name the JDK, say that preview features require `--enable-preview` at compile and runtime, and do not present them as a default production dependency. A feature may be changed, re-previewed, finalised, or removed in a later JDK.

For example, primitive patterns in `instanceof` and `switch` remain a preview feature in Java 26, while structured concurrency is in its sixth preview. [Java SE specifications](https://docs.oracle.com/javase/specs/) and [JDK 26 features](https://openjdk.org/projects/jdk/26/)

## Java 21 Essentials

### 3. What are virtual threads?

**Answer:** Virtual threads are lightweight threads managed by the JDK rather than being mapped one-to-one to operating-system threads. They make a thread-per-task style practical when tasks spend much of their time blocked on I/O.

```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    var users = executor.submit(() -> userClient.fetchUsers());
    var orders = executor.submit(() -> orderClient.fetchOrders());
    return new Dashboard(users.get(), orders.get());
}
```

**When they help:** high-concurrency, blocking HTTP/database/file work where the client libraries cooperate with the JDK.

**What they do not solve:** CPU capacity, connection-pool size, downstream rate limits, unbounded request admission, or poor timeout/retry policy. Do not pool virtual threads; bound the scarce resource instead, such as database connections or calls to a downstream service.

### 4. What is pinning, and why does it matter with virtual threads?

**Answer:** A virtual thread can temporarily pin its carrier thread when it blocks while holding a monitor or when executing some native code. Excessive pinning reduces scalability. Prefer `java.util.concurrent` locks where appropriate, keep blocking work out of long `synchronized` sections, and confirm behavior with profiling and load tests rather than guessing.

### 5. What are sequenced collections?

**Answer:** Java 21 added `SequencedCollection`, `SequencedSet`, and `SequencedMap` to give ordered collections a common first/last/reversed API.

```java
List<String> stages = new ArrayList<>(List.of("received", "validated", "saved"));
String first = stages.getFirst();
String last = stages.getLast();
List<String> newestFirst = stages.reversed();
```

Use the API when order is part of the contract; do not assume every `Set` or `Map` has a meaningful encounter order.

### 6. Which pattern-matching features are stable?

**Answer:** Pattern matching for `instanceof`, record patterns, and pattern matching for `switch` are permanent by Java 21.

```java
static String describe(Object value) {
    return switch (value) {
        case null -> "missing";
        case Integer number when number > 0 -> "positive number";
        case String text -> "text: " + text;
        default -> "other";
    };
}
```

The `when` guard above is stable. Keep the `default` branch unless the compiler can prove a sealed hierarchy is exhaustive.

## Java 22 to 25 Essentials

### 7. What problem does the Foreign Function and Memory API solve?

**Answer:** It provides a safer, supported way to call native code and manage off-heap memory, replacing many JNI use cases. It is relevant for high-performance or platform integrations, not routine Spring Boot CRUD services. The API became permanent in Java 22.

### 8. What are scoped values, and how do they differ from `ThreadLocal`?

**Answer:** A scoped value shares immutable context with code called within a bounded dynamic scope, including child threads. Unlike `ThreadLocal`, it is not a general mutable per-thread bag, and its lifetime is explicit.

```java
private static final ScopedValue<String> CORRELATION_ID = ScopedValue.newInstance();

ScopedValue.where(CORRELATION_ID, requestId)
        .run(() -> service.handle(command));
```

Scoped values became permanent in Java 25. Prefer explicit method parameters for ordinary dependencies; use scoped context selectively for cross-cutting, read-only metadata such as a correlation ID.

### 9. Are structured concurrency APIs ready to use as a stable default?

**Answer:** No. Structured concurrency expresses related subtasks as one operation with a shared lifetime, error policy, and cancellation boundary. It is conceptually important and works naturally with virtual threads, but it remains a preview API in Java 26. State the JDK and preview status before suggesting it for production.

### 10. What are Stream Gatherers?

**Answer:** Stream Gatherers let you define reusable intermediate stream operations that can be stateful and can emit zero, one, or many results per input. They became permanent in Java 24. Use them when a custom pipeline operation is clearer than a complicated collector; do not force them into simple `map`/`filter` workflows.

### 11. Which Java 25 features are useful to know but uncommon in enterprise services?

**Answer:** Module imports, compact source files with instance `main` methods, and flexible constructor bodies are permanent Java 25 features. They reduce ceremony, particularly in small programs and learning material. Normal package, module, and class conventions remain appropriate for most production services.

### 12. What performance/operations improvements should a backend developer know from Java 25?

**Answer:** Know the themes rather than memorising every JEP: compact object headers, generational Shenandoah, ahead-of-time profiling/ergonomics, and richer JFR profiling. A strong answer is: measure with JFR, metrics, and load tests; then choose a GC and tuning strategy based on latency, allocation rate, heap, and deployment constraints.

## Migration Questions

### 13. How do you migrate from Java 8 or 11 to Java 21/25 safely?

1. Inventory runtime, build plugins, framework versions, transitive dependencies, bytecode agents, and container base image.
2. Upgrade the framework and dependencies to versions supported by the target JDK before modernising application code.
3. Fix removed APIs, encapsulation/reflection warnings, and `javax.*` to `jakarta.*` migrations where the framework requires it.
4. Run unit, integration, contract, performance, and security tests on the target JDK in CI.
5. Roll out gradually with health checks, metrics, logs, traces, and a rollback plan.
6. Adopt records, pattern matching, virtual threads, or scoped values only when they improve a real design or measured bottleneck.

### 14. What common migration mistakes should you call out?

- Treating virtual threads as a replacement for database connection pooling or back pressure.
- Enabling preview APIs in a production service without a lifecycle decision.
- Upgrading the JDK without upgrading incompatible framework, bytecode, or test dependencies.
- Changing behavior and infrastructure at the same time, which makes regressions hard to isolate.
- Assuming a record is a valid JPA entity or deeply immutable aggregate.

## Rapid-Fire Revision

| Topic | One-line answer |
|---|---|
| Java 25 | Current LTS; a good default for new learning projects. |
| Java 26 | Current non-LTS feature release; evaluate features, but manage its short support window. |
| Virtual threads | Scale blocking I/O concurrency, not CPU or downstream capacity. |
| Scoped values | Bounded, immutable context propagation; permanent in Java 25. |
| Structured concurrency | Valuable model, but still preview in Java 26. |
| Preview API | Requires `--enable-preview`; version-specific and not a stable default. |
| Stream Gatherers | Custom intermediate stream operations; permanent in Java 24. |

## Sources

- [Oracle Java SE support roadmap](https://www.oracle.com/in/java/technologies/java-se-support-roadmap.html)
- [JEPs integrated in JDK 25 since JDK 21](https://openjdk.org/projects/jdk/25/jeps-since-jdk-21)
- [Java SE specifications](https://docs.oracle.com/javase/specs/)
