# Repair a Document Contract (Liskov Substitution)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Principle:** Liskov Substitution
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/repair-document-contract)

### Problem

A `Document` base class promises that `save()` persists changes, and `setContent()` mutates content.
A `ReadOnlyDocument` subclass rejects `save()` and `setContent()` by throwing — so any code written
against `Document` breaks when handed a read-only document. Repair the hierarchy.

### The Smell (before)

```java
// ❌ Base promises mutate + save; ReadOnly subclass breaks both
abstract class Document {
    abstract void setContent(String content);
    abstract void save();
    abstract String content();
}

class ReadOnlyDocument extends Document {
    private final String content;
    ReadOnlyDocument(String content) { this.content = content; }
    public String content() { return content; }
    public void setContent(String content) { throw new UnsupportedOperationException(); } // LSP break
    public void save()                     { throw new UnsupportedOperationException(); } // LSP break
}

void edit(Document doc) {
    doc.setContent("new");     // 💥 throws for a read-only document
    doc.save();
}
```

### The Fix (after)

Split the **read** contract from the **write** contract; promise only what every subtype supports.

```java
interface ReadableDocument {
    String content();
}

interface EditableDocument extends ReadableDocument {   // adds the write capability
    void setContent(String content);
    void save();
}

class ReadOnlyDocument implements ReadableDocument {
    private final String content;
    ReadOnlyDocument(String content) { this.content = content; }
    public String content() { return content; }           // only promises reading
}

class EditableTextDocument implements EditableDocument {
    private String content;
    EditableTextDocument(String content) { this.content = content; }
    public String content()              { return content; }
    public void setContent(String c)     { content = c; }
    public void save()                   { System.out.println("Saved: " + content); }
}

// Now only accepts documents that genuinely support editing
void edit(EditableDocument doc) {
    doc.setContent("new");     // safe — the type guarantees it
    doc.save();
}
```

### Design points
- **Honest contracts** — `ReadableDocument` declares only reading; editing is a separate role.
- **Substitutability** — every `EditableDocument` *is* a `ReadableDocument` and behaves correctly.
- **Compile-time safety** — `edit(...)` can no longer be handed a read-only document.
- **Preconditions not strengthened** — no subtype rejects a legal base-class operation.

**Complexity:** O(1) per operation · Space O(content)

---
#solid #lsp #lld #practice