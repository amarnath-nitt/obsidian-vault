# Command — Implementations & Examples

**Pattern:** Command (Behavioural) · **Skill:** encapsulating requests for undo, queue & log

### Approach

- Define a **Command** interface (`execute` / `undo`).
- Each **ConcreteCommand** holds a **Receiver** plus any parameters and stores undo state.
- An **Invoker** triggers commands without knowing the Receiver.

### Java Solutions

**1. Remote Control with Undo**
```java
interface Command { void execute(); void undo(); }

class Light {                                          // Receiver
    private boolean on = false;
    void on()  { on = true;  System.out.println("Light ON"); }
    void off() { on = false; System.out.println("Light OFF"); }
}

class LightOnCommand implements Command {
    private final Light light;
    LightOnCommand(Light light) { this.light = light; }
    public void execute() { light.on(); }
    public void undo()    { light.off(); }
}
class LightOffCommand implements Command {
    private final Light light;
    LightOffCommand(Light light) { this.light = light; }
    public void execute() { light.off(); }
    public void undo()    { light.on(); }
}

class RemoteControl {                                  // Invoker
    private Command last;
    public void press(Command c) { c.execute(); last = c; }
    public void pressUndo()      { if (last != null) last.undo(); }
}
```

**2. Text Editor Undo/Redo (command history)**
```java
import java.util.*;

interface TextCommand { void execute(); void undo(); }

class TextEditor {
    private final StringBuilder text = new StringBuilder();
    void insert(int pos, String s) { text.insert(pos, s); }
    void delete(int pos, int len)  { text.delete(pos, pos + len); }
    String content() { return text.toString(); }
    int length() { return text.length(); }
}

class InsertCommand implements TextCommand {
    private final TextEditor editor; private final int pos; private final String s;
    InsertCommand(TextEditor e, int pos, String s) { editor = e; this.pos = pos; this.s = s; }
    public void execute() { editor.insert(pos, s); }
    public void undo()    { editor.delete(pos, s.length()); }
}

class CommandManager {                                 // Invoker + history
    private final Deque<TextCommand> undoStack = new ArrayDeque<>();
    private final Deque<TextCommand> redoStack = new ArrayDeque<>();
    void run(TextCommand c) { c.execute(); undoStack.push(c); redoStack.clear(); }
    void undo() { if (!undoStack.isEmpty()) { TextCommand c = undoStack.pop(); c.undo(); redoStack.push(c); } }
    void redo() { if (!redoStack.isEmpty()) { TextCommand c = redoStack.pop(); c.execute(); undoStack.push(c); } }
}
```

**3. Macro Command (batch)**
```java
import java.util.*;

class MacroCommand implements Command {
    private final List<Command> commands = new ArrayList<>();
    public MacroCommand add(Command c) { commands.add(c); return this; }
    public void execute() { commands.forEach(Command::execute); }
    public void undo()    {                                   // reverse order!
        for (int i = commands.size() - 1; i >= 0; i--) commands.get(i).undo();
    }
}
```

**4. Job Queue (enqueue & execute later)**
```java
import java.util.concurrent.*;

class JobQueue {
    private final BlockingQueue<Command> queue = new LinkedBlockingQueue<>();
    private final ExecutorService worker = Executors.newSingleThreadExecutor();

    JobQueue() {
        worker.submit(() -> {
            while (!Thread.currentThread().isInterrupted()) {
                Command c = queue.take();          // blocks until a job arrives
                c.execute();
            }
        });
    }
    void submit(Command c) { queue.offer(c); }
    void shutdown() { worker.shutdownNow(); }
}
```

**5. Undoable Drawing Operations**
```java
interface DrawCommand { void execute(); void undo(); }

class Canvas {
    private final List<String> shapes = new ArrayList<>();
    void add(String shape)    { shapes.add(shape); }
    void remove(String shape) { shapes.remove(shape); }
    List<String> shapes() { return List.copyOf(shapes); }
}
class AddShapeCommand implements DrawCommand {
    private final Canvas canvas; private final String shape;
    AddShapeCommand(Canvas c, String s) { canvas = c; shape = s; }
    public void execute() { canvas.add(shape); }
    public void undo()    { canvas.remove(shape); }
}
```

**Complexity:** `execute` / `undo` O(1) (O(k) for a macro of k commands) · Space O(commands) for history

**Design note:** the **Invoker holds only `Command`** references, so a button, a scheduler, or a queue can all drive the same commands without knowing the receivers.