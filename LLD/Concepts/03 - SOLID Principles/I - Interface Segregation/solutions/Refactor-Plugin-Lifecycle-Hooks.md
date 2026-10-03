# Refactor Plugin Lifecycle Hooks (Interface Segregation)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Principle:** Interface Segregation
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-plugin-lifecycle-hooks)

### Problem

A plugin host defines one big `Plugin` interface with `init`, `start`, `stop`, `destroy`, and
`onError`. Most plugins only need one or two of these hooks, so they are forced to implement empty
stubs. Refactor into **focused interfaces** so a plugin depends only on what it uses.

### The Smell (before)

```java
// ❌ Fat interface — most implementers stub out methods they don't use
interface Plugin {
    void init();     void start();   void stop();
    void destroy();  void onError(Throwable t);
}

class MetricsPlugin implements Plugin {
    public void init()  { /* setup */ }
    public void start() {}      // noise
    public void stop()  {}      // noise
    public void destroy() {}    // noise
    public void onError(Throwable t) {}   // noise
}
```

### The Fix (after)

```java
// Focused, single-purpose interfaces
interface Initializable { void init(); }
interface Startable     { void start(); }
interface Stoppable     { void stop(); }
interface ErrorAware    { void onError(Throwable t); }

// A plugin implements only the hooks it actually supports
class MetricsPlugin implements Initializable, Startable, ErrorAware {
    public void init()  { System.out.println("Metrics init"); }
    public void start() { System.out.println("Metrics start"); }
    public void onError(Throwable t) { System.out.println("Metrics error: " + t.getMessage()); }
}

class OneShotPlugin implements Initializable {
    public void init() { System.out.println("One-shot init"); }
}

// The host drives each phase, checking for the capability it needs
class PluginHost {
    void boot(List<Object> plugins) {
        for (Object p : plugins) {
            if (p instanceof Initializable i) i.init();
            if (p instanceof Startable s)     s.start();
        }
    }
    void shutdown(List<Object> plugins) {
        for (Object p : plugins) if (p instanceof Stoppable s) s.stop();
    }
}
```

**Usage**
```java
PluginHost host = new PluginHost();
host.boot(List.of(new MetricsPlugin(), new OneShotPlugin()));
// Metrics init / Metrics start / One-shot init  — no empty stubs anywhere
```

### Design points
- **No forced methods** — `OneShotPlugin` never sees `start`/`stop`/`onError`.
- **Role interfaces** — each capability is its own contract.
- **Capability checks** — the host uses `instanceof` patterns to invoke only supported hooks.
- **Easier to implement** — a new plugin picks exactly the interfaces it needs.

**Complexity:** O(plugins) per phase · Space O(plugins)

---
#solid #isp #lld #practice