# Implement Email Builder

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Builder
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/implement-builder-email)

### Problem

Build an `Email` step by step. It has required fields (`to`, `subject`) and optional ones
(`cc`, `bcc` lists, `body`, attachments). A telescoping constructor would be unusable, so expose a
fluent **builder** whose `build()` validates the required fields and returns an immutable object.

### Approach

- Make `Email` immutable (`private final` fields, private constructor).
- Provide a static nested `Builder`; every setter returns `this`.
- Validate required fields in `build()`.

### Java Solution

```java
import java.util.*;

public final class Email {

    private final String to;
    private final String subject;
    private final String body;
    private final List<String> cc;
    private final List<String> bcc;
    private final List<String> attachments;

    private Email(Builder b) {
        this.to = b.to;
        this.subject = b.subject;
        this.body = b.body;
        this.cc = List.copyOf(b.cc);
        this.bcc = List.copyOf(b.bcc);
        this.attachments = List.copyOf(b.attachments);
    }

    public String to()                { return to; }
    public String subject()           { return subject; }
    public String body()              { return body; }
    public List<String> cc()          { return cc; }
    public List<String> bcc()         { return bcc; }
    public List<String> attachments() { return attachments; }

    public static Builder builder() { return new Builder(); }

    public static final class Builder {
        private String to, subject, body;
        private final List<String> cc = new ArrayList<>();
        private final List<String> bcc = new ArrayList<>();
        private final List<String> attachments = new ArrayList<>();

        public Builder to(String to)        { this.to = to; return this; }
        public Builder subject(String s)    { this.subject = s; return this; }
        public Builder body(String body)    { this.body = body; return this; }
        public Builder cc(String addr)      { cc.add(addr); return this; }
        public Builder bcc(String addr)     { bcc.add(addr); return this; }
        public Builder attach(String file)  { attachments.add(file); return this; }

        public Email build() {
            if (to == null || to.isBlank())           throw new IllegalStateException("to is required");
            if (subject == null || subject.isBlank()) throw new IllegalStateException("subject is required");
            return new Email(this);
        }
    }
}
```

**Usage**
```java
Email email = Email.builder()
        .to("alice@example.com")
        .cc("bob@example.com")
        .subject("Q3 report")
        .body("Please review the attached report.")
        .attach("q3.pdf")
        .build();
```

### Design points
- **Required vs optional** — only `to` / `subject` are validated; everything else is optional.
- **Immutability** — `List.copyOf` stops callers mutating the built email.
- **Fluent chain** — each method returns the builder, so the call reads top to bottom.

**Complexity:** O(n) to build · Space O(fields)

---
#builder #lld #practice