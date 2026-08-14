# Java 8 — Code Snippet Practice

Practice these "What does this code print?" questions for Java 8 features — Streams, Lambdas, Optional, and Functional Interfaces. Attempt each snippet before revealing the answer.

Related theory: [Java 8 and Streams Interview Questions](Java Core/Core-Java-Interview-Questions.mdJava-8-and-Streams-Interview-Questions.md)

---

## Snippet 1 — Stream Reuse After Terminal Operation 🟢

**What happens when this code runs?**

```java
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        Stream<String> stream = List.of("A", "B", "C").stream();

        long count = stream.count();
        System.out.println("Count: " + count);

        List<String> list = stream.collect(Collectors.toList());
        System.out.println("List: " + list);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Count: 3
Exception in thread "main" java.lang.IllegalStateException:
stream has already been operated upon or closed
```

**Explanation:**
- A stream can only be consumed **once**. After a terminal operation (`count()`), the stream is closed.
- Calling another terminal operation (`collect()`) on the same stream throws `IllegalStateException`.
- **Fix:** Create a new stream for each terminal operation:

```java
List<String> source = List.of("A", "B", "C");
long count = source.stream().count();
List<String> list = source.stream().collect(Collectors.toList());
```

**Interview Tip:** "Streams are single-use pipelines. After a terminal operation, you must create a new stream from the source."

</details>

---

## Snippet 2 — Stream Lazy Evaluation 🟡

**What does this code print?**

```java
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        List<String> names = List.of("Alice", "Bob", "Charlie", "Diana");

        Stream<String> stream = names.stream()
            .filter(name -> {
                System.out.println("Filtering: " + name);
                return name.startsWith("A");
            })
            .map(name -> {
                System.out.println("Mapping: " + name);
                return name.toUpperCase();
            });

        System.out.println("Stream created, no output yet");
        System.out.println("---");

        String result = stream.findFirst().orElse("None");
        System.out.println("Result: " + result);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Stream created, no output yet
---
Filtering: Alice
Mapping: Alice
Result: ALICE
```

**Explanation:**
- Intermediate operations (`filter`, `map`) are **lazy** — they are NOT executed when defined.
- Nothing happens until a **terminal operation** (`findFirst()`) is called.
- `findFirst()` is a **short-circuiting** terminal operation — it stops processing as soon as it finds one result.
- Only "Alice" is processed because it passes the filter. "Bob", "Charlie", "Diana" are never touched.
- Stream operations are processed **element-by-element** (not stage-by-stage).

**Common wrong answer:** All 4 names filtered, then all mapped — streams process vertically, not horizontally.

**Interview Tip:** "Stream operations are lazy and process elements vertically. Short-circuiting operations like `findFirst()` stop early once a result is found."

</details>

---

## Snippet 3 — Optional.get() on Empty 🟢

**What happens when this code runs?**

```java
import java.util.Optional;

public class Main {
    public static void main(String[] args) {
        Optional<String> empty = Optional.empty();
        System.out.println(empty.get());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Exception in thread "main" java.util.NoSuchElementException: No value present
```

**Explanation:**
- `Optional.get()` throws `NoSuchElementException` if the Optional is empty.
- This defeats the purpose of Optional — it's just as bad as a NullPointerException.
- **Correct usage:**
```java
empty.orElse("default");
empty.orElseGet(() -> computeDefault());
empty.orElseThrow(() -> new NotFoundException("not found"));
empty.ifPresent(val -> process(val));
```
- `isPresent()` + `get()` is also valid but verbose — prefer `orElse()` / `map()` chains.

**Interview Tip:** "Never call `Optional.get()` without checking. Use `orElse()`, `orElseGet()`, `orElseThrow()`, `map()`, or `ifPresent()` instead."

</details>

---

## Snippet 4 — Lambda Capturing Non-Effectively-Final Variable 🟢

**Will this code compile?**

```java
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        int multiplier = 2;
        List<Integer> numbers = List.of(1, 2, 3, 4, 5);

        multiplier = 3;  // reassignment

        List<Integer> result = numbers.stream()
            .map(n -> n * multiplier)
            .collect(Collectors.toList());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Compilation Error: local variables referenced from a lambda expression
must be final or effectively final
```

**Explanation:**
- Lambdas can capture local variables, but they must be **final or effectively final**.
- "Effectively final" means the variable is never reassigned after initialization.
- `multiplier = 3;` makes it NOT effectively final → compilation error.
- **Fix 1:** Remove the reassignment.
- **Fix 2:** Use a final variable: `final int mult = 3;`
- **Fix 3:** Use an array or `AtomicInteger` (workaround, not recommended for simple cases):
```java
int[] multiplier = {3};
numbers.stream().map(n -> n * multiplier[0])...
```

**Interview Tip:** "Lambdas capture local variables by value. To prevent confusing behavior, Java requires captured variables to be effectively final."

</details>

---

## Snippet 5 — Collectors.toMap Duplicate Key 🟡

**What happens when this code runs?**

```java
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        List<String> words = List.of("apple", "banana", "avocado", "blueberry");

        Map<Character, String> map = words.stream()
            .collect(Collectors.toMap(
                w -> w.charAt(0),
                w -> w
            ));

        System.out.println(map);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Exception in thread "main" java.lang.IllegalStateException:
Duplicate key a (attempted merging values apple and avocado)
```

**Explanation:**
- "apple" and "avocado" both start with 'a', producing the same key.
- `Collectors.toMap()` without a merge function throws `IllegalStateException` on duplicate keys.
- **Fix — provide a merge function:**
```java
Collectors.toMap(
    w -> w.charAt(0),
    w -> w,
    (existing, replacement) -> existing + ", " + replacement
)
```
- Or use `groupingBy` when you expect multiple values per key:
```java
Collectors.groupingBy(w -> w.charAt(0))
```

**Interview Tip:** "Always provide a merge function to `Collectors.toMap()` when duplicate keys are possible. Without it, duplicates cause `IllegalStateException`."

</details>

---

## Snippet 6 — flatMap vs map With Optional 🟡

**What does this code print?**

```java
import java.util.Optional;

public class Main {
    static Optional<String> getEmail(String userId) {
        if ("u1".equals(userId)) return Optional.of("u1@mail.com");
        return Optional.empty();
    }

    static Optional<String> getDomain(String email) {
        int at = email.indexOf('@');
        return at > 0 ? Optional.of(email.substring(at + 1)) : Optional.empty();
    }

    public static void main(String[] args) {
        // Using map — produces Optional<Optional<String>>
        Optional<Optional<String>> nested = getEmail("u1")
            .map(email -> getDomain(email));

        // Using flatMap — produces Optional<String>
        Optional<String> flat = getEmail("u1")
            .flatMap(email -> getDomain(email));

        System.out.println("Nested: " + nested);
        System.out.println("Flat: " + flat);
        System.out.println("Flat value: " + flat.orElse("N/A"));
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Nested: Optional[Optional[mail.com]]
Flat: Optional[mail.com]
Flat value: mail.com
```

**Explanation:**
- `map()` wraps the return value in an Optional. If the mapper returns `Optional<String>`, you get `Optional<Optional<String>>` — a nested Optional.
- `flatMap()` expects the mapper to return an `Optional` and **flattens** it — no double wrapping.
- **Rule:** Use `map()` when the mapper returns a plain value. Use `flatMap()` when the mapper returns an `Optional`.

| Method | Mapper Returns | Result |
|---|---|---|
| `map(f)` | `T` | `Optional<T>` |
| `map(f)` | `Optional<T>` | `Optional<Optional<T>>` ❌ |
| `flatMap(f)` | `Optional<T>` | `Optional<T>` ✅ |

**Interview Tip:** "`flatMap` is for chaining Optional-returning methods without nesting. Same principle applies in Stream: `flatMap` flattens one-to-many."

</details>

---

## Snippet 7 — Parallel Stream Shared Mutable State 🔴

**What does this code print?**

```java
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> result = new ArrayList<>();

        IntStream.rangeClosed(1, 1000)
            .parallel()
            .forEach(i -> result.add(i));

        System.out.println("Size: " + result.size());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Non-deterministic. Could be:
Size: 987  (some number ≤ 1000)
or
ArrayIndexOutOfBoundsException
or
Size: 1000 (rarely, by luck)
```

**Explanation:**
- `ArrayList` is NOT thread-safe. Multiple parallel threads adding to it simultaneously causes:
  - Lost elements (race condition on internal array and size counter).
  - `ArrayIndexOutOfBoundsException` (concurrent resize).
- **Fix 1:** Use a synchronized collection:
```java
List<Integer> result = Collections.synchronizedList(new ArrayList<>());
```
- **Fix 2 (better):** Use a thread-safe collector:
```java
List<Integer> result = IntStream.rangeClosed(1, 1000)
    .parallel()
    .boxed()
    .collect(Collectors.toList());
```
- **Rule:** Never use shared mutable state with parallel streams. Use collectors instead.

**Interview Tip:** "Parallel streams and mutable shared state don't mix. Use `Collectors.toList()` instead of manually adding to a shared list."

</details>

---

## Snippet 8 — reduce With Wrong Identity 🟡

**What does this code print?**

```java
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        int sum1 = List.of(1, 2, 3).stream()
            .reduce(0, Integer::sum);

        int sum2 = List.of(1, 2, 3).stream()
            .reduce(10, Integer::sum);

        System.out.println("sum1: " + sum1);
        System.out.println("sum2: " + sum2);

        // Parallel with wrong identity
        int sum3 = List.of(1, 2, 3).parallelStream()
            .reduce(10, Integer::sum);

        System.out.println("sum3: " + sum3);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
sum1: 6
sum2: 16
sum3: 36 (or another unexpected value)
```

**Explanation:**
- `reduce(identity, accumulator)` starts with the identity value.
- `sum1`: `0 + 1 + 2 + 3 = 6` ✅ (identity `0` is correct for sum).
- `sum2`: `10 + 1 + 2 + 3 = 16` — works for sequential, but `10` is NOT a valid identity for addition (identity of sum should be `0`).
- `sum3` with parallel: Each chunk starts with `10`. If split into 3 chunks: `(10+1) + (10+2) + (10+3) = 36`. The wrong identity is applied multiple times.
- **Rule:** The identity must satisfy `accumulator(identity, x) == x` for all `x`. For sum, identity is `0`. For multiplication, identity is `1`.

**Interview Tip:** "The identity element in `reduce()` must be a true identity for the operation. With parallel streams, a wrong identity gets applied per chunk, amplifying the error."

</details>

---

## Snippet 9 — peek() Side Effects 🟡

**What does this code print?**

```java
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        List<String> result = List.of("a", "b", "c", "d")
            .stream()
            .peek(s -> System.out.println("Peek: " + s))
            .filter(s -> s.compareTo("b") > 0)
            .collect(Collectors.toList());

        System.out.println("Result: " + result);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Peek: a
Peek: b
Peek: c
Peek: d
Result: [c, d]
```

**Explanation:**
- `peek()` runs its action on **every element** that passes through that point in the pipeline — before the filter.
- All 4 elements pass through `peek` (it's before `filter`).
- Only "c" and "d" pass the filter (`compareTo("b") > 0`).
- **Warning:** `peek()` is designed for debugging only. Using it for business logic is an anti-pattern:
  - The behavior may change with parallel streams.
  - Short-circuiting operations may skip some peeks.
  - The API docs explicitly state it's "for debugging purposes."

**Interview Tip:** "`peek()` is for debugging stream pipelines. Don't rely on it for side effects in production code — use `forEach()` as the terminal operation instead."

</details>

---

## Snippet 10 — Method Reference Ambiguity 🔴

**Will this code compile?**

```java
import java.util.function.*;

public class Main {
    static void process(Consumer<String> consumer) {
        consumer.accept("Hello");
    }

    static void process(Function<String, String> function) {
        System.out.println(function.apply("Hello"));
    }

    public static void main(String[] args) {
        process(s -> System.out.println(s));        // Line A
        process(s -> s.toUpperCase());              // Line B
        process((Function<String, String>) s -> s.toUpperCase());  // Line C
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Line A: prints "Hello" (resolves to Consumer)
Line B: Compilation Error — ambiguous method call
Line C: prints "HELLO" (explicit cast resolves ambiguity)
```

**Explanation:**
- **Line A:** `s -> System.out.println(s)` returns `void` → matches `Consumer<String>` only → no ambiguity.
- **Line B:** `s -> s.toUpperCase()` returns `String` but can also be interpreted as a statement expression (void-compatible). It matches BOTH `Consumer<String>` and `Function<String, String>` → ambiguous.
- **Line C:** Explicit cast to `Function<String, String>` resolves the ambiguity.
- This is a Java type inference limitation with overloaded methods and lambdas.

**Interview Tip:** "Lambda type inference can cause ambiguity with overloaded methods. Use explicit casts or rename overloaded methods to avoid this."

</details>

---

## Snippet 11 — Stream sorted() Without Comparator 🟡

**What happens when this code runs?**

```java
import java.util.*;
import java.util.stream.*;

class Employee {
    String name;
    Employee(String name) { this.name = name; }
    public String toString() { return name; }
}

public class Main {
    public static void main(String[] args) {
        List<Employee> emps = List.of(
            new Employee("Charlie"),
            new Employee("Alice"),
            new Employee("Bob")
        );

        List<Employee> sorted = emps.stream()
            .sorted()
            .collect(Collectors.toList());

        System.out.println(sorted);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Exception in thread "main" java.lang.ClassCastException:
Employee cannot be cast to java.lang.Comparable
```

**Explanation:**
- `sorted()` without arguments uses **natural ordering**, which requires elements to implement `Comparable`.
- `Employee` does NOT implement `Comparable` → `ClassCastException` at runtime.
- **Fix — provide a Comparator:**
```java
.sorted(Comparator.comparing(e -> e.name))
```
- Or implement `Comparable<Employee>` in the class.
- Note: This is the same issue as TreeSet with non-Comparable objects.

**Interview Tip:** "`Stream.sorted()` without a Comparator requires elements to be `Comparable`. Always provide a Comparator for custom objects."

</details>

---

## Snippet 12 — Predicate Chaining 🟢

**What does this code print?**

```java
import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        Predicate<Integer> isEven = n -> n % 2 == 0;
        Predicate<Integer> isPositive = n -> n > 0;
        Predicate<Integer> isSmall = n -> n < 10;

        Predicate<Integer> combined = isEven.and(isPositive).and(isSmall);
        Predicate<Integer> negated = isEven.negate();

        List<Integer> numbers = List.of(-4, -1, 0, 3, 4, 8, 12, 15);

        List<Integer> result1 = numbers.stream()
            .filter(combined)
            .collect(Collectors.toList());

        List<Integer> result2 = numbers.stream()
            .filter(negated)
            .collect(Collectors.toList());

        System.out.println("Combined: " + result1);
        System.out.println("Negated: " + result2);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Combined: [4, 8]
Negated: [-1, 3, 15]
```

**Explanation:**
- `combined`: even AND positive AND less than 10 → `4` (even, positive, <10) and `8` (even, positive, <10). `0` fails positive. `12` fails <10. `-4` fails positive.
- `negated`: NOT even → odd numbers → `-1, 3, 15`. `0` is even, so excluded.
- Predicate composition methods:
  - `.and()` → logical AND
  - `.or()` → logical OR
  - `.negate()` → logical NOT
  - `Predicate.not()` (Java 11+) → static negation

**Interview Tip:** "Predicates compose with `.and()`, `.or()`, `.negate()`. This enables building complex filters from simple, reusable conditions."

</details>

---

## Quick Review Table

| # | Concept Tested | Key Rule |
|---|---|---|
| 1 | Stream reuse | Single-use — terminal operation closes the stream |
| 2 | Lazy evaluation | Intermediate ops only run when terminal op triggers |
| 3 | Optional.get() | Throws NoSuchElementException on empty |
| 4 | Lambda variable capture | Must be final or effectively final |
| 5 | toMap duplicate key | Must provide merge function |
| 6 | flatMap vs map | flatMap flattens nested Optional/Stream |
| 7 | Parallel stream + mutable state | Race condition — use collectors instead |
| 8 | reduce identity | Wrong identity amplified in parallel |
| 9 | peek() | Debug only — not for business logic |
| 10 | Method reference ambiguity | Overloaded methods + lambdas can cause ambiguity |
| 11 | sorted() without Comparator | Requires Comparable or ClassCastException |
| 12 | Predicate chaining | and(), or(), negate() for composition |
