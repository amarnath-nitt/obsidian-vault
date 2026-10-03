# Design an ID Generator

**Source:** AlgoMaster · Low-Level Design Practice · **medium (premium)** · **Pattern:** Singleton
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-id-generator)

### Problem

Design an application-wide **unique ID generator**. Every component draws IDs from the same
generator, so numbers never repeat — even when requested concurrently. Construction is controlled:
there is exactly one generator per process.

### Approach

- A **singleton** instance (eager or Bill Pugh holder — no locking needed on the hot path).
- Back the counter with an **`AtomicLong`** so `incrementAndGet()` is atomic and lock-free.

### Java Solution

```java
import java.util.concurrent.atomic.AtomicLong;

public final class IdGenerator {

    private static final IdGenerator INSTANCE = new IdGenerator();   // eager → always safe

    private final AtomicLong counter = new AtomicLong(0);

    private IdGenerator() { }

    public static IdGenerator getInstance() { return INSTANCE; }

    public long nextId()                { return counter.incrementAndGet(); }
    public String nextId(String prefix) { return prefix + "-" + nextId(); }
    public long current()               { return counter.get(); }
    public void reset(long start)       { counter.set(start); }
}
```

**Usage**
```java
long   orderId   = IdGenerator.getInstance().nextId();        // 1, 2, 3, ...
String invoiceId = IdGenerator.getInstance().nextId("INV");   // INV-4, INV-5, ...
```

### Why `AtomicLong`
`counter++` is a read-modify-write and is **not** atomic — two threads can read the same value and
lose an update. `AtomicLong.incrementAndGet()` runs a **CAS loop**, so concurrent callers always get
distinct IDs without a global lock.

### Alternatives
- **Prefix + UUID** for non-sequential IDs: `prefix + "-" + UUID.randomUUID()`.
- **Snowflake-style** (timestamp + machine id + sequence) for distributed, time-sortable IDs.

**Complexity:** O(1) per ID · Space O(1)

---
#singleton #ids #lld #practice