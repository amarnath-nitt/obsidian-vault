# Design a Text Editor (Memento)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Memento
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-text-editor)

### Problem

A text editor supports typing and **undo/redo**. You must be able to restore the document to earlier
states without exposing its internal representation. Capture snapshots (**mementos**) at each step
and restore them on demand.

### Approach — Memento

- **Originator** = `TextEditor` — owns the content, `save()` returns a memento, `restore()` applies one.
- **Memento** = an immutable, opaque snapshot of the content.
- **Caretaker** = `History` — stores snapshots in undo/redo stacks, never inspects them.

### Java Solution

```java
import java.util.*;

final class TextEditor {                                    // Originator
    private final StringBuilder content = new StringBuilder();

    void type(String text) { content.append(text); }
    void delete(int chars) { content.delete(Math.max(0, content.length() - chars), content.length()); }
    String content()       { return content.toString(); }

    EditorMemento save() { return new EditorMemento(content.toString()); }
    void restore(EditorMemento m) {
        content.setLength(0);
        content.append(m.state());
    }

    /** Opaque snapshot — only the originator reads it. */
    static final class EditorMemento {
        private final String state;
        private EditorMemento(String state) { this.state = state; }
        private String state() { return state; }            // private → opaque to the caretaker
    }
}

class History {                                             // Caretaker
    private final Deque<TextEditor.EditorMemento> undo = new ArrayDeque<>();
    private final Deque<TextEditor.EditorMemento> redo = new ArrayDeque<>();
    private final TextEditor editor;

    History(TextEditor editor) { this.editor = editor; }

    /** Snapshot BEFORE a change, so it can be restored on undo. */
    void record() { undo.push(editor.save()); redo.clear(); }

    void undo() {
        if (undo.isEmpty()) return;
        redo.push(editor.save());               // snapshot current for redo
        editor.restore(undo.pop());
    }
    void redo() {
        if (redo.isEmpty()) return;
        undo.push(editor.save());
        editor.restore(redo.pop());
    }
}
```

**Usage**
```java
TextEditor editor = new TextEditor();
History history = new History(editor);

history.record(); editor.type("Hello");        // "Hello"
history.record(); editor.type(", world");      // "Hello, world"
history.record(); editor.delete(6);            // "Hello"

history.undo();                                 // "Hello, world"
history.undo();                                 // "Hello"
history.redo();                                 // "Hello, world"
System.out.println(editor.content());
```

### Design points
- **Encapsulation preserved** — the memento's only accessor is private to the originator.
- **Undo + redo** — two stacks move snapshots back and forth.
- **Immutable snapshots** — a memento is never mutated after creation.

### Alternative
A **Command**-based editor stores reversible operations (insert/delete) instead of whole-document
snapshots — cheaper for large documents with small edits.

**Complexity:** O(n) per snapshot/restore (document length) · Space O(history × n)

---
#memento #lld #practice