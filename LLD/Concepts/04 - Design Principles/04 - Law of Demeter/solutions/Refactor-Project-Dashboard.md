# Refactor Project Dashboard (Law of Demeter)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Principle:** Law of Demeter
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-project-dashboard)

### Problem

A dashboard builds a summary by **reaching through** long object chains — project → owner → team →
lead → email, and project → tasks → assignee. Each hop couples the dashboard to internals it should
not know. Apply the **Law of Demeter** with delegating methods.

### The Smell (before)

```java
class ProjectDashboard {
    String summary(Project project) {
        String leadEmail = project.getOwner().getTeam().getLead().getEmail();   // 4 hops
        long openTasks   = project.getTasks().stream()
                .filter(t -> !t.getStatus().isDone()).count();                 // 3 hops
        String assignee  = project.getTasks().get(0).getAssignee().getName();  // 3 hops
        return leadEmail + " | open=" + openTasks + " | first=" + assignee;
    }
}
```

### The Fix (after)

```java
record Member(String name, String email) {}

class Team {
    private final Member lead;
    Team(Member lead) { this.lead = lead; }
    String leadEmail() { return lead.email(); }             // delegates
}

class Project {
    private final Member owner;
    private final Team team;
    private final java.util.List<Task> tasks;

    Project(Member owner, Team team, java.util.List<Task> tasks) {
        this.owner = owner; this.team = team; this.tasks = tasks;
    }

    // Project answers questions about itself — callers never reach inside
    String leadEmail()          { return team.leadEmail(); }
    long openTaskCount()        { return tasks.stream().filter(Task::isOpen).count(); }
    String firstAssigneeName()  { return tasks.isEmpty() ? "—" : tasks.get(0).assigneeName(); }

    static class Task {
        private final boolean done;
        private final Member assignee;
        Task(boolean done, Member assignee) { this.done = done; this.assignee = assignee; }
        boolean isOpen()      { return !done; }
        String assigneeName() { return assignee.name(); }
    }
}

class ProjectDashboard {
    String summary(Project project) {
        return project.leadEmail()
             + " | open=" + project.openTaskCount()
             + " | first=" + project.firstAssigneeName();       // one friend: the project
    }
}
```

### Design points
- **One friend per call** — the dashboard talks only to `Project`.
- **Delegating methods** — `Project` hides `Team`, `Member`, and `Task` internals.
- **Fewer dependencies** — no `getOwner().getTeam()...` chains anywhere.
- **Resilient** — restructuring `Team`/`Task` does not touch the dashboard.

> **Law of Demeter:** a method may call methods on itself, its fields, its parameters, objects it
> creates, or its components — but not on objects *returned* by those calls.

**Complexity:** O(tasks) per summary · Space O(1)

---
#design-principles #law-of-demeter #lld #practice