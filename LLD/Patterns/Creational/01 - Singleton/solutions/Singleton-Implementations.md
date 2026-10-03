# Singleton — Implementations & Hardening

**Pattern:** Singleton (Creational) · **Skill:** thread safety, lazy init, reflection & serialisation safety

### Approach

- **Eager** — instance built at class load; simplest, always safe, no laziness.
- **Double-Checked Locking** — lazy; needs `volatile` to avoid publishing a partially-built object.
- **Bill Pugh Holder** — lazy + lock-free; JVM guarantees single holder initialisation. **Recommended.**
- **Enum** — serialisation- and reflection-safe; the most robust one-liner.

### Java Solutions

**1. Eager**
```java
public class EagerSingleton {
    private static final EagerSingleton INSTANCE = new EagerSingleton();
    private EagerSingleton() {}
    public static EagerSingleton getInstance() { return INSTANCE; }
}
```

**2. Double-Checked Locking**
```java
public class LazySingleton {
    private static volatile LazySingleton instance;
    private LazySingleton() {}
    public static LazySingleton getInstance() {
        if (instance == null) {
            synchronized (LazySingleton.class) {
                if (instance == null) instance = new LazySingleton();
            }
        }
        return instance;
    }
}
```

**3. Bill Pugh Holder (recommended)**
```java
public class HolderSingleton {
    private HolderSingleton() {}
    private static class Holder { static final HolderSingleton INSTANCE = new HolderSingleton(); }
    public static HolderSingleton getInstance() { return Holder.INSTANCE; }
}
```

**4. Enum (robust)**
```java
public enum EnumSingleton {
    INSTANCE;
    public void doWork() { /* ... */ }
}
```

**5. Reflection-proof construction guard**
```java
public class SafeSingleton {
    private static final SafeSingleton INSTANCE = new SafeSingleton();
    private SafeSingleton() {
        if (INSTANCE != null) throw new IllegalStateException("Use getInstance()");
    }
    public static SafeSingleton getInstance() { return INSTANCE; }
}
```

**6. Serialisation-safe (`readResolve`)**
```java
public class SerializableSingleton implements java.io.Serializable {
    private static final SerializableSingleton INSTANCE = new SerializableSingleton();
    private SerializableSingleton() {}
    public static SerializableSingleton getInstance() { return INSTANCE; }
    private Object readResolve() { return INSTANCE; }   // keeps single instance on deserialise
}
```

**Complexity:** Time O(1) per `getInstance()` · Space O(1) (one instance)

**Note:** a Singleton is *per JVM* — it does not survive clustering or multiple processes. In production, prefer Dependency Injection and treat the "single instance" as a container-scoped bean.