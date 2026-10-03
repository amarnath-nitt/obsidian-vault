# Implement a Report Builder

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Builder
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/implement-report-builder)

### Problem

Assemble a `Report` from a title, an ordered list of **sections**, an optional header/footer and an
output format. Sections are added incrementally and the report is rendered in the requested format.
Use the Builder pattern so construction is readable and validated.

### Approach

- Immutable `Report` produced by a fluent `Builder`.
- `addSection(heading, body)` appends in order.
- `build()` validates that a title and at least one section exist.
- A `render()` method turns the report into text using the chosen `Format`.

### Java Solution

```java
import java.util.*;

public final class Report {

    public enum Format { TEXT, MARKDOWN }

    public record Section(String heading, String body) {}

    private final String title;
    private final String header;
    private final String footer;
    private final Format format;
    private final List<Section> sections;

    private Report(Builder b) {
        this.title = b.title;
        this.header = b.header;
        this.footer = b.footer;
        this.format = b.format;
        this.sections = List.copyOf(b.sections);
    }

    public String render() {
        StringBuilder sb = new StringBuilder();
        if (header != null) sb.append(header).append("\n");
        sb.append(format == Format.MARKDOWN ? "# " + title : title).append("\n");
        for (Section s : sections) {
            sb.append(format == Format.MARKDOWN ? "## " + s.heading() : s.heading()).append("\n");
            sb.append(s.body()).append("\n");
        }
        if (footer != null) sb.append(footer).append("\n");
        return sb.toString();
    }

    public static Builder builder() { return new Builder(); }

    public static final class Builder {
        private String title, header, footer;
        private Format format = Format.TEXT;
        private final List<Section> sections = new ArrayList<>();

        public Builder title(String t)                { this.title = t; return this; }
        public Builder header(String h)               { this.header = h; return this; }
        public Builder footer(String f)               { this.footer = f; return this; }
        public Builder format(Format f)               { this.format = f; return this; }
        public Builder addSection(String h, String b) { sections.add(new Section(h, b)); return this; }

        public Report build() {
            if (title == null || title.isBlank()) throw new IllegalStateException("title is required");
            if (sections.isEmpty())               throw new IllegalStateException("at least one section is required");
            return new Report(this);
        }
    }
}
```

**Usage**
```java
Report report = Report.builder()
        .title("Quarterly Report")
        .format(Report.Format.MARKDOWN)
        .addSection("Revenue", "Up 12% QoQ")
        .addSection("Costs", "Down 3% QoQ")
        .footer("Confidential")
        .build();
System.out.println(report.render());
```

### Design points
- **Ordered sections** — the list preserves insertion order.
- **Validation in `build()`** — no half-built report can escape.
- **Format as a strategy** — swap rendering without touching the builder.

**Complexity:** O(sections) · Space O(content)

---
#builder #lld #practice