# Core Java, OOP, JVM, Collections, and Concurrency

This is the main Core Java interview guide. Study it in order, then use the focused code drills below to test active recall.

## Related Code Drills

- [OOP code snippets](../Practice/Code-Snippet-Practice/OOP-Code-Snippet-Practice.md)
- [Core Java code snippets](../Practice/Code-Snippet-Practice/Core-Java-Code-Snippet-Practice.md)
- [Collections code snippets](../Practice/Code-Snippet-Practice/Collections-Code-Snippet-Practice.md)
- [Exception-handling code snippets](../Practice/Code-Snippet-Practice/Exception-Handling-Code-Snippet-Practice.md)
- [Concurrency code snippets](../Practice/Code-Snippet-Practice/Java-Concurrency-Code-Snippet-Practice.md)
- [JVM and memory code snippets](../Practice/Code-Snippet-Practice/JVM-Memory-Code-Snippet-Practice.md)

## Object-Oriented Programming (OOP)

### 1. What are the four pillars of OOP?

**Answer:**
1. **Encapsulation**: Bundling data (variables) and methods that operate on the data into a single unit (class). It hides internal state and requires interaction through methods.
2. **Inheritance**: Mechanism where a new class inherits properties and behaviors from an existing class.
3. **Polymorphism**: Ability of objects to take multiple forms. Allows methods to do different things based on the object.
4. **Abstraction**: Hiding complex implementation details and showing only necessary features.

### 2. What is the difference between Abstraction and Encapsulation?

**Answer:**
- **Abstraction**: Focuses on *what* an object does. Hides complexity by showing only relevant information.
- **Encapsulation**: Focuses on *how* it achieves functionality. Hides internal state by bundling data and methods.

Example:
```java
// Abstraction - defining what to do
abstract class Vehicle {
    abstract void start();
}

// Encapsulation - hiding how it's done
class Car {
    private String engine; // Hidden
    
    public void startEngine() { // Public interface
        // Implementation hidden
    }
}
```

### 3. What is the difference between Abstract Class and Interface?

**Answer:**

| Abstract Class | Interface |
|---------------|-----------|
| Can have both abstract and concrete methods | All methods are abstract by default (before Java 8) |
| Can have instance variables | Only constants (public static final) |
| Can have constructors | Cannot have constructors |
| Supports single inheritance | Supports multiple inheritance |
| Use `extends` keyword | Use `implements` keyword |
| Can have any access modifier | Methods are public by default |

**When to use:**
- **Abstract Class**: When classes share common behavior and state
- **Interface**: When defining a contract for unrelated classes

### 4. What is method overloading and overriding?

**Answer:**

**Method Overloading (Compile-time Polymorphism):**
- Same method name, different parameters
- Happens in the same class
- Return type can be different

```java
class Calculator {
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
    int add(int a, int b, int c) { return a + b + c; }
}
```

**Method Overriding (Runtime Polymorphism):**
- Same method signature in parent and child class
- Happens across inheritance
- Return type must be same or covariant

```java
class Animal {
    void sound() { System.out.println("Animal makes sound"); }
}

class Dog extends Animal {
    @Override
    void sound() { System.out.println("Dog barks"); }
}
```

### 5. What is the diamond problem in Java? How does Java solve it?

**Answer:**
The diamond problem occurs in multiple inheritance when a class inherits from two classes that have a common ancestor, creating ambiguity.

Java solves this by:
- **Not allowing multiple inheritance with classes**
- **Allowing multiple inheritance with interfaces**
- **Using default methods in Java 8+** with explicit override requirement

```java
interface A {
    default void show() { System.out.println("A"); }
}

interface B {
    default void show() { System.out.println("B"); }
}

class C implements A, B {
    // Must override to resolve conflict
    @Override
    public void show() {
        A.super.show(); // Can call specific interface's method
    }
}
```

---

## Java Fundamentals

### 6. What is the difference between `==` and `.equals()`?

**Answer:**
- **`==`**: Compares **references** (memory addresses) for objects, **values** for primitives
- **`.equals()`**: Compares **content/values** of objects

```java
String s1 = new String("Hello");
String s2 = new String("Hello");
String s3 = "Hello";
String s4 = "Hello";

System.out.println(s1 == s2);        // false (different objects)
System.out.println(s1.equals(s2));   // true (same content)
System.out.println(s3 == s4);        // true (string pool)
```

### 7. What is String Pool in Java?

**Answer:**
String Pool is a special memory region in the heap where Java stores string literals to optimize memory usage through string interning.

```java
String s1 = "Hello";        // Goes to string pool
String s2 = "Hello";        // Reuses same reference from pool
String s3 = new String("Hello"); // Creates new object in heap

System.out.println(s1 == s2);        // true (same reference)
System.out.println(s1 == s3);        // false (different locations)
System.out.println(s1 == s3.intern()); // true (intern returns pool reference)
```

### 7b. What is the difference between a String literal and `new String()`?

**Answer:**

| Literal | `new String()` |
|---|---|
| **Storage** | Stored in the **String pool** | Stored in the **heap** (not pool) |
| **Reuse** | If same literal exists, **reuses** the pooled reference | Always creates a **new object** |
| **Memory** | More memory-efficient (shared) | Wastes memory if duplicates exist |
| **`==` comparison** | Two identical literals → `true` (same pool reference) | Two `new String("x")` → `false` (different heap objects) |

```java
String s1 = "Hello";              // String pool
String s2 = "Hello";              // Reuses same pool reference
System.out.println(s1 == s2);     // true (same object in pool)

String s3 = new String("Hello");  // New object in heap (NOT pool)
String s4 = new String("Hello");  // Another new object in heap
System.out.println(s3 == s4);     // false (different heap objects)
System.out.println(s3.equals(s4)); // true (same content)

// Interning to pull heap String into pool:
String s5 = s3.intern();           // Now points to pooled "Hello"
System.out.println(s1 == s5);     // true (both in pool)
```

This is one of the most frequently asked **questions** — interviewers test whether you understand the string pool mechanics.

### 8. Why is String immutable in Java?

**Answer:**
Strings are immutable for several reasons:
1. **Security**: Prevents modification of sensitive data like passwords, connection URLs
2. **Thread Safety**: No synchronization needed for concurrent access
3. **String Pool**: Enables safe string sharing and memory optimization
4. **Hashcode Caching**: Hashcode can be cached since value won't change
5. **Class Loading**: Class names are strings; immutability ensures integrity

### 9. What is the difference between String, StringBuilder, and StringBuffer?

**Answer:**

| Feature | String | StringBuilder | StringBuffer |
|---------|--------|---------------|--------------|
| Mutability | Immutable | Mutable | Mutable |
| Thread Safety | Thread-safe | Not thread-safe | Thread-safe (synchronized) |
| Performance | Slow for concatenation | Fastest | Slower than StringBuilder |
| When to Use | Few modifications | Single-threaded, many modifications | Multi-threaded, many modifications |

```java
// String - creates new objects
String str = "Hello";
str = str + " World"; // Creates new object

// StringBuilder - modifies same object
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World"); // Modifies existing object

// StringBuffer - synchronized
StringBuffer sbf = new StringBuffer("Hello");
sbf.append(" World"); // Thread-safe modification
```

### 10. What is the difference between `final`, `finally`, and `finalize()`?

**Answer:**
- **`final`**: Keyword for constants, preventing inheritance, or method overriding
  ```java
  final int MAX = 100;
  final class NoInheritance { }
  final void cannotOverride() { }
  ```

- **`finally`**: Block that always executes after try-catch, used for cleanup
  ```java
  try {
      // code
  } catch (Exception e) {
      // handle
  } finally {
      // always executes (cleanup)
  }
  ```

- **`finalize()`**: A legacy GC hook. It is deprecated for removal, non-deterministic, and must not be used for resource cleanup. Use `try-with-resources` and `AutoCloseable` for deterministic cleanup; use `Cleaner` only as a narrowly scoped safety net for rare native-resource cases. [JEP 421](https://openjdk.org/jeps/421)

---

## Collections Framework

### 11. What is the Java Collections Framework hierarchy?

**Answer:**
```
Collection (Interface)
├── List (Interface)
│   ├── ArrayList
│   ├── LinkedList
│   └── Vector
│       └── Stack
├── Set (Interface)
│   ├── HashSet
│   ├── LinkedHashSet
│   └── SortedSet (Interface)
│       └── TreeSet
└── Queue (Interface)
    ├── PriorityQueue
    └── Deque (Interface)
        └── ArrayDeque

Map (Interface)
├── HashMap
├── LinkedHashMap
├── Hashtable
└── SortedMap (Interface)
    └── TreeMap
```

### 12. What is the difference between ArrayList and LinkedList?

**Answer:**

| Feature | ArrayList | LinkedList |
|---------|-----------|------------|
| Internal Structure | Dynamic array | Doubly linked list |
| Access Time | O(1) - fast random access | O(n) - slow traversal needed |
| Insert/Delete (middle) | O(n) - shifting required | O(1) - just pointer changes |
| Insert/Delete (end) | O(1) amortized | O(1) |
| Memory | Less overhead | More (stores node references) |
| Best For | Reading/accessing | Frequent insertions/deletions |

```java
List<String> arrayList = new ArrayList<>();
arrayList.get(5); // O(1) - direct index access

List<String> linkedList = new LinkedList<>();
linkedList.get(5); // O(n) - must traverse from head
```

### 13. What is the difference between HashMap and HashTable?

**Answer:**

| Feature | HashMap | Hashtable |
|---------|---------|-----------|
| Thread Safety | Not synchronized | Synchronized |
| Null Keys/Values | Allows one null key, multiple null values | Doesn't allow null |
| Performance | Faster | Slower (synchronization overhead) |
| Since | Java 1.2 | Java 1.0 (legacy) |
| Iteration | Iterator (fail-fast) | Enumerator + Iterator |
| Modern Alternative | Use `ConcurrentHashMap` for thread safety | - |

```java
Map<String, Integer> hashMap = new HashMap<>();
hashMap.put(null, 1);  // OK
hashMap.put("key", null); // OK

Map<String, Integer> hashTable = new Hashtable<>();
hashTable.put(null, 1);  // NullPointerException
```

### 13b. What is the difference between `HashMap` and `ConcurrentHashMap`?

**Answer:**

| Feature | HashMap | ConcurrentHashMap |
|---|---|---|
| Thread Safety | Not thread-safe | Thread-safe |
| Locking | None | Bucket-level (Java 8+: CAS + synchronized on bins) |
| Null Keys/Values | Allows one null key, multiple null values | Neither keys nor values can be null |
| Performance | Fast (no locking overhead) | Slightly slower per op, but far better under concurrent load |
| Iterator | Fail-fast (throws `ConcurrentModificationException`) | Weakly consistent (no CME) |
| Use Case | Single-threaded or read-only after population | Concurrent reads/writes in multi-threaded apps |

```java
// HashMap — DO NOT share across threads without external synchronization
Map<String, Integer> map = new HashMap<>();

// ConcurrentHashMap — safe for concurrent access
Map<String, Integer> safeMap = new ConcurrentHashMap<>();
// safeMap.put(null, 1);  // NullPointerException!
```

### 13c. What is the difference between `HashMap` and `Collections.synchronizedMap(new HashMap<>())`?

**Answer:**

| Aspect                          | `Collections.synchronizedMap()`                                                                                                                    | `ConcurrentHashMap`                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Locking granularity**         | Single object-level lock wraps **every** method                                                                                                    | **Bucket-level** locking — different threads can operate on different buckets simultaneously                     |
| **Concurrency**                 | Effectively **serial** — only one thread can access the map at a time                                                                              | **Highly concurrent** — multiple threads read/write different buckets in parallel                                |
| **Iterator behavior**           | Iterator still throws `ConcurrentModificationException` during concurrent modification unless you manually synchronize on the map during iteration | **Weakly consistent** iterator — never throws CME, reflects the state at some point during or after construction |
| **Per-operation overhead**      | Lower                                                                                                                                              | Slightly higher (CAS, bin-level locking)                                                                         |
| **Throughput under contention** | **Poor** — becomes a bottleneck                                                                                                                    | **Excellent** — scales with number of cores                                                                      |

**Key insight:** `synchronizedMap` is a **legacy wrapper** that adds a single lock to every operation. It serializes ALL access. `ConcurrentHashMap` uses **fine-grained locking** (segmented in Java 7, CAS + bin-level `synchronized` in Java 8+) — only the specific bucket being modified is locked.

**Answer shape:** *"Always prefer `ConcurrentHashMap`. `synchronizedMap` is a legacy wrapper — avoid it because (a) it serializes all access and (b) its iterators are still not thread-safe for concurrent modification."*

### 13d. What is the difference between `HashMap` and `TreeMap`?

**Answer:**

| Feature | HashMap | TreeMap |
|---|---|---|
| Internal Structure | Hash table (array of buckets) | Red-Black tree (self-balancing BST) |
| Ordering | No guaranteed order | Sorted by keys (natural order or custom `Comparator`) |
| Null Keys/Values | Allows one null key, multiple null values | No null keys (can't compare null), allows null values (if natural ordering, but risky) |
| Time Complexity | O(1) average, O(n) worst case (hash collisions) | O(log n) for get/put/remove |
| Navigable methods | None | `firstKey()`, `lastKey()`, `floorKey()`, `ceilingKey()`, `higherKey()`, `lowerKey()` |
| Use Case | Fast lookup when order doesn't matter | Need sorted keys or range queries |

```java
Map<Integer, String> hashMap = new HashMap<>();
hashMap.put(3, "C"); hashMap.put(1, "A"); hashMap.put(2, "B");
// Iteration order: unpredictable (e.g., 1, 3, 2)

Map<Integer, String> treeMap = new TreeMap<>();
treeMap.put(3, "C"); treeMap.put(1, "A"); treeMap.put(2, "B");
// Iteration order: sorted (1, 2, 3)
// treeMap.ceilingKey(2) → 2
```

### 13e. What is the difference between `HashMap` and `LinkedHashMap`?

**Answer:**

| Feature | HashMap | LinkedHashMap |
|---|---|---|
| Internal Structure | Hash table | Hash table + doubly-linked list |
| Ordering | No guaranteed order | **Insertion order** (default) or **access order** (if constructed with `accessOrder=true`) |
| Null support | One null key, multiple null values | Same |
| Time Complexity | O(1) average | O(1) average (slight overhead for maintaining linked list) |
| Memory | Lower | Slightly higher (stores prev/next pointers) |
| Use Case | General-purpose, order doesn't matter | Need predictable iteration order, or LRU cache (with `accessOrder=true`) |

```java
Map<String, Integer> linkedHashMap = new LinkedHashMap<>();
linkedHashMap.put("Alice", 1);
linkedHashMap.put("Bob", 2);
linkedHashMap.put("Charlie", 3);
// Iteration order: Alice, Bob, Charlie (insertion order)

// LRU cache with access-order:
Map<String, Integer> lruCache = new LinkedHashMap<>(16, 0.75f, true);
// Setting accessOrder=true → entries accessed (get/put) move to the end
// Override removeEldestEntry() to evict when size exceeds threshold
```

### 14. How does HashMap work internally?

**Answer:**
HashMap uses an **array of buckets** with **hashing and chaining/tree structure**.

**Key Concepts:**
1. **Hashing**: `hashCode()` determines bucket index
2. **Bucket**: Each array position stores a linked list or tree of entries
3. **Collision**: Multiple keys with same hash go to same bucket
4. **Load Factor**: Default 0.75 - when to resize (capacity × load factor)
5. **Treeification**: Since Java 8, bucket converts to tree when entries > 8

**Process:**
```java
Map<String, Integer> map = new HashMap<>();
map.put("key", 100);

// 1. Calculate hash: hashCode() → hash compression
// 2. Find bucket: index = hash & (capacity - 1)
// 3. Check for existing key using equals()
// 4. If exists, replace value; else add new entry
// 5. If size > threshold, resize (double capacity)
```

### 15. What is the difference between HashSet and TreeSet?

**Answer:**

| Feature | HashSet | TreeSet |
|---------|---------|---------|
| Internal Structure | HashMap | Red-Black Tree (TreeMap) |
| Ordering | No order | Sorted (natural or comparator) |
| Null Elements | Allows one null | Doesn't allow null |
| Performance | O(1) add, remove, contains | O(log n) operations |
| Use Case | Fast operations, no order needed | Need sorted elements |

```java
Set<Integer> hashSet = new HashSet<>();
hashSet.add(3); hashSet.add(1); hashSet.add(2);
// Order: unpredictable [1, 2, 3] or [3, 1, 2]

Set<Integer> treeSet = new TreeSet<>();
treeSet.add(3); treeSet.add(1); treeSet.add(2);
// Order: sorted [1, 2, 3]
```

### 16. What is fail-fast and fail-safe iterators?

**Answer:**

**Fail-Fast Iterators:**
- Throws `ConcurrentModificationException` if collection is modified during iteration
- Used by: ArrayList, HashMap, HashSet
- Works on original collection

```java
List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C"));
for (String item : list) {
    list.remove(item); // ConcurrentModificationException
}
```

**Fail-Safe Iterators:**
- Doesn't throw exception, works on clone
- Used by: ConcurrentHashMap, CopyOnWriteArrayList
- May not reflect latest modifications

```java
CopyOnWriteArrayList<String> list = new CopyOnWriteArrayList<>(Arrays.asList("A", "B", "C"));
for (String item : list) {
    list.remove(item); // OK - works on copy
}
```

---

## Exception Handling

### 17. What is the difference between Checked and Unchecked Exceptions?

**Answer:**

**Checked Exceptions:**
- Checked at compile-time
- Must be handled with try-catch or declared with `throws`
- Extend `Exception` (but not `RuntimeException`)
- Examples: `IOException`, `SQLException`, `ClassNotFoundException`

**Unchecked Exceptions:**
- Checked at runtime
- No compilation requirement to handle
- Extend `RuntimeException`
- Examples: `NullPointerException`, `ArrayIndexOutOfBoundsException`, `IllegalArgumentException`

```java
// Checked - must handle
public void readFile() throws IOException {
    FileReader fr = new FileReader("file.txt");
}

// Unchecked - optional to handle
public void divide(int a, int b) {
    int result = a / b; // May throw ArithmeticException
}
```

### 18. What is the exception hierarchy in Java?

**Answer:**
```
Throwable
├── Error (Unchecked)
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── VirtualMachineError
└── Exception
    ├── IOException (Checked)
    ├── SQLException (Checked)
    ├── ClassNotFoundException (Checked)
    └── RuntimeException (Unchecked)
        ├── NullPointerException
        ├── ArrayIndexOutOfBoundsException
        ├── ArithmeticException
        └── IllegalArgumentException
```

### 19. Can we have multiple catch blocks? What is multi-catch?

**Answer:**

**Multiple catch blocks:** Yes, ordered from most specific to most general

```java
try {
    // code
} catch (FileNotFoundException e) {
    // Most specific
} catch (IOException e) {
    // More general
} catch (Exception e) {
    // Most general
}
```

**Multi-catch (Java 7+):** Handle multiple exceptions in one catch block

```java
try {
    // code
} catch (IOException | SQLException e) {
    // Handle both same way
    System.out.println(e.getMessage());
}
```

### 20. What is try-with-resources?

**Answer:**
Introduced in Java 7, automatically closes resources that implement `AutoCloseable` or `Closeable`.

**Before Java 7:**
```java
BufferedReader br = null;
try {
    br = new BufferedReader(new FileReader("file.txt"));
    // use br
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (br != null) {
        try {
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**With try-with-resources:**
```java
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    // use br
} catch (IOException e) {
    e.printStackTrace();
}
// br is automatically closed
```

---

## Multithreading & Concurrency

### 21. What are the different ways to create a thread?

**Answer:**

**1. Extending Thread class:**
```java
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread running");
    }
}

MyThread t = new MyThread();
t.start();
```

**2. Implementing Runnable interface:**
```java
class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Thread running");
    }
}

Thread t = new Thread(new MyRunnable());
t.start();
```

**3. Using Lambda (Java 8+):**
```java
Thread t = new Thread(() -> System.out.println("Thread running"));
t.start();
```

**4. Using Callable and Future:**
```java
Callable<Integer> task = () -> {
    return 123;
};

ExecutorService executor = Executors.newSingleThreadExecutor();
Future<Integer> future = executor.submit(task);
Integer result = future.get();
```

### 22. What is the difference between `start()` and `run()` methods?

**Answer:**
- **`start()`**: Creates a new thread and executes `run()` in that thread
- **`run()`**: Executes code in the current thread (no new thread created)

```java
Thread t = new Thread(() -> System.out.println("Running"));

t.start(); // Creates new thread, runs asynchronously
t.run();   // Runs in current thread, like a normal method call
```

### 23. What is synchronization? What are synchronized methods and blocks?

**Answer:**
Synchronization prevents multiple threads from accessing shared resources simultaneously, avoiding race conditions.

**Synchronized Method:**
```java
class Counter {
    private int count = 0;
    
    public synchronized void increment() {
        count++; // Only one thread can execute at a time
    }
}
```

**Synchronized Block:**
```java
class Counter {
    private int count = 0;
    private Object lock = new Object();
    
    public void increment() {
        synchronized(lock) {
            count++; // Only synchronized part is locked
        }
    }
}
```

**Static Synchronized Method:**
```java
class Counter {
    private static int count = 0;
    
    public static synchronized void increment() {
        count++; // Locks on Class object
    }
}
```

### 24. What is the difference between `wait()` and `sleep()`?

**Answer:**

| Feature | wait() | sleep() |
|---------|--------|---------|
| Purpose | Inter-thread communication | Pause execution |
| Lock Release | Releases monitor lock | Doesn't release lock |
| Class | Object class | Thread class |
| Wake Up | `notify()` or `notifyAll()` | After specified time |
| Synchronized | Must be in synchronized block | Can be called anywhere |

```java
synchronized(obj) {
    obj.wait();  // Releases lock, waits for notify
}

Thread.sleep(1000); // Pauses for 1 second, keeps lock
```

### 25. What is a deadlock? How to prevent it?

**Answer:**
**Deadlock:** Two or more threads waiting for each other to release locks, causing permanent blocking.

**Example:**
```java
// Thread 1
synchronized(lockA) {
    synchronized(lockB) { }
}

// Thread 2
synchronized(lockB) {
    synchronized(lockA) { } // Deadlock!
}
```

**Prevention:**
1. **Lock Ordering**: Always acquire locks in same order
2. **Lock Timeout**: Use `tryLock()` with timeout
3. **Deadlock Detection**: Monitor and detect cycles
4. **Avoid Nested Locks**: Minimize nested synchronization

```java
// Solution: Same order
synchronized(lockA) {
    synchronized(lockB) { }
}

synchronized(lockA) {
    synchronized(lockB) { } // Both acquire in same order
}
```

---

## JVM, Memory Management & Garbage Collection

### 26. Explain JVM architecture.

**Answer:**
```
┌─────────────────────────────────────┐
│      Class Loader Subsystem         │
│  (Loading, Linking, Initialization) │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│        Runtime Data Areas           │
│  ┌───────────────────────────────┐  │
│  │   Method Area (Metadata)      │  │
│  │   Heap (Objects)              │  │
│  │   Stack (Method Calls)        │  │
│  │   PC Registers                │  │
│  │   Native Method Stack         │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│       Execution Engine              │
│  ┌───────────────────────────────┐  │
│  │   Interpreter                 │  │
│  │   JIT Compiler                │  │
│  │   Garbage Collector           │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

### 27. What is the difference between Stack and Heap memory?

**Answer:**

| Feature | Stack | Heap |
|---------|-------|------|
| Storage | Primitive values, method calls, local references | Objects, instance variables |
| Access Speed | Faster | Slower |
| Size | Smaller | Larger |
| Lifetime | Exists until method returns | Until garbage collected |
| Thread | Each thread has own stack | Shared among all threads |
| Error | StackOverflowError | OutOfMemoryError |

```java
public void method() {
    int x = 10;           // Stack: primitive
    String str = "Hello"; // Stack: reference, Heap: "Hello" object
    Person p = new Person(); // Stack: reference, Heap: Person object
}
```

### 28. What is Garbage Collection? How does it work?

**Answer:**
Garbage Collection automatically frees memory by removing objects that are no longer referenced.

**Types of GC:**
1. **Serial GC**: Single-threaded, small applications
2. **Parallel GC**: Multi-threaded, throughput focused
3. **CMS (Concurrent Mark Sweep)**: Low latency
4. **G1 GC**: Balanced, large heaps (default since Java 9)
5. **ZGC & Shenandoah**: Ultra-low latency (Java 11+)

**GC Process:**
1. **Mark**: Identify live objects
2. **Sweep**: Remove unreferenced objects
3. **Compact**: Defragment memory (optional)

**Making object eligible for GC:**
```java
Person p = new Person();
p = null; // Now eligible for GC

// Or
p = new Person(); // Old object eligible for GC
```

### 29. What are the different memory generations in heap?

**Answer:**
```
Heap Memory
├── Young Generation
│   ├── Eden Space (new objects)
│   ├── Survivor Space S0
│   └── Survivor Space S1
└── Old Generation (Tenured)
    └── Long-lived objects

Separate: Metaspace (Class metadata) - Not in heap
```

**Process:**
1. New objects → Eden
2. Minor GC → Survivors (S0 ↔ S1)
3. After multiple Minor GCs → Old Generation
4. Major GC → Old Generation cleanup

### 30. What is the difference between `==` for comparing objects vs primitives?

**Answer:**
- **Primitives**: Compares actual values
- **Objects**: Compares memory references

```java
// Primitives
int a = 5;
int b = 5;
System.out.println(a == b); // true (same value)

// Objects
Integer x = new Integer(5);
Integer y = new Integer(5);
System.out.println(x == y);        // false (different objects)
System.out.println(x.equals(y));   // true (same value)

// Autoboxing cache (-128 to 127)
Integer m = 100;
Integer n = 100;
System.out.println(m == n);        // true (from cache)

Integer p = 200;
Integer q = 200;
System.out.println(p == q);        // false (outside cache)
```

### 30b. What is the difference between `int` and `Integer`? When do you use each?

**Answer:**

| `int` | `Integer` |
|---|---|
| **Type** | Primitive (8 bytes raw value) | Wrapper class (object) |
| **Value** | Always a value | Can be `null` |
| **Memory** | Stored on stack (or in object fields on heap) | Stored on heap (object overhead) |
| **Collections** | Cannot be stored in collections directly | Can be stored in `List<Integer>`, `Map`, etc. |
| **Auto-boxing** | N/A | `Integer x = 5;` (auto-converted from `int`) |
| **Performance** | Faster (no object allocation) | Slower (object allocation + GC) |
| **Use Case** | Counters, calculations, local variables | Collection elements, nullable values, method parameters requiring objects |

```java
// int → Integer (autoboxing)
Integer boxed = 42;          // compiler does: new Integer(42)
int unboxed = boxed;         // auto-unboxing: boxed.intValue()

// This is a classic Coforge trap — the integer cache:
Integer a = 127;
Integer b = 127;
System.out.println(a == b);   // true (cached: -128 to 127)

Integer c = 128;
Integer d = 128;
System.out.println(c == d);   // false (cache only covers -128 to 127!)
System.out.println(c.equals(d)); // true (always use .equals for objects)

// Null handling
Integer nullable = null;
// int cannotBeNull = nullable; // NullPointerException at unboxing!
```

**Key insight:** `==` compares references for `Integer` objects — the cache (-128 to 127) makes it *look* like value comparison, but it breaks for values outside the cache range. **Always use `.equals()` for object comparison.**

---

## Additional Questions To Add Next

Use these to expand the note after the first 30 questions are comfortable.

### Easy

31. What is the difference between a class and an object?
32. What is a constructor, and can it be overloaded?
33. What is the difference between instance variables, local variables, and static variables?
34. What is the difference between `public`, `private`, `protected`, and default access?
35. What is autoboxing and unboxing?
36. What is a wrapper class?
37. What is the difference between `break`, `continue`, and `return`?
38. What is the difference between an array and an `ArrayList`?

### Medium

39. Why must `equals()` and `hashCode()` be overridden together?
40. What happens when two different keys have the same hash code in a `HashMap`?
41. What is the difference between `Comparable` and `Comparator`?
42. What is the difference between shallow copy and deep copy?
43. What is immutability, and how do you create an immutable class?
44. What is the difference between `throw` and `throws`?
45. What is the difference between `ExecutorService`, `Callable`, and `Future`?
46. What is the difference between `volatile` and `synchronized`?

### Hard

47. Explain the Java Memory Model in interview-friendly terms.
48. How would you design a thread-safe singleton?
49. What are race conditions, and how can they be prevented?
50. What is the difference between optimistic and pessimistic locking?
51. How does `ConcurrentHashMap` work at a high level?
52. How would you debug a memory leak in Java?
53. How would you investigate high CPU usage in a Java service?
54. How would you choose between G1, ZGC, and Parallel GC?
55. What are virtual threads, and where do they help?
56. What is structured concurrency?
57. What are scoped values, and how are they different from `ThreadLocal`?
58. What are sequenced collections?
59. What changed in Java 21, Java 25 LTS, and Java 26?
60. How would you migrate a Java 8 or Java 11 service to Java 21/25?
61. What can go wrong when frameworks mutate `final` fields using reflection?
62. How would you use JFR to debug latency, allocation, or lock contention?

## Quick Answer Framework

For every question, practice answering in this shape:

1. **Definition:** one direct sentence.
2. **Why it matters:** performance, safety, readability, or correctness.
3. **Example:** one small Java example or real interview scenario.
4. **Trade-off:** when not to use it or what can go wrong.
