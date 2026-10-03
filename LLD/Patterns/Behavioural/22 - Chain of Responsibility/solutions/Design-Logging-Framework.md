# Design a Logging Framework

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Chain of Responsibility
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-logging-framework)

### Problem

A logging framework has multiple levels — **DEBUG**, **INFO**, **WARN**, **ERROR** — and multiple
output targets (console, file, alert). Each log line should be handled by the appropriate
handler(s), and handlers should be arranged in a chain so a request flows through until it is
handled.

### Approach — Chain of Responsibility

- **Handler** = `LogHandler` with a `next` link and `handle(level, message)`.
- **ConcreteHandlers** = `DebugHandler`, `InfoHandler`, `WarnHandler`, `ErrorHandler`.
- A console appender and/or a terminal handler ends the chain.

### Java Solution

```java
enum LogLevel { DEBUG, INFO, WARN, ERROR }

abstract class LogHandler {
    protected LogHandler next;
    LogHandler setNext(LogHandler next) { this.next = next; return next; }   // fluent linking

    /** Handle if this level applies, then always forward (impure chain / filter style). */
    void handle(LogLevel level, String message) {
        if (handles(level)) write(level, message);
        if (next != null) next.handle(level, message);
    }
    protected abstract boolean handles(LogLevel level);
    protected abstract void write(LogLevel level, String message);
}

class ConsoleHandler extends LogHandler {
    private final LogLevel threshold;
    ConsoleHandler(LogLevel threshold) { this.threshold = threshold; }
    protected boolean handles(LogLevel level) { return level.ordinal() >= threshold.ordinal(); }
    protected void write(LogLevel level, String message) {
        System.out.println("[console " + level + "] " + message);
    }
}
class FileHandler extends LogHandler {
    protected boolean handles(LogLevel level) { return level.ordinal() >= LogLevel.INFO.ordinal(); }
    protected void write(LogLevel level, String message) {
        System.out.println("[file " + level + "] " + message);   // pretend to append to a file
    }
}
class AlertHandler extends LogHandler {                          // terminal — errors only
    protected boolean handles(LogLevel level) { return level == LogLevel.ERROR; }
    protected void write(LogLevel level, String message) {
        System.out.println("🚨 ALERT: " + message);
    }
}
```

**Usage**
```java
LogHandler chain = new ConsoleHandler(LogLevel.DEBUG);
chain.setNext(new FileHandler()).setNext(new AlertHandler());

chain.handle(LogLevel.DEBUG, "cache warmed");     // console only
chain.handle(LogLevel.INFO,  "user signed in");    // console + file
chain.handle(LogLevel.ERROR, "disk full");         // console + file + alert
```

### Design points
- **Sender decoupled** — the caller submits to the head; it does not know which handlers run.
- **Composable** — thresholds and targets are configured by linking handlers.
- **Terminal handler** — `AlertHandler` (or a catch-all) ensures important lines are not dropped.

**Complexity:** O(handler chain length) per log line · Space O(handlers)

---
#chain-of-responsibility #logging #lld #practice