# Design a Text Formatter

**Source:** AlgoMaster · Low-Level Design Practice · **easy (premium)** · **Pattern:** Template Method
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

Formatting text is a fixed pipeline — **read → normalise → transform → wrap → write** — but the
transform and wrap steps differ per formatter (e.g. Markdown vs HTML). Enforce the pipeline in a base
class and let each formatter fill in the varying steps.

### Approach — Template Method

- `TextFormatter` defines the `final` `format(text)` pipeline.
- `normalise()` / `wrap()` are abstract (or hook) steps.
- Concrete formatters (Markdown, Html, Plain) override only the differing steps.

### Java Solution

```java
abstract class TextFormatter {
    // Template method — fixed pipeline
    final String format(String input) {
        String normalised = normalise(input);
        String transformed = transform(normalised);
        String wrapped = wrap(transformed);
        return write(wrapped);
    }

    // Shared default step (can be overridden)
    protected String normalise(String text) {
        return text.strip().replaceAll("\\s+", " ");      // trim + collapse spaces
    }

    // Abstract steps — must be supplied by subclasses
    protected abstract String transform(String text);
    protected abstract String wrap(String text);

    // Hook — default writes the result unchanged
    protected String write(String text) { return text; }
}

class MarkdownFormatter extends TextFormatter {
    protected String transform(String text) { return text.replace("**", "##"); }
    protected String wrap(String text)      { return "# " + text; }
}

class HtmlFormatter extends TextFormatter {
    protected String transform(String text) { return text.replace("&", "&amp;"); }
    protected String wrap(String text)      { return "<p>" + text + "</p>"; }
    @Override protected String write(String text) { return text; }
}

class PlainFormatter extends TextFormatter {
    protected String transform(String text) { return text; }
    protected String wrap(String text)      { return text; }
}
```

**Usage**
```java
System.out.println(new MarkdownFormatter().format("  hello   world  "));  // # hello world
System.out.println(new HtmlFormatter().format("Tom & Jerry"));            // <p>Tom &amp; Jerry</p>
```

### Design points
- **Pipeline fixed** — `format` is `final`; subclasses cannot skip or reorder steps.
- **Varying steps abstract** — `transform`/`wrap` are the formatter-specific parts.
- **Shared default reused** — `normalise` has a common implementation subclasses can override.

**Complexity:** O(n) in the text length · Space O(n)

---
#template-method #lld #practice