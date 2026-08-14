# Exception Handling — Code Snippet Practice

Practice these "What does this code print?" questions for Exception Handling. Attempt each snippet before revealing the answer.

Related theory: [Core Java Interview Questions](Java Core/Core-Java-Interview-Questions.mdCore-Java-Interview-Questions.md)

---

## Snippet 1 — finally Overrides return 🟡

**What does this code print?**

```java
public class Main {
    static int getValue() {
        try {
            return 1;
        } catch (Exception e) {
            return 2;
        } finally {
            return 3;
        }
    }

    public static void main(String[] args) {
        System.out.println(getValue());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
3
```

**Explanation:**
- The `try` block executes `return 1`, but before actually returning, the `finally` block runs.
- The `finally` block has its own `return 3`, which **overrides** the return value from `try`.
- This is a well-known Java trap — `finally` can hijack the return value.
- **Best practice:** Never use `return` inside `finally`. It silently swallows the intended result and any exceptions.

**Common wrong answer:** "1" — forgetting that `finally` always runs before the method actually returns.

**Interview Tip:** "`finally` always executes before the method returns. A `return` in `finally` overrides the `return` from `try` or `catch`. Never return from `finally`."

</details>

---

## Snippet 2 — finally Runs Even After Exception 🟢

**What does this code print?**

```java
public class Main {
    public static void main(String[] args) {
        try {
            System.out.println("try");
            int result = 10 / 0;
            System.out.println("after division");
        } catch (ArithmeticException e) {
            System.out.println("catch");
        } finally {
            System.out.println("finally");
        }
        System.out.println("done");
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
try
catch
finally
done
```

**Explanation:**
- "try" prints, then `10 / 0` throws `ArithmeticException`.
- "after division" is **skipped** because the exception occurred before it.
- The `catch` block handles the exception → prints "catch".
- `finally` always runs → prints "finally".
- Since the exception was caught, execution continues → prints "done".

**Interview Tip:** "`finally` runs whether or not an exception occurs, and whether or not it's caught. Execution continues after `try-catch-finally` only if the exception was caught."

</details>

---

## Snippet 3 — Unreachable Catch Block 🟢

**Will this code compile?**

```java
import java.io.FileNotFoundException;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try {
            throw new FileNotFoundException("not found");
        } catch (IOException e) {
            System.out.println("IOException");
        } catch (FileNotFoundException e) {
            System.out.println("FileNotFoundException");
        }
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Compilation Error: Unreachable catch block for FileNotFoundException.
It is already handled by the catch block for IOException.
```

**Explanation:**
- `FileNotFoundException` extends `IOException`. The `catch (IOException)` block catches all `IOException` subclasses including `FileNotFoundException`.
- The second `catch (FileNotFoundException)` is **unreachable** — the compiler detects this and refuses to compile.
- **Rule:** Catch blocks must be ordered from **most specific to most general**.

**Fix:**
```java
catch (FileNotFoundException e) {    // specific first
    System.out.println("FileNotFoundException");
} catch (IOException e) {            // general second
    System.out.println("IOException");
}
```

**Interview Tip:** "Order catch blocks from most specific to most general. The compiler rejects unreachable catch blocks."

</details>

---

## Snippet 4 — try-with-resources Close Order 🟡

**What does this code print?**

```java
class ResourceA implements AutoCloseable {
    ResourceA() { System.out.println("Open A"); }
    @Override
    public void close() { System.out.println("Close A"); }
}

class ResourceB implements AutoCloseable {
    ResourceB() { System.out.println("Open B"); }
    @Override
    public void close() { System.out.println("Close B"); }
}

public class Main {
    public static void main(String[] args) {
        try (ResourceA a = new ResourceA();
             ResourceB b = new ResourceB()) {
            System.out.println("Using resources");
        }
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Open A
Open B
Using resources
Close B
Close A
```

**Explanation:**
- Resources are **opened** in declaration order: A first, then B.
- Resources are **closed** in **reverse** declaration order: B first, then A.
- This follows a **stack-like** (LIFO) pattern — the last opened is the first closed.
- This is similar to how you'd manually close resources in nested `finally` blocks.

**Common wrong answer:** "Close A, Close B" — not knowing the reverse-order closing rule.

**Interview Tip:** "try-with-resources closes in reverse declaration order (LIFO). This ensures dependent resources are closed safely."

</details>

---

## Snippet 5 — Exception in finally Swallows Original Exception 🔴

**What does this code print?**

```java
public class Main {
    public static void main(String[] args) {
        try {
            try {
                throw new RuntimeException("Original");
            } finally {
                throw new RuntimeException("From finally");
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
From finally
```

**Explanation:**
- The inner `try` throws "Original".
- Before propagating, the `finally` block runs and throws "From finally".
- The new exception from `finally` **replaces** the original exception — the original is lost.
- This is why throwing exceptions in `finally` is dangerous — it silently swallows the real error.
- In try-with-resources, Java handles this better with **suppressed exceptions**.

**Common wrong answer:** "Original" — not knowing that a `finally` exception replaces the original.

**Interview Tip:** "An exception thrown in `finally` replaces the original exception. Use try-with-resources for proper suppressed exception handling."

</details>

---

## Snippet 6 — Suppressed Exceptions in try-with-resources 🔴

**What does this code print?**

```java
class MyResource implements AutoCloseable {
    @Override
    public void close() {
        throw new RuntimeException("Close failed");
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            try (MyResource r = new MyResource()) {
                throw new RuntimeException("Body failed");
            }
        } catch (RuntimeException e) {
            System.out.println("Primary: " + e.getMessage());
            for (Throwable t : e.getSuppressed()) {
                System.out.println("Suppressed: " + t.getMessage());
            }
        }
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Primary: Body failed
Suppressed: Close failed
```

**Explanation:**
- The try body throws "Body failed".
- During automatic close, `close()` throws "Close failed".
- Unlike manual `finally`, try-with-resources does NOT lose the original exception.
- The close exception is added as a **suppressed exception** via `addSuppressed()`.
- You can retrieve suppressed exceptions with `getSuppressed()`.
- This is a major advantage of try-with-resources over manual `finally`.

**Interview Tip:** "try-with-resources preserves the primary exception and attaches close exceptions as suppressed. This is better than manual `finally` where the close exception replaces the original."

</details>

---

## Snippet 7 — Checked Exception From Lambda 🟡

**Will this code compile?**

```java
import java.util.List;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        List<String> paths = Arrays.asList("a.txt", "b.txt");

        paths.forEach(path -> {
            java.io.FileReader reader = new java.io.FileReader(path);
        });
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Compilation Error: Unhandled exception type FileNotFoundException
```

**Explanation:**
- `FileReader` constructor throws `FileNotFoundException` (a checked exception).
- The `Consumer<T>` functional interface (used by `forEach`) does NOT declare any checked exception in its `accept()` method.
- You cannot throw a checked exception from a lambda whose functional interface doesn't declare it.
- **Fixes:**
  1. Wrap in try-catch inside the lambda.
  2. Create a custom functional interface that declares the exception.
  3. Wrap the checked exception in an unchecked exception.

```java
paths.forEach(path -> {
    try {
        java.io.FileReader reader = new java.io.FileReader(path);
    } catch (java.io.FileNotFoundException e) {
        throw new RuntimeException(e);
    }
});
```

**Interview Tip:** "Standard functional interfaces don't declare checked exceptions. You must handle checked exceptions inside the lambda or wrap them as unchecked."

</details>

---

## Snippet 8 — StackOverflowError From Recursion 🟢

**What happens when this code runs?**

```java
public class Main {
    static void recurse() {
        recurse();
    }

    public static void main(String[] args) {
        try {
            recurse();
        } catch (StackOverflowError e) {
            System.out.println("Caught StackOverflowError");
        }
        System.out.println("Program continues");
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Caught StackOverflowError
Program continues
```

**Explanation:**
- `recurse()` calls itself infinitely, consuming stack frames until the thread stack is exhausted.
- JVM throws `StackOverflowError` (which extends `Error`, not `Exception`).
- `catch (StackOverflowError e)` catches it because `StackOverflowError` is a `Throwable`.
- Execution continues after the `try-catch`.
- **However:** Catching `Error` is generally a bad practice. Errors indicate serious JVM-level problems. This code works but is not recommended in production.

**Common wrong answer:** "Cannot catch StackOverflowError" — you CAN catch any `Throwable`, but you SHOULDN'T catch `Error` in most cases.

**Interview Tip:** "`StackOverflowError` is an `Error`, not an `Exception`. You can technically catch it, but you usually shouldn't because it indicates a fundamental issue like infinite recursion."

</details>

---

## Snippet 9 — finally With System.exit() 🟡

**What does this code print?**

```java
public class Main {
    public static void main(String[] args) {
        try {
            System.out.println("try");
            System.exit(0);
        } catch (Exception e) {
            System.out.println("catch");
        } finally {
            System.out.println("finally");
        }
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
try
```

**Explanation:**
- `System.exit(0)` terminates the JVM immediately.
- The `finally` block does **NOT** execute because the JVM is shutting down.
- This is one of the very few cases where `finally` does not run.
- Cases where `finally` won't run:
  1. `System.exit()` is called.
  2. JVM crashes.
  3. The thread running the try-finally is killed (daemon thread and JVM exits).
  4. Infinite loop or deadlock in `try` or `catch`.

**Common wrong answer:** "try, finally" — `System.exit()` kills the JVM before `finally` gets a chance.

**Interview Tip:** "`finally` always runs EXCEPT when `System.exit()` is called, the JVM crashes, or the thread is killed. These are rare but important edge cases."

</details>

---

## Snippet 10 — Multi-catch Cannot Catch Related Exceptions 🟡

**Will this code compile?**

```java
import java.io.IOException;
import java.io.FileNotFoundException;

public class Main {
    public static void main(String[] args) {
        try {
            throw new FileNotFoundException();
        } catch (FileNotFoundException | IOException e) {
            System.out.println("Caught");
        }
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Compilation Error: The exception FileNotFoundException is already caught
by the alternative IOException
```

**Explanation:**
- Multi-catch (`|`) cannot list exceptions where one is a subclass of the other.
- `FileNotFoundException` extends `IOException`, so catching `IOException` already covers `FileNotFoundException`.
- The compiler detects this redundancy and reports an error.
- **Fix:** Just catch `IOException` alone, which covers all its subclasses.

```java
catch (IOException e) {
    System.out.println("Caught");
}
```

**Interview Tip:** "Multi-catch alternatives must be disjoint — no parent-child relationships allowed. The compiler checks this."

</details>

---

## Quick Review Table

| # | Concept Tested | Key Rule |
|---|---|---|
| 1 | finally overrides return | `return` in `finally` replaces `try`/`catch` return |
| 2 | finally always runs | Runs after both normal and exceptional paths |
| 3 | Unreachable catch | Order from specific to general |
| 4 | try-with-resources close order | Closed in reverse (LIFO) order |
| 5 | Exception in finally | Replaces original exception silently |
| 6 | Suppressed exceptions | try-with-resources preserves both via `getSuppressed()` |
| 7 | Checked exception in lambda | Functional interfaces don't declare checked exceptions |
| 8 | StackOverflowError | Catchable but shouldn't be caught in production |
| 9 | System.exit in try | `finally` does NOT run after `System.exit()` |
| 10 | Multi-catch hierarchy | Cannot list parent-child exceptions together |
