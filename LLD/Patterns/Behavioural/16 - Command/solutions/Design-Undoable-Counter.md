# Design an Undoable Counter

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Command
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-undoable-counter)

### Problem

A counter can be incremented and decremented, and every operation must be **undoable** (and
redoable). Model each operation as an object so it can be stored in a history and reversed later.

### Approach — Command

- **Receiver** = `Counter` (holds the value).
- **Command** = `Command` with `execute()` / `undo()`.
- **Invoker** = `CommandManager` with undo/redo stacks.
- Concrete commands: `IncrementCommand`, `DecrementCommand`.

### Java Solution

```java
import java.util.*;

interface Command {
    void execute();
    void undo();
}

class Counter {                                           // Receiver
    private int value = 0;
    void increment() { value++; }
    void decrement() { value--; }
    int value() { return value; }
}

class IncrementCommand implements Command {
    private final Counter counter;
    IncrementCommand(Counter c) { this.counter = c; }
    public void execute() { counter.increment(); }
    public void undo()    { counter.decrement(); }         // exact inverse
}
class DecrementCommand implements Command {
    private final Counter counter;
    DecrementCommand(Counter c) { this.counter = c; }
    public void execute() { counter.decrement(); }
    public void undo()    { counter.increment(); }
}

class CommandManager {                                    // Invoker
    private final Deque<Command> undoStack = new ArrayDeque<>();
    private final Deque<Command> redoStack = new ArrayDeque<>();

    public void run(Command c) { c.execute(); undoStack.push(c); redoStack.clear(); }

    public void undo() {
        if (undoStack.isEmpty()) return;
        Command c = undoStack.pop();
        c.undo();
        redoStack.push(c);
    }
    public void redo() {
        if (redoStack.isEmpty()) return;
        Command c = redoStack.pop();
        c.execute();
        undoStack.push(c);
    }
}
```

**Usage**
```java
Counter counter = new Counter();
CommandManager manager = new CommandManager();

manager.run(new IncrementCommand(counter));   // 1
manager.run(new IncrementCommand(counter));   // 2
manager.run(new DecrementCommand(counter));   // 1

manager.undo();                               // 2
manager.undo();                               // 1
manager.redo();                               // 2
System.out.println(counter.value());          // 2
```

### Design points
- **Requests as objects** — each operation carries exactly the state needed to reverse itself.
- **Undo/redo stacks** — `undo` moves a command from undo to redo; `redo` does the opposite.
- **Invoker decoupled** — `CommandManager` never knows about `Counter` concretely.

### Alternative
A snapshot-based **Memento** approach could store counter values instead of inverse commands —
simpler for tiny state, heavier for large state.

**Complexity:** O(1) per operation · Space O(history)

---
#command #lld #practice