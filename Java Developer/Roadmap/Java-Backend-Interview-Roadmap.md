# Java Backend Interview Roadmap

Use this file as the spine of the Java Developer vault. It connects the interview guides and practice material into a start-to-advanced learning path.

> [!note] Current target
> Learn the concepts independently of any one release. For new examples, target Java 25 LTS; remain fluent with Java 21 and Java 8 because both are common in existing codebases and interviews. See [Current Java and Spring Backend Standards](../Reference/Current-Java-and-Spring-Backend-Standards.md) for version-sensitive guidance.

## How To Use This Package

Study in three passes:

1. **Concept pass:** Read the topic, understand the model, and write one tiny example.
2. **Recall pass:** Close the note and answer the question in your own words.
3. **Application pass:** Solve a coding task, debug a scenario, or explain a trade-off.

For every concept, practice this answer shape:

1. **Definition:** what it is.
2. **Purpose:** why Java has it.
3. **Mechanism:** how it works internally.
4. **Example:** small code or real project scenario.
5. **Trade-off:** when it fails, hurts performance, or becomes over-engineering.

## Learning Ladder

| Level | Goal                   | Topics                                                              | Files                                                                                                                                                                 |
| ----- | ---------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0     | Programming foundation | variables, control flow, methods, arrays, basic classes             | This file                                                                                                                                                             |
| 1     | Core Java              | OOP, strings, exceptions, collections, generics, JVM                | [Core Java guide](../Java%20Core/Core-Java-Interview-Questions.mdCore-Java-Interview-Questions.md)                                                                                               |
| 2     | Java 8                 | lambdas, streams, `Optional`, Date/Time, default methods            | [Java 8 and Streams guide](../Java%20Core/Java-8-and-Streams-Interview-Questions.mdJava-8-and-Streams-Interview-Questions.md)                                                                             |
| 3     | Modern Java            | modules, records, sealed classes, pattern matching, virtual threads | [Java 9 to 17 guide](../Java%20Core/Java-9-to-17-Features-Interview-Questions.mdJava-9-to-17-Features-Interview-Questions.md), [Java 21 to 26 guide](../Java%20Core/Modern-Java-Interview-Questions.mdModern-Java-Interview-Questions.md) |
| 4     | Backend Java           | Spring Boot, REST, SQL, JPA/Hibernate, testing                      | [Current backend standards](../Reference/Current-Java-and-Spring-Backend-Standards.md), [SQL guide](../SQL/SQL-Interview-Questions.md)SQL-Interview-Questions.md)                   |
| 5     | Architecture           | service boundaries, messaging, consistency, caching, HLD, LLD       | Practise from project stories and design exercises                                                                                                                    |
| 6     | Production readiness   | Docker, observability, troubleshooting, deployment basics           | [Docker guide](../../HLD/Docker-for-Java-Developers-Interview-Guide.md)                                                                                     |

## Java From Scratch

### What Java Is

Java is a strongly typed, object-oriented, garbage-collected language. Java source code is compiled into bytecode, and bytecode runs on the JVM. This is why the same `.class` or `.jar` can run on different operating systems if a compatible JVM is available.

```
Source Code (.java)
    -> javac compiler
Bytecode (.class)
    -> Class Loader
JVM Runtime
    -> Interpreter + JIT Compiler + Garbage Collector
Native Machine Code
```

### Basic Building Blocks

- **Variable:** named storage for a value.
- **Type:** defines allowed values and operations.
- **Method:** reusable behavior.
- **Class:** blueprint containing state and behavior.
- **Object:** runtime instance of a class.
- **Package:** namespace for organizing classes.

```java
class Account {
    private String owner;
    private double balance;

    Account(String owner, double balance) {
        this.owner = owner;
        this.balance = balance;
    }

    void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("amount must be positive");
        }
        balance += amount;
    }
}
```

### Primitive Types Vs Reference Types

Primitive values store the value directly: `int`, `long`, `double`, `boolean`, `char`, `byte`, `short`, `float`.

Reference variables store a reference to an object. The object itself lives on the heap.

```java
int count = 10;                  // primitive value
String name = "Asha";            // reference to String object
Account account = new Account("Asha", 500);
```

Interview point: `==` compares primitive values directly, but object references for objects. Use `.equals()` for logical object equality.

## OOP From Scratch To Depth

### Class, Object, State, Behavior, Identity

An object combines:

- **State:** fields, such as `balance`.
- **Behavior:** methods, such as `deposit`.
- **Identity:** two objects can have the same data but still be different objects.

```java
Account a = new Account("Ravi", 100);
Account b = new Account("Ravi", 100);

System.out.println(a == b); // false: different identities
```

### Encapsulation

Encapsulation protects object state and exposes controlled behavior.

Good encapsulation is not just "make fields private"; it is preserving invariants.

```java
class Wallet {
    private int balance;

    void addMoney(int amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("amount must be positive");
        }
        balance += amount;
    }

    int balance() {
        return balance;
    }
}
```

The invariant is: balance must not change through invalid operations.

### Abstraction

Abstraction hides implementation details and exposes useful capability.

```java
interface NotificationSender {
    void send(String userId, String message);
}

class EmailSender implements NotificationSender {
    public void send(String userId, String message) {
        // SMTP implementation hidden from caller
    }
}
```

The caller depends on the idea of "send notification", not SMTP details.

### Inheritance

Inheritance models an **is-a** relationship, but it should be used carefully. It is best when the subtype truly follows the parent contract.

```java
abstract class Payment {
    abstract void authorize();
}

class CardPayment extends Payment {
    void authorize() {
        // card authorization
    }
}
```

Use inheritance for stable hierarchies. Prefer composition when behavior varies frequently.

### Polymorphism

Polymorphism lets the same call dispatch to different behavior at runtime.

```java
List<NotificationSender> senders = List.of(new EmailSender(), new SmsSender());
for (NotificationSender sender : senders) {
    sender.send("u1", "Order shipped");
}
```

The caller does not need `if (type == EMAIL)` logic. This is the foundation of Strategy, Template Method, and many Spring patterns.

### Composition Over Inheritance

Composition means building a class from collaborators instead of extending another class.

```java
class OrderService {
    private final PaymentGateway paymentGateway;
    private final NotificationSender notificationSender;

    OrderService(PaymentGateway paymentGateway, NotificationSender notificationSender) {
        this.paymentGateway = paymentGateway;
        this.notificationSender = notificationSender;
    }
}
```

Benefits:

- Easier testing with mocks/fakes.
- Fewer fragile parent-child dependencies.
- Behavior can change at runtime by swapping collaborators.

### Association, Aggregation, Composition

| Relationship | Meaning | Example |
|---|---|---|
| Association | One object uses or knows another | `OrderService` uses `PaymentGateway` |
| Aggregation | Whole-part, part can live independently | `Department` has `Employee`s |
| Composition | Whole-part, part lifecycle belongs to whole | `Order` has `OrderLine`s |

Interview rule: do not force these words. Explain lifecycle ownership.

### SOLID In One Practical Model

- **SRP:** one reason to change.
- **OCP:** add behavior by extension, not repeated edits.
- **LSP:** subclasses must not surprise callers of the parent type.
- **ISP:** small interfaces are easier to implement correctly.
- **DIP:** depend on abstractions for volatile dependencies.

Production example:

```java
interface DiscountPolicy {
    BigDecimal discountFor(Order order);
}

class FestivalDiscountPolicy implements DiscountPolicy {
    public BigDecimal discountFor(Order order) {
        return order.total().multiply(new BigDecimal("0.10"));
    }
}

class PricingService {
    private final DiscountPolicy discountPolicy;

    PricingService(DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }
}
```

This design avoids hard-coded discount `if/else` chains and keeps pricing testable.

## Core Java Depth Map

### Equality And Hashing

Override `equals()` and `hashCode()` together when objects need logical equality, especially as keys in `HashMap` or elements in `HashSet`.

Rules:

- Equal objects must have the same hash code.
- Unequal objects may have the same hash code.
- Equality should be reflexive, symmetric, transitive, consistent, and handle null.

### Immutability

Immutable objects cannot change after construction.

Benefits:

- Thread-safe by default.
- Safer as map keys.
- Easier to reason about.

Checklist:

- Make class `final`, or prevent unsafe subclassing.
- Make fields `private final`.
- Do not expose mutable internal objects directly.
- Copy mutable inputs and outputs defensively.

### Collections

Choose collections by access pattern:

| Need | Good Choice | Why |
|---|---|---|
| Fast random access | `ArrayList` | index access is O(1) |
| Frequent queue operations | `ArrayDeque` | fast stack/queue operations |
| Unique values, no order | `HashSet` | average O(1) lookup |
| Unique sorted values | `TreeSet` | O(log n), sorted |
| Key-value lookup | `HashMap` | average O(1) |
| Ordered map iteration | `LinkedHashMap` | predictable insertion/access order |
| Concurrent key-value access | `ConcurrentHashMap` | segmented/bin-level concurrency |

### Generics

Generics give compile-time type safety.

```java
List<String> names = new ArrayList<>();
names.add("Asha");
String first = names.get(0); // no cast needed
```

Wildcard rule:

- `? extends T`: producer, read as `T`.
- `? super T`: consumer, write `T`.

Remember PECS: Producer Extends, Consumer Super.

### Exceptions

Use exceptions for exceptional flow, not normal branching.

- Checked exception: caller must handle or declare.
- Unchecked exception: programming error or invalid state.
- Custom exception: use when it adds domain meaning.

```java
class InsufficientBalanceException extends RuntimeException {
    InsufficientBalanceException(String message) {
        super(message);
    }
}
```

## Java 8 Mastery Map

### Lambda Expressions

A lambda is a compact implementation of a functional interface.

```java
Predicate<Order> isPaid = order -> order.status() == Status.PAID;
```

Important detail: lambdas can capture local variables only if they are final or effectively final.

### Functional Interfaces

Common interfaces:

- `Predicate<T>`: test.
- `Function<T, R>`: transform.
- `Consumer<T>`: perform side effect.
- `Supplier<T>`: provide value.
- `UnaryOperator<T>`: transform same type.
- `BinaryOperator<T>`: combine same type.

### Streams

A stream is not a data structure. It is a pipeline for processing data.

Pipeline shape:

```
source -> intermediate operations -> terminal operation
```

```java
Map<Department, Long> employeesByDepartment = employees.stream()
    .filter(Employee::isActive)
    .collect(Collectors.groupingBy(
        Employee::department,
        Collectors.counting()
    ));
```

Interview depth:

- Intermediate operations are lazy.
- Terminal operations trigger execution.
- Avoid shared mutable state.
- Parallel streams are useful mostly for CPU-heavy, independent work on large data.

### Optional

Use `Optional` as a return type when absence is expected.

Good:

```java
Optional<User> findByEmail(String email)
```

Avoid:

```java
Optional<User> user;       // field
void save(Optional<User>)  // parameter
```

Optional is a signal to the caller, not a universal null replacement.

### CompletableFuture

`CompletableFuture` helps compose asynchronous tasks.

```java
CompletableFuture<User> userFuture =
    CompletableFuture.supplyAsync(() -> userClient.getUser(userId));

CompletableFuture<List<Order>> orderFuture =
    CompletableFuture.supplyAsync(() -> orderClient.getOrders(userId));

CompletableFuture<UserProfile> profile =
    userFuture.thenCombine(orderFuture, UserProfile::new);
```

Know the difference:

- `thenApply`: transform value.
- `thenCompose`: flatten another future.
- `thenCombine`: combine two independent futures.
- `exceptionally`: recover from failure.

## JVM And Memory Model

### Runtime Areas

- **Heap:** objects and arrays.
- **Thread stack:** method frames and local variables.
- **Metaspace:** class metadata.
- **PC register:** current instruction per thread.
- **Native method stack:** native calls.

### Garbage Collection

GC removes unreachable objects. You do not manually free memory in Java.

Interview explanation:

1. Object is allocated, usually in Eden.
2. Minor GC moves surviving objects to survivor spaces.
3. Long-lived objects may move to old generation.
4. Major/mixed GC cleans older regions depending on collector.

### Java Memory Model

The Java Memory Model defines visibility and ordering guarantees between threads.

Key ideas:

- Atomicity: operation happens as one indivisible step.
- Visibility: one thread's write becomes visible to another.
- Ordering: compiler/CPU may reorder unless rules prevent it.

`volatile` gives visibility and ordering for a single variable, but not compound atomicity.

```java
volatile boolean running = true;
```

`synchronized` gives mutual exclusion plus visibility at lock enter/exit.

## Backend Java Depth

### Spring Boot

Core mental model:

- Spring creates objects called beans.
- Dependency injection wires beans.
- Auto-configuration creates common beans based on classpath and properties.
- AOP proxies power features like `@Transactional`, security, and caching.

Common interview trap: `@Transactional` on self-invocation fails because the method call does not pass through the proxy.

### REST API Design

Strong REST answers cover:

- Resource naming.
- HTTP method semantics.
- Status codes.
- Validation.
- Idempotency.
- Pagination.
- Error format.
- Authentication and authorization.

### SQL And JPA

Know both SQL and ORM behavior. JPA does not remove the need to understand joins, indexes, transaction isolation, and query plans.

High-priority pitfalls:

- N+1 queries.
- Lazy loading outside transaction.
- Missing indexes.
- Long transactions.
- Incorrect cascade settings.
- Optimistic lock conflicts.

## Architecture Depth

### Microservices

Do not answer "microservices are always better." Explain trade-offs.

Benefits:

- Independent deployment.
- Team ownership.
- Scaling by service.

Costs:

- Network failures.
- Observability complexity.
- Distributed transactions.
- Versioning and compatibility.

### Kafka

Core mental model:

- Topic stores events.
- Partitions provide ordering within a partition.
- Consumer group divides partitions among consumers.
- Offsets track progress.

Production topics:

- Idempotent consumers.
- Retry topic and dead-letter topic.
- Rebalance tuning.
- Schema compatibility.
- Outbox pattern for database plus Kafka consistency.

### System Design

Always structure answers:

1. Requirements.
2. Capacity estimates.
3. APIs.
4. Data model.
5. High-level components.
6. Scaling and bottlenecks.
7. Failure handling.
8. Security and observability.
9. Trade-offs.

## Practice Plan

### 14-Day Foundation Plan

| Day | Focus | Output |
|---|---|---|
| 1 | Java syntax and classes | create 5 small classes |
| 2 | OOP pillars | explain each with code |
| 3 | equality, strings, immutability | implement immutable `Money` |
| 4 | exceptions | design domain exceptions |
| 5 | collections | compare list, set, map choices |
| 6 | generics | write generic repository interface |
| 7 | review | answer 30 core questions aloud |
| 8 | lambdas | rewrite anonymous classes |
| 9 | streams | solve grouping/sorting problems |
| 10 | Optional | refactor null-heavy code |
| 11 | Date/Time | timezone and duration examples |
| 12 | CompletableFuture | compose two async calls |
| 13 | mini project | build library/order domain model |
| 14 | mock interview | 45-minute Java round |

### Advanced Practice Projects

1. **Parking Lot LLD:** OOP modeling, concurrency-safe spot assignment.
2. **In-memory Cache:** generics, eviction strategy, thread safety.
3. **Order Service API:** REST, validation, service layer, repository layer.
4. **Kafka Outbox Demo:** transaction boundary, event publishing, retry.
5. **Java Troubleshooting Drill:** read thread dumps, heap usage, and GC symptoms.

## Interview Readiness Checklist

- Can explain OOP with real code, not only definitions.
- Can choose the right collection and justify complexity.
- Can explain `HashMap` collisions, resizing, and Java 8 treeification.
- Can write `equals()` and `hashCode()` correctly.
- Can explain stream laziness and when parallel streams are harmful.
- Can use `Optional` without abusing it.
- Can explain checked vs unchecked exceptions with API design reasoning.
- Can explain `volatile`, `synchronized`, locks, and executors.
- Can explain JVM heap, stack, metaspace, GC, and memory leaks.
- Can connect Java knowledge to Spring Boot, JPA, REST, Kafka, and microservices.
