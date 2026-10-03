# Singleton Pattern — Concept

## What Is It?

**Singleton** guarantees that a class has **exactly one instance** and provides a **global point of access** to it. It is the most-asked design pattern in LLD interviews, mostly because there are many ways to implement it — and interviewers want to hear you discuss **thread safety** and **lazy vs eager** initialisation.

---

## When to Use

> **Trigger keywords:** "single instance", "one shared", "global", "config", "manager", "logger", "cache", "registry", "connection pool"

| Trigger | Real Example |
|---------|--------------|
| A **single shared resource** | Connection pool, thread pool |
| **Global config / registry** | `AppConfig`, `ServiceRegistry` |
| **Central logger / audit trail** | `Logger` |
| **A cache with one owner** | `CacheManager` |
| **A coordinating manager** | `ParkingLotManager` in a single-process simulation |

---

## Variants

### 1. Eager Initialisation
Instance created at class-load time — simple, always thread-safe, no laziness.
```java
public class EagerSingleton {
    private static final EagerSingleton INSTANCE = new EagerSingleton();
    private EagerSingleton() {}
    public static EagerSingleton getInstance() { return INSTANCE; }
}
```

### 2. Lazy (DCL) — Double-Checked Locking
Lazy + thread-safe; needs `volatile` to prevent a partially-constructed object escaping.
```java
public class LazySingleton {
    private static volatile LazySingleton instance;
    private LazySingleton() {}
    public static LazySingleton getInstance() {
        if (instance == null) {                     // first check (no lock)
            synchronized (LazySingleton.class) {
                if (instance == null)               // second check (with lock)
                    instance = new LazySingleton();
            }
        }
        return instance;
    }
}
```

### 3. Bill Pugh (Holder) — Recommended
Lazy, thread-safe, no synchronisation cost. The JVM guarantees the holder is initialised once, on first access.
```java
public class HolderSingleton {
    private HolderSingleton() {}
    private static class Holder { static final HolderSingleton INSTANCE = new HolderSingleton(); }
    public static HolderSingleton getInstance() { return Holder.INSTANCE; }
}
```

### 4. Enum Singleton — Simplest & Most Robust
Serialisation-safe and reflection-safe by the JVM.
```java
public enum EnumSingleton {
    INSTANCE;
    public void doWork() { /* ... */ }
}
```

---

## Visual Walkthrough

```
                 getInstance()
Thread A ─────────────────────►  instance == null?  ──► acquire lock
                                                          │
                                                          ▼
                                                   instance == null? ──► create
Thread B ─────────────────────►  instance != null  ──► return same object
```

Key point: **the constructor must be private**, otherwise anyone can `new` a second instance.

---

## Trade-offs / Comparison

| Variant | Lazy | Thread-safe | Serialisation-safe | Reflection-safe |
|---------|------|-------------|--------------------|-----------------|
| Eager | ❌ | ✅ | ❌ (unless `readResolve`) | ❌ |
| Double-Checked Locking | ✅ | ✅ (needs `volatile`) | ❌ | ❌ |
| Bill Pugh Holder | ✅ | ✅ | ❌ | ❌ |
| Enum | ✅ | ✅ | ✅ | ✅ |

---

## Common Mistakes

1. **Forgetting `volatile`** in double-checked locking → a half-initialised object can be published.
2. **Not making the constructor private** → callers create extra instances.
3. **Overusing Singleton** → hidden global state, hard to test. Prefer **Dependency Injection**.
4. **Breaking it with reflection / serialisation** → use an `enum`, or `readResolve()`, or a guard in the constructor.
5. **Using it for caching in a distributed system** → "one instance per JVM", not per cluster.

---

## Related Patterns

- [[../02 - Factory Method/Concept|Factory Method]] — controls *why* objects are created; Singleton controls *how many*
- [[../../../Concepts/03 - SOLID Principles/00 - Index|SOLID]] — Singleton can violate SRP/DI; use sparingly

---

#singleton #creational #lld #concept