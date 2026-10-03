# Design Alert Preview (Dependency)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Relationship:** Dependency
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-alert-preview)

### Problem

Design an alert preview that renders a short, safe preview of a message. Rendering needs a
**formatter**, but the preview does not **own** or store the formatter — it merely **uses** it while
producing the preview. This temporary "uses-a" link is a **dependency**.

### Approach — Dependency

- `AlertPreview` has no formatter field.
- The formatter is passed into the method, used, and discarded.
- `AlertPreview` depends on the `Formatter` abstraction only during the call.

### Java Solution

```java
public interface Formatter {
    String format(String message);
}

class PlainFormatter implements Formatter {
    public String format(String message) { return message; }
}
class UpperCaseFormatter implements Formatter {
    public String format(String message) { return message.toUpperCase(); }
}
class TruncatingFormatter implements Formatter {
    private final int max;
    TruncatingFormatter(int max) { this.max = max; }
    public String format(String message) {
        return message.length() <= max ? message : message.substring(0, max) + "…";
    }
}

public class AlertPreview {

    /**
     * `formatter` is a DEPENDENCY: it is used for this call only and never stored.
     * AlertPreview does not own the formatter and has no field for it.
     */
    public String preview(String message, Formatter formatter) {
        String formatted = formatter.format(message);
        return "🔔 " + formatted;
    }
}
```

**Usage**
```java
AlertPreview preview = new AlertPreview();
preview.preview("Deployment finished", new PlainFormatter());       // "🔔 Deployment finished"
preview.preview("Deployment finished", new UpperCaseFormatter());   // "🔔 DEPLOYMENT FINISHED"
preview.preview("A very long alert message", new TruncatingFormatter(10)); // "🔔 A very long…"
```

### Why Dependency (not Association)
- **No stored reference** — `AlertPreview` has no `Formatter` field.
- **Call-scoped** — the formatter is supplied per call and released afterwards.
- **Weakest coupling** — swap or mock the formatter freely; the preview is unaffected.

### Dependency vs Association
If `AlertPreview` stored the formatter in a field and used it across many calls, it would be an
**association** (it would "know" the formatter). Passing it as a parameter keeps it a **dependency**.

**Complexity:** O(message length) per preview · Space O(1)

---
#oop #dependency #lld #practice