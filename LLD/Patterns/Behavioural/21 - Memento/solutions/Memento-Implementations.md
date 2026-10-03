# Memento — Implementations & Examples

**Pattern:** Memento (Behavioural) · **Skill:** snapshot & restore state without breaking encapsulation

### Approach

- Give the **Originator** a `save()` that returns an immutable **Memento** and a `restore(Memento)`.
- Keep the memento's state **private** (readable only by the originator).
- The **Caretaker** stores mementos in a stack/history and never inspects them.

### Java Solutions

**1. Text Editor Undo**
```java
final class EditorMemento {                        // opaque snapshot
    private final String state;
    EditorMemento(String state) { this.state = state; }
    private String state() { return state; }       // private → only the originator can read
}

class TextEditor {                                 // Originator
    private String content = "";

    void type(String words) { content += words; }
    String content() { return content; }

    EditorMemento save() { return new EditorMemento(content); }
    void restore(EditorMemento m) { content = m.state(); }
}

class History {                                    // Caretaker
    private final java.util.Deque<EditorMemento> stack = new java.util.ArrayDeque<>();
    void push(EditorMemento m) { stack.push(m); }
    EditorMemento pop() { return stack.poll(); }
    boolean isEmpty() { return stack.isEmpty(); }
}

// usage
TextEditor editor = new TextEditor();
History history = new History();
editor.type("Hello");
history.push(editor.save());
editor.type(", world");
System.out.println(editor.content());              // Hello, world
editor.restore(history.pop());
System.out.println(editor.content());              // Hello
```

**2. Undo / Redo (two stacks)**
```java
class VersionedDocument {
    private String state = "";

    static class Memento { private final String state; private Memento(String s) { state = s; } }

    void setState(String s) { state = s; }
    String state() { return state; }
    Memento save() { return new Memento(state); }
    void restore(Memento m) { state = m.state; }
}

class UndoManager {
    private final java.util.Deque<VersionedDocument.Memento> undo = new java.util.ArrayDeque<>();
    private final java.util.Deque<VersionedDocument.Memento> redo = new java.util.ArrayDeque<>();
    private final VersionedDocument doc;

    UndoManager(VersionedDocument doc) { this.doc = doc; }

    void commit() { undo.push(doc.save()); redo.clear(); }
    void undo()   { if (!undo.isEmpty()) { redo.push(doc.save()); doc.restore(undo.pop()); } }
    void redo()   { if (!redo.isEmpty()) { undo.push(doc.save()); doc.restore(redo.pop()); } }
}
```

**3. Game Checkpoint (deep snapshot)**
```java
final class GameMemento {
    private final int level, health, score;
    GameMemento(int level, int health, int score) { this.level = level; this.health = health; this.score = score; }
    int level()  { return level; }
    int health() { return health; }
    int score()  { return score; }
}
class Game {
    private int level = 1, health = 100, score = 0;
    void play() { score += 10; if (score % 50 == 0) { level++; health -= 10; } }
    GameMemento save() { return new GameMemento(level, health, score); }   // value copy → safe
    void restore(GameMemento m) { level = m.level(); health = m.health(); score = m.score(); }
}
```

**4. Bounded History (cap memory)**
```java
class BoundedHistory {
    private final java.util.Deque<EditorMemento> history = new java.util.ArrayDeque<>();
    private final int maxSize;
    BoundedHistory(int maxSize) { this.maxSize = maxSize; }
    void push(EditorMemento m) {
        if (history.size() == maxSize) history.removeLast();   // drop the oldest
        history.push(m);
    }
    EditorMemento pop() { return history.poll(); }
}
```

**5. Memento + Command (precise undo)**
```java
interface UndoableCommand { void execute(); void undo(); }

class TypeCommand implements UndoableCommand {
    private final TextEditor editor; private final String words; private EditorMemento before;
    TypeCommand(TextEditor editor, String words) { this.editor = editor; this.words = words; }
    public void execute() { before = editor.save(); editor.type(words); }   // snapshot first
    public void undo()    { editor.restore(before); }                       // restore on undo
}
```

**Complexity:** save/restore O(size of state) · Space O(history × state size)

**Design note:** making the memento's accessor **private** means only the originator can read it — the caretaker/receiver cannot inspect or mutate snapshots, preserving encapsulation.