# Proxy — Implementations & Examples

**Pattern:** Proxy (Structural) · **Skill:** controlling access to an object

### Approach

- Define a **Subject** interface.
- Implement the **RealSubject** (the real work).
- Implement a **Proxy** with the same interface that controls access and (usually) delegates.

### Java Solutions

**1. Virtual (Lazy) Proxy — Image**
```java
interface Image { void display(); }

class RealImage implements Image {
    private final String file;
    RealImage(String file) { this.file = file; load(); }
    private void load() { System.out.println("Loading " + file + " from disk (expensive)"); }
    public void display() { System.out.println("Displaying " + file); }
}

class ImageProxy implements Image {
    private final String file;
    private RealImage real;                          // lazily created
    ImageProxy(String file) { this.file = file; }
    public void display() {
        if (real == null) real = new RealImage(file); // load only on first use
        real.display();
    }
}
```

**2. Protection Proxy — Bank Account**
```java
interface BankAccount { void withdraw(double amount); }

class RealBankAccount implements BankAccount {
    private double balance = 1000;
    public void withdraw(double amount) {
        if (amount > balance) { System.out.println("Insufficient funds"); return; }
        balance -= amount;
        System.out.println("Withdrew " + amount + ", balance " + balance);
    }
}

class ProtectionProxy implements BankAccount {
    private final BankAccount real;
    private final String role;
    ProtectionProxy(BankAccount real, String role) { this.real = real; this.role = role; }
    public void withdraw(double amount) {
        if (!"ADMIN".equals(role)) { System.out.println("Access denied for role " + role); return; }
        real.withdraw(amount);
    }
}
```

**3. Caching Proxy**
```java
import java.util.*;

interface DataService { String get(String key); }

class DbService implements DataService {
    public String get(String key) { System.out.println("DB hit for " + key); return "value-" + key; }
}
class CachingProxy implements DataService {
    private final DataService real;
    private final Map<String, String> cache = new HashMap<>();
    CachingProxy(DataService real) { this.real = real; }
    public String get(String key) {
        if (cache.containsKey(key)) { System.out.println("Cache hit for " + key); return cache.get(key); }
        String value = real.get(key);
        cache.put(key, value);
        return value;
    }
}
```

**4. Thread-Safe Lazy Proxy**
```java
class SafeLazyProxy implements DataService {
    private final String key;
    private volatile DbService real;
    SafeLazyProxy(String key) { this.key = key; }
    public String get(String k) {
        if (real == null) {
            synchronized (this) {
                if (real == null) real = new DbService();
            }
        }
        return real.get(k);
    }
}
```

**5. Dynamic Proxy (JDK) — logging**
```java
import java.lang.reflect.*;

DataService loggingProxy = (DataService) Proxy.newProxyInstance(
    DataService.class.getClassLoader(),
    new Class<?>[]{ DataService.class },
    (proxyObj, method, args) -> {
        System.out.println("→ calling " + method.getName() + " with " + java.util.Arrays.toString(args));
        Object result = method.invoke(new DbService(), args);
        System.out.println("← returned " + result);
        return result;
    });

loggingProxy.get("user:42");
```

**Complexity:** O(1) overhead per delegated call (plus the actual work) · Space O(1)

**Real-world tie-in:** Spring uses dynamic proxies to implement `@Transactional`, `@Cacheable`, `@Async`, and method-security — all proxy-based cross-cutting concerns.