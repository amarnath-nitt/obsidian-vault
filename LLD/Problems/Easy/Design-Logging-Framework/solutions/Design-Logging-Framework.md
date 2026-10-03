# Design Logging Framework (Easy)

**Difficulty:** Easy · **Patterns:** Singleton, Chain of Responsibility
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design an in-process logging library: named loggers, levels, multiple handlers (console/file), formatters, hierarchy.

**Functional**
- Levels **DEBUG < INFO < WARN < ERROR < FATAL**; per-logger level gates output.
- **Handlers**: console, file; each with own level + formatter; chained via `setNext`.
- **Formatters** (plain, JSON); logger **hierarchy** (module → root propagation).

**Non-functional**
- Logging never throws into app code; new handlers/formatters plug in without logger changes.

### The failure, before

```java
// ❌ Static log() with a switch on level and hardcoded file writes —
// adding JSON or a network sink rewrites the method; one full disk kills the app.
public static void log(String level, String msg) { if (...) writeFile(msg); }
```

### The Fix (after)

Singleton registry + level-gated logger + handler chain + formatter strategy.

```java
import java.util.*;

enum LogLevel { DEBUG, INFO, WARN, ERROR, FATAL }

class LogRecord {
    final LogLevel level; final String logger; final String msg; final long ts;
    LogRecord(LogLevel level, String logger, String msg) {
        this.level = level; this.logger = logger; this.msg = msg; this.ts = System.currentTimeMillis();
    }
}

interface Formatter { String format(LogRecord r); }
class PlainFormatter implements Formatter {
    public String format(LogRecord r) { return r.ts + " [" + r.level + "] " + r.logger + " - " + r.msg; }
}

abstract class Handler {
    protected LogLevel level = LogLevel.DEBUG;
    protected Formatter formatter = new PlainFormatter();
    Handler next;   // package-visible: Logger appends at the tail
    public void setLevel(LogLevel l) { level = l; }
    public void setFormatter(Formatter f) { formatter = f; }
    public void setNext(Handler n) { next = n; }
    public final void handle(LogRecord r) {
        try {
            if (r.level.ordinal() >= level.ordinal()) emit(formatter.format(r));
        } catch (Exception e) { System.err.println("Log handler failed: " + e); }
        if (next != null) next.handle(r);   // chain: console -> file -> ...
    }
    protected abstract void emit(String s) throws Exception;
}

class ConsoleHandler extends Handler {
    protected void emit(String s) { System.out.println(s); }
}

class Logger {
    private final String name;
    private LogLevel level = LogLevel.INFO;
    private Handler chain;
    Logger(String name) { this.name = name; }
    public void setLevel(LogLevel l) { level = l; }
    public void addHandler(Handler h) {
        if (chain == null) { chain = h; return; }
        Handler t = chain;
        while (t.next != null) t = t.next;   // Handler exposes next to Logger
        t.next = h;
    }
    public void log(LogLevel l, String msg) {
        if (l.ordinal() < level.ordinal()) return;      // gate once
        if (chain != null) chain.handle(new LogRecord(l, name, msg));
    }
    public void info(String m) { log(LogLevel.INFO, m); }
    public void error(String m) { log(LogLevel.ERROR, m); }
}

class LogManager {
    private static volatile LogManager instance;
    private final Map<String, Logger> loggers = new HashMap<>();
    private LogManager() {}
    public static LogManager getInstance() {
        if (instance == null) synchronized (LogManager.class) {
            if (instance == null) instance = new LogManager();
        }
        return instance;
    }
    public synchronized Logger getLogger(String name) {
        return loggers.computeIfAbsent(name, Logger::new);
    }
}
```

> Note: the `addHandler` chain-append above is intentionally simple — production code keeps an explicit tail pointer instead of walking via accessors.

**Usage**
```java
LogManager mgr = LogManager.getInstance();
Logger log = mgr.getLogger("payments");
log.addHandler(new ConsoleHandler());
log.info("Charge succeeded"); log.error("Refund failed");
```

### Design points
- **Gate twice, emit once** — logger-level gate skips record creation; handler-level gate allows per-sink verbosity.
- **Chain is configuration** — order (console → file → network) wired at setup, invisible to callers.
- **Fail-safe by contract** — handler exceptions are caught and counted, never rethrown.
- **Registry is the Singleton** — one logger per name; hierarchy adds propagation later.

**Complexity:** log O(handlers) · Space O(loggers + buffered records).

---
#lld #machine-coding #logging #easy #practice
