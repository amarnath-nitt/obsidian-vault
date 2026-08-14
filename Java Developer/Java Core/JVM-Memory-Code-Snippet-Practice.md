# JVM & Memory — Code Snippet Practice

Practice these "What does this code print?" questions for JVM internals, memory management, and garbage collection. Attempt each snippet before revealing the answer.

Related theory: [Core Java Interview Questions](Java Core/Core-Java-Interview-Questions.mdCore-Java-Interview-Questions.md)

---

## Snippet 1 — StackOverflowError From Recursion 🟢

**What happens when this code runs?**

```java
public class Main {
    static int depth = 0;

    static void recurse() {
        depth++;
        recurse();
    }

    public static void main(String[] args) {
        try {
            recurse();
        } catch (StackOverflowError e) {
            System.out.println("Stack overflow at depth: " + depth);
        }
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Stack overflow at depth: <some large number, e.g., 10000-30000>
```

**Explanation:**
- Each method call creates a new **stack frame** on the thread's stack.
- The thread stack has a finite size (default ~512KB-1MB depending on JVM).
- Infinite recursion exhausts the stack → `StackOverflowError`.
- The exact depth depends on stack size (`-Xss`), frame size (local variables), and JVM implementation.
- `StackOverflowError` extends `Error`, not `Exception`. You can catch it, but the stack is nearly exhausted.
- **Production:** Avoid deep recursion. Use iterative approaches or tail-call optimization (not natively supported in Java).

**Interview Tip:** "Each thread gets its own stack. `StackOverflowError` means the stack is exhausted from too many nested method calls. Set stack size with `-Xss`."

</details>

---

## Snippet 2 — OutOfMemoryError From Unbounded Growth 🟡

**What happens when this code runs?**

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<byte[]> leaks = new ArrayList<>();
        int count = 0;

        try {
            while (true) {
                leaks.add(new byte[1024 * 1024]); // 1 MB each
                count++;
            }
        } catch (OutOfMemoryError e) {
            System.out.println("OOM after " + count + " allocations");
        }
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
OOM after <N> allocations (depends on heap size)
Example with -Xmx256m: OOM after ~245 allocations
```

**Explanation:**
- Each iteration allocates 1 MB that is **retained** (referenced by the list).
- GC cannot collect these objects because they're all reachable.
- Eventually the heap is exhausted → `OutOfMemoryError: Java heap space`.
- **Common OOM causes in production:**
  - Unbounded caches
  - Listener/callback leaks
  - Large result sets loaded entirely into memory
  - ThreadLocal values not cleaned up
- **Diagnose:** Use `-XX:+HeapDumpOnOutOfMemoryError` to generate a heap dump on OOM.

**Interview Tip:** "`OutOfMemoryError: Java heap space` means the heap is full and GC can't reclaim enough memory. Objects are reachable and cannot be collected."

</details>

---

## Snippet 3 — Static Field Memory Leak Pattern 🟡

**What is the memory problem in this code?**

```java
import java.util.*;

public class EventBus {
    private static final List<Object> listeners = new ArrayList<>();

    public static void register(Object listener) {
        listeners.add(listener);
    }

    // No unregister method!
}

class OrderService {
    OrderService() {
        EventBus.register(this);
    }

    void processOrder() {
        // business logic
    }
}

public class Main {
    public static void main(String[] args) {
        for (int i = 0; i < 100000; i++) {
            OrderService service = new OrderService();
            service.processOrder();
            // service goes out of scope, but...
        }
    }
}
```

<details>
<summary>Answer</summary>

**Answer: Memory Leak — all 100,000 OrderService objects are never garbage collected.**

**Explanation:**
- Each `OrderService` registers itself with `EventBus.register(this)`.
- The static `listeners` list holds a reference to every `OrderService` instance.
- Even though `service` goes out of scope in the loop, the `listeners` list still references it.
- GC cannot collect any of them → memory grows unboundedly → eventual OOM.
- **This is the classic Java memory leak pattern:** a long-lived collection (static field, singleton cache, listener registry) holding references to short-lived objects.
- **Fix:** Add an `unregister()` method, use `WeakReference`, or use weak listener patterns.

```java
public static void unregister(Object listener) {
    listeners.remove(listener);
}
```

**Interview Tip:** "Java memory leaks happen when objects are unintentionally kept reachable. Common culprits: static collections, unclosed resources, ThreadLocal values, and listener registrations without cleanup."

</details>

---

## Snippet 4 — String.intern() and Memory 🟡

**What does this code demonstrate?**

```java
public class Main {
    public static void main(String[] args) {
        String s1 = new String("hello");
        String s2 = new String("hello");

        System.out.println(s1 == s2);

        String s3 = s1.intern();
        String s4 = s2.intern();

        System.out.println(s3 == s4);
        System.out.println(s1 == s3);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
false
true
false
```

**Explanation:**
- `s1` and `s2` are two separate heap objects → `s1 == s2` is `false`.
- `s1.intern()` returns the pool reference for "hello". `s2.intern()` returns the same pool reference → `s3 == s4` is `true`.
- `s1` is still the heap object, `s3` is the pool reference → `s1 == s3` is `false`.
- **Memory implication:** Interning avoids duplicate String objects in memory. Useful for frequently repeated strings (e.g., country codes, status values).
- **Warning:** Over-interning can cause memory issues in older JVMs where the string pool was in PermGen (fixed-size). In Java 7+, the pool is in the heap.
- From Java 9+, String uses **compact strings** (byte[] with Latin-1 or UTF-16 encoding) to save memory further.

**Interview Tip:** "String pool is in the heap since Java 7. `intern()` saves memory for repeated strings but overuse can cause GC pressure on the pool."

</details>

---

## Snippet 5 — Class Loading and Static Initialization Order 🔴

**What does this code print?**

```java
class Parent {
    static {
        System.out.println("Parent static block");
    }

    {
        System.out.println("Parent instance block");
    }

    Parent() {
        System.out.println("Parent constructor");
    }
}

class Child extends Parent {
    static {
        System.out.println("Child static block");
    }

    {
        System.out.println("Child instance block");
    }

    Child() {
        System.out.println("Child constructor");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("--- First object ---");
        Child c1 = new Child();
        System.out.println("--- Second object ---");
        Child c2 = new Child();
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Parent static block
Child static block
--- First object ---
Parent instance block
Parent constructor
Child instance block
Child constructor
--- Second object ---
Parent instance block
Parent constructor
Child instance block
Child constructor
```

**Explanation:**
- **Class loading phase** (once per class, parent first):
  1. Parent static block
  2. Child static block
- Note: Static blocks run when the class is first loaded, which happens before `main()` prints "--- First object ---" because the JVM loads `Child` (and its parent `Parent`) when it first encounters `new Child()`.
- Actually, static blocks run before the first object creation. The JVM class-loads `Child` before executing the constructor.
- **Instance creation phase** (every `new`, parent before child):
  1. Parent instance initializer → Parent constructor
  2. Child instance initializer → Child constructor
- Second `new Child()`: static blocks DON'T run again. Only instance blocks and constructors run.

**Initialization order:**
1. Static blocks (parent → child, once only)
2. Instance initializer blocks (parent → child, per object)
3. Constructors (parent → child, per object)

**Interview Tip:** "Static init runs once at class load (parent first). Instance init + constructor run per object (parent first). This is the complete Java initialization order."

</details>

---

## Snippet 6 — Stack vs Heap Allocation 🟢

**Where does each variable live?**

```java
public class Main {
    static int classVar = 100;          // Line A

    public static void main(String[] args) {
        int localPrimitive = 42;        // Line B
        String localRef = "Hello";      // Line C
        int[] array = new int[5];       // Line D
        Object obj = new Object();      // Line E
    }
}
```

<details>
<summary>Answer</summary>

**Answer:**

| Line | Variable | Where Variable Lives | Where Value/Object Lives |
|---|---|---|---|
| A | `classVar` | Method area (class metadata) | Value `100` is directly in method area |
| B | `localPrimitive` | Stack | Value `42` is directly on the stack |
| C | `localRef` | Stack (reference) | `"Hello"` object is in Heap (string pool) |
| D | `array` | Stack (reference) | `int[5]` array object is in Heap |
| E | `obj` | Stack (reference) | `Object` instance is in Heap |

**Explanation:**
- **Stack** stores: local primitive values, local reference variables (the pointer, not the object).
- **Heap** stores: all objects and arrays. This includes String pool objects (since Java 7).
- **Method area** (Metaspace in Java 8+) stores: class metadata, static fields, constant pool.
- Each thread has its own stack. The heap and metaspace are shared across all threads.
- **Key insight:** `localRef` (the reference pointer) is on the stack. The `String` object it points to is on the heap.

**Interview Tip:** "Primitives and references live on the stack. Objects and arrays live on the heap. Static fields are in metaspace. Each thread has its own stack, but all threads share the heap."

</details>

---

## Snippet 7 — Garbage Collection Eligibility 🟡

**After which line are objects eligible for GC?**

```java
public class Main {
    public static void main(String[] args) {
        Object a = new Object();    // Obj1
        Object b = new Object();    // Obj2
        Object c = a;               // c -> Obj1

        a = null;                   // Line 1
        b = null;                   // Line 2
        c = null;                   // Line 3

        System.gc();                // request GC (no guarantee)
    }
}
```

<details>
<summary>Answer</summary>

**Answer:**

| After Line | GC-Eligible Objects |
|---|---|
| Line 1 (`a = null`) | None — Obj1 is still referenced by `c` |
| Line 2 (`b = null`) | Obj2 — no references remain |
| Line 3 (`c = null`) | Obj1 — now no references remain |

**Explanation:**
- An object becomes eligible for GC when **no live references** point to it (it becomes unreachable from any GC root).
- After Line 1: `a` is null, but `c` still references Obj1 → NOT eligible.
- After Line 2: `b` is null, and Obj2 has no other references → eligible.
- After Line 3: `c` is null, and Obj1 has no other references → eligible.
- `System.gc()` is only a **request** — the JVM may or may not run GC.

**GC Roots include:** local variables, static fields, active threads, JNI references.

**Interview Tip:** "An object is GC-eligible when it's unreachable from all GC roots. Multiple references must all be cleared. `System.gc()` is a hint, not a command."

</details>

---

## Snippet 8 — finalize() Is Unreliable 🟡

**What does this code print?**

```java
public class Main {
    @Override
    protected void finalize() throws Throwable {
        System.out.println("finalize called");
    }

    public static void main(String[] args) {
        Main obj = new Main();
        obj = null;
        System.gc();
        System.out.println("After gc request");

        // Wait a moment for finalizer thread
        try { Thread.sleep(500); } catch (InterruptedException e) {}
        System.out.println("Done");
    }
}
```

<details>
<summary>Answer</summary>

**Output (non-deterministic):**
```
After gc request
finalize called
Done

OR

After gc request
Done
finalize called

OR

After gc request
Done
(finalize may never run)
```

**Explanation:**
- This is a legacy demonstration only. Finalization timing is unpredictable and applications must not depend on it.
- `System.gc()` is a hint. The JVM may not run GC immediately (or at all).
- Even if GC runs, the finalizer thread runs asynchronously — no guaranteed order relative to `main`.
- `Object.finalize()` has long been deprecated, and finalization was deprecated for removal in JDK 18. Modern JDKs can disable it; never use it for application cleanup. [JEP 421](https://openjdk.org/jeps/421)
- **Problems with finalize():**
  - Non-deterministic timing
  - May never run
  - Performance overhead (2 GC cycles to reclaim)
  - Can resurrect objects (bad pattern)
  - Security risk
- **Modern alternatives:** `try-with-resources` with `AutoCloseable` for deterministic cleanup. `Cleaner` is only a last-resort safety net for rare native-resource integrations.

**Interview Tip:** "Never rely on finalization. Model a resource as `AutoCloseable` and clean it up with `try-with-resources`; a `Cleaner` is not a replacement for deterministic cleanup."

</details>

---

## Quick Review Table

| # | Concept Tested | Key Rule |
|---|---|---|
| 1 | StackOverflowError | Thread stack exhausted from deep recursion |
| 2 | OutOfMemoryError | Heap exhausted from retained objects |
| 3 | Static field memory leak | Long-lived collections holding short-lived objects |
| 4 | String.intern() | Returns pool reference, saves memory for duplicates |
| 5 | Class initialization order | Static (parent→child, once) → Instance (parent→child, per object) |
| 6 | Stack vs Heap | Primitives/references on stack, objects on heap |
| 7 | GC eligibility | No live references → eligible |
| 8 | Finalization | Legacy only; use `AutoCloseable` and try-with-resources |
