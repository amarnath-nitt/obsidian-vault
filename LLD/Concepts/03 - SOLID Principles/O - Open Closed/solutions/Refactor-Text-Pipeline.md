# Refactor a Text Pipeline (Open/Closed)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Principle:** Open/Closed
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-text-pipeline)

### Problem

A text-processing pipeline applies a fixed set of transformations (trim, lowercase, remove
punctuation) hard-coded in one method. Adding a new step, or reordering steps, means editing the
pipeline. Refactor so steps can be **added and composed without modifying** the pipeline.

### The Smell (before)

```java
// ❌ Every new step edits this method
class TextPipeline {
    String process(String text, boolean trim, boolean lower, boolean stripPunct) {
        if (trim)       text = text.strip();
        if (lower)      text = text.toLowerCase();
        if (stripPunct) text = text.replaceAll("[^a-z0-9 ]", "");
        return text;
    }
    // adding "collapse spaces" means another boolean parameter and another if
}
```

### The Fix (after)

```java
import java.util.*;
import java.util.function.UnaryOperator;

// A step is any text transformation — composition over modification
@FunctionalInterface
interface TextStep extends UnaryOperator<String> {}

class TextPipeline {
    private final List<TextStep> steps = new ArrayList<>();

    /** Add a step; returns this for fluent composition. */
    TextPipeline then(TextStep step) { steps.add(step); return this; }

    String process(String text) {
        String result = text;
        for (TextStep step : steps) result = step.apply(result);   // never edited to add a step
        return result;
    }
}

// Reusable named steps
class Steps {
    static final TextStep TRIM          = String::strip;
    static final TextStep LOWERCASE     = String::toLowerCase;
    static final TextStep STRIP_PUNCT   = s -> s.replaceAll("[^a-z0-9 ]", "");
    static final TextStep COLLAPSE_SPACE = s -> s.replaceAll("\\s+", " ");
}
```

**Usage**
```java
TextPipeline pipeline = new TextPipeline()
        .then(Steps.TRIM)
        .then(Steps.LOWERCASE)
        .then(Steps.STRIP_PUNCT)
        .then(Steps.COLLAPSE_SPACE);       // a NEW step — TextPipeline untouched

pipeline.process("  Hello,   World!!  ");   // "hello world"
```

### Design points
- **Closed for modification** — `TextPipeline` is never edited to add a step.
- **Open for extension** — any `TextStep` (method reference or lambda) plugs in.
- **Composable** — steps are added in whatever order the caller wants.
- **Reusable** — named steps can be shared across pipelines.

**Complexity:** O(steps × text) per run · Space O(text)

---
#solid #ocp #lld #practice