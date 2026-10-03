# Implement Log Formatter Decorators

**Source:** AlgoMaster · Low-Level Design Practice · **medium (premium)** · **Pattern:** Decorator
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

A logging system formats each message before it is written. Formatting steps — **timestamp**,
**log level**, **JSON wrapping**, **redaction** — should be composable in any order and any
combination, each transforming the message.

### Approach — Decorator

- **Component** = `LogFormatter` (`format(message)` → `String`).
- **ConcreteComponent** = `PlainFormatter` (identity).
- **Decorator** = abstract `FormatterDecorator`.
- **ConcreteDecorators** = `TimestampFormatter`, `LevelFormatter`, `JsonFormatter`, `Redactor`.

### Java Solution

```java
import java.time.LocalTime;

// Component
interface LogFormatter {
    String format(String level, String message);
}

// ConcreteComponent
class PlainFormatter implements LogFormatter {
    public String format(String level, String message) { return message; }
}

// Decorator base
abstract class FormatterDecorator implements LogFormatter {
    protected final LogFormatter inner;
    protected FormatterDecorator(LogFormatter inner) { this.inner = inner; }
    public String format(String level, String message) { return inner.format(level, message); }
}

// Concrete decorators — each transforms the inner result
class TimestampFormatter extends FormatterDecorator {
    TimestampFormatter(LogFormatter f) { super(f); }
    public String format(String level, String message) {
        return "[" + LocalTime.now().withNano(0) + "] " + super.format(level, message);
    }
}
class LevelFormatter extends FormatterDecorator {
    LevelFormatter(LogFormatter f) { super(f); }
    public String format(String level, String message) {
        return level.toUpperCase() + " " + super.format(level, message);
    }
}
class JsonFormatter extends FormatterDecorator {
    JsonFormatter(LogFormatter f) { super(f); }
    public String format(String level, String message) {
        return "{\"level\":\"" + level + "\",\"msg\":\"" + super.format(level, message) + "\"}";
    }
}
class Redactor extends FormatterDecorator {
    private final String secret;
    Redactor(LogFormatter f, String secret) { super(f); this.secret = secret; }
    public String format(String level, String message) {
        return super.format(level, message.replace(secret, "***"));
    }
}
```

**Usage — compose any order**
```java
LogFormatter formatter = new JsonFormatter(
        new TimestampFormatter(
                new Redactor(new PlainFormatter(), "hunter2")));

System.out.println(formatter.format("info", "login ok"));
// {"level":"info","msg":"[12:30:05] login ok"}
```

### Design points
- **Order matters** — `JsonFormatter(Timestamp(...))` wraps the timestamped text as JSON.
- **Redaction is a decorator** — cross-cutting concern kept out of the core formatter.
- **Composable** — any subset/order builds a tailored formatter.

**Complexity:** O(depth) per message · Space O(1)

---
#decorator #logging #lld #practice