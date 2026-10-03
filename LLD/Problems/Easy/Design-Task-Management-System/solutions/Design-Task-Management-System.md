# Design a Task Management System (Easy)

**Difficulty:** Easy · **Patterns:** Composite, Observer
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a Kanban tracker: tasks with metadata, nested lists, assign/move/filter, notifications on every change.

**Functional**
- **Tasks**: title, description, priority, due date, assignee, status, comments.
- **Lists nest** (project → sprint → list); **move** tasks across lists.
- **Filter** by assignee/priority/due/status; **notify** assignee + watchers on assign/move/comment.

**Non-functional**
- Single tasks and lists treated uniformly; new event types without task changes.

### The failure, before

```java
// ❌ TaskManager with a method per query and notify() calls pasted into each —
// adding "overdue reminders" edits 6 methods; nested projects need a parallel class tree.
public void assign(...) { ...; sendMail(...); } public void move(...) { ...; sendMail(...); }
```

### The Fix (after)

Composite `WorkItem` + validated status moves + observer fan-out.

```java
import java.time.LocalDate;
import java.util.*;

enum Priority { LOW, MEDIUM, HIGH }
enum Status { TODO, IN_PROGRESS, BLOCKED, DONE }

interface WorkItem { double progress(); }

class TaskEvent {
    final Task task; final String type;
    TaskEvent(Task task, String type) { this.task = task; this.type = type; }
}
interface TaskListener { void onEvent(TaskEvent e); }

class Task implements WorkItem {
    private final String id, title;
    private String assignee;
    private Status status = Status.TODO;
    private Priority priority = Priority.MEDIUM;
    private LocalDate due;
    private final List<String> comments = new ArrayList<>();
    private final Set<String> watchers = new HashSet<>();
    private final List<TaskListener> listeners = new ArrayList<>();

    Task(String id, String title) { this.id = id; this.title = title; }
    public void subscribe(TaskListener l) { listeners.add(l); }
    public void watch(String u) { watchers.add(u); }
    private void emit(String type) {
        TaskEvent e = new TaskEvent(this, type);
        for (TaskListener l : listeners) l.onEvent(e);
    }
    public void assign(String u) { assignee = u; watch(u); emit("ASSIGN"); }
    public void move(Status s) {
        if (status == Status.DONE) throw new IllegalStateException("Done is terminal");
        status = s; emit("MOVE");
    }
    public void comment(String c) { comments.add(c); emit("COMMENT"); }
    public boolean isOverdue() {
        return due != null && status != Status.DONE && due.isBefore(LocalDate.now());
    }
    public void setDue(LocalDate d) { due = d; }
    public void setPriority(Priority p) { priority = p; }
    public String getAssignee() { return assignee; }
    public Status getStatus() { return status; }
    public Priority getPriority() { return priority; }
    public double progress() { return status == Status.DONE ? 1.0 : status == Status.IN_PROGRESS ? 0.5 : 0.0; }
}

class TaskList implements WorkItem {
    private final String name;
    private final List<WorkItem> kids = new ArrayList<>();
    TaskList(String name) { this.name = name; }
    public void add(WorkItem w) { kids.add(w); }
    public void remove(WorkItem w) { kids.remove(w); }
    public double progress() {
        if (kids.isEmpty()) return 0;
        return kids.stream().mapToDouble(WorkItem::progress).average().orElse(0);
    }
}

interface TaskFilter { boolean matches(Task t); }

class NotificationService implements TaskListener {
    public void onEvent(TaskEvent e) {
        System.out.println("Notify about " + e.type + " on task " + e.task.getAssignee());
    }
}
```

**Usage**
```java
Task t = new Task("T1", "Design API");
t.subscribe(new NotificationService());
t.assign("amy"); t.move(Status.IN_PROGRESS); t.comment("draft ready");
TaskList sprint = new TaskList("Sprint 3"); sprint.add(t);
```

### Design points
- **Composite roll-up** — list progress is the mean of children; nesting projects costs nothing.
- **Done is terminal** — one guard in `move()` kills the teleport bug class.
- **Overdue derived** — due + status query; no stored flag to go stale.
- **Listeners own side effects** — notify/audit/remind subscribe; `Task` stays clean.

**Complexity:** progress O(items) · Space O(tasks + lists).

---
#lld #machine-coding #task-management #easy #practice
