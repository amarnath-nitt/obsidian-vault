# Design a Shared Counter

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Singleton
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-shared-counter)

### Problem (contract)

Turn `Counter` into a **thread-safe singleton**:

- `getInstance()` returns one controlled, thread-safe instance; no second instance can be built.
- `int increment()` adds one and returns the new value.
- `int getCount()` returns the current count.
- `void reset()` sets the count to `0` **without replacing** the singleton object.

A provided driver (`CounterGate`) obtains two handles via two separate `getInstance()` calls and
expects `sameInstance()` to be `true`, with increments through one handle visible through the other.
The driver must not be modified.

### Approach

- Private constructor + safely published static instance.
- Guard all access to the single `count` field with `synchronized`.
- `reset()` changes only the **value** — never the stored instance reference.

### Java Solution

```java
public final class Counter {

    private static volatile Counter instance;

    private int count = 0;

    private Counter() { }

    public static Counter getInstance() {
        if (instance == null) {
            synchronized (Counter.class) {
                if (instance == null) {
                    instance = new Counter();
                }
            }
        }
        return instance;
    }

    public synchronized int increment() { return ++count; }
    public synchronized int getCount()  { return count; }
    public synchronized void reset()    { count = 0; }   // value only
}
```

### Driver (provided — do not modify)
```java
class CounterGate {
    private final Counter a = Counter.getInstance();
    private final Counter b = Counter.getInstance();

    CounterGate() { Counter.getInstance().reset(); }

    boolean sameInstance() { return a == b; }   // true
    int incrementA()       { return a.increment(); }
    int readB()            { return b.getCount(); }
}
```

### Key design points
- **Stable identity** — `reset()` must not null out `instance`, or the two handles diverge.
- **One lock for all state** — `increment` / `getCount` / `reset` must guard the *same* monitor so increments are never lost.

**Complexity:** O(1) per operation · Space O(1)

---
#singleton #concurrency #lld #practice