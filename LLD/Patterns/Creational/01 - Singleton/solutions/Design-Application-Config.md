# Design an Application Config

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Singleton
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-application-config)

### Problem

A single configuration object is shared across a whole application. Two unrelated components that
ask for the config must receive **the same instance**, so a value written by one is immediately
visible to the other. Construction from outside the class must not be possible, and the shared
state must stay correct under concurrent access.

### Approach

- Make the constructor **private** and expose a static `getInstance()`.
- Publish the instance safely (double-checked locking + `volatile`, or a holder).
- Store settings in a **`ConcurrentHashMap`** so reads and writes are thread-safe.

### Java Solution

```java
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public final class AppConfig {                          // Singleton

    private static volatile AppConfig instance;          // lazily published

    private final Map<String, String> settings = new ConcurrentHashMap<>();

    private AppConfig() { }                              // blocks external `new`

    public static AppConfig getInstance() {
        if (instance == null) {                          // 1st check (no lock)
            synchronized (AppConfig.class) {
                if (instance == null) {                  // 2nd check (with lock)
                    instance = new AppConfig();
                }
            }
        }
        return instance;
    }

    public void set(String key, String value) { settings.put(key, value); }
    public String get(String key)             { return settings.getOrDefault(key, ""); }
    public boolean has(String key)            { return settings.containsKey(key); }
    public void reset()                       { settings.clear(); }   // value only
}
```

**Usage**
```java
AppConfig.getInstance().set("region", "eu-west-1");
String region = AppConfig.getInstance().get("region");   // same object → "eu-west-1"
```

### Why it works
- **Private constructor** blocks `new AppConfig()` everywhere else.
- **`volatile` + double-checked locking** guarantees exactly one instance under concurrency.
- **`ConcurrentHashMap`** protects the settings map without a coarse lock.

### Alternatives
- **Bill Pugh holder** — lazy, lock-free: `private static class Holder { static final AppConfig I = new AppConfig(); }`.
- **Enum singleton** — `enum AppConfig { INSTANCE; ... }` — serialisation/reflection safe.

**Complexity:** O(1) access · Space O(keys)

---
#singleton #lld #practice