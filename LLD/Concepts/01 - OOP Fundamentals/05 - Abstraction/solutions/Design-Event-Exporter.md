# Design Event Exporter (Abstraction)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Topic:** Abstraction
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-event-exporter)

### Problem

Design an event exporter that can render a list of events in different formats (JSON, CSV, plain
text). Callers should work through a common **abstraction** and pick a format at runtime, without a
`switch` over formats inside the calling code.

### Approach

- Define an abstract `EventExporter` with `export(events)` and `formatName()`.
- Concrete exporters implement the rendering.
- A factory/registry picks the exporter by name (keeps selection out of the caller).

### Java Solution

```java
import java.util.*;

public record Event(long timestamp, String type, String detail) {}

// Abstraction
public abstract class EventExporter {
    public abstract String formatName();
    public abstract String export(List<Event> events);
}

class JsonExporter extends EventExporter {
    public String formatName() { return "json"; }
    public String export(List<Event> events) {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < events.size(); i++) {
            Event e = events.get(i);
            if (i > 0) sb.append(",");
            sb.append("{\"ts\":").append(e.timestamp())
              .append(",\"type\":\"").append(e.type())
              .append("\",\"detail\":\"").append(e.detail()).append("\"}");
        }
        return sb.append("]").toString();
    }
}

class CsvExporter extends EventExporter {
    public String formatName() { return "csv"; }
    public String export(List<Event> events) {
        StringBuilder sb = new StringBuilder("timestamp,type,detail\n");
        for (Event e : events) {
            sb.append(e.timestamp()).append(",").append(e.type()).append(",").append(e.detail()).append("\n");
        }
        return sb.toString();
    }
}

class PlainExporter extends EventExporter {
    public String formatName() { return "plain"; }
    public String export(List<Event> events) {
        StringBuilder sb = new StringBuilder();
        for (Event e : events) sb.append(e.timestamp()).append(" ").append(e.type()).append(": ").append(e.detail()).append("\n");
        return sb.toString();
    }
}

// Selection lives here, not in the caller
class ExporterFactory {
    private static final Map<String, EventExporter> EXPORTERS = Map.of(
        "json",  new JsonExporter(),
        "csv",   new CsvExporter(),
        "plain", new PlainExporter()
    );
    static EventExporter of(String format) {
        EventExporter e = EXPORTERS.get(format.toLowerCase());
        if (e == null) throw new IllegalArgumentException("Unknown format: " + format);
        return e;
    }
}
```

**Usage**
```java
List<Event> events = List.of(new Event(1, "login", "alice"), new Event(2, "logout", "alice"));
System.out.println(ExporterFactory.of("csv").export(events));
System.out.println(ExporterFactory.of("json").export(events));
```

### Design points
- **Abstraction** — the caller sees only `EventExporter`.
- **No `switch` in callers** — a registry resolves the format.
- **Open/Closed** — add an `XmlExporter` without editing existing code.

**Complexity:** O(events) per export · Space O(output)

---
#oop #abstraction #lld #practice