# Coupling & Cohesion — Concept

## What Is It?

Two halves of the same goal:

- **Low coupling** — modules depend on each other as little as possible, ideally through interfaces.
- **High cohesion** — the things inside a module belong together and serve a single purpose.

Target: **high cohesion inside, low coupling between.**

| | |
|---|---|
| **Principle** | Coupling & Cohesion |
| **One-liner** | Independent modules, each doing one thing well |

---

## When to Use

> **Trigger keywords:** "a change ripples across many classes", "everything knows everything", "god class"

| Smell | Move |
|-------|------|
| A `switch` over concrete implementations | depend on an interface; register implementations |
| One class mixes routing, formatting and delivery | one class, one job |
| Editing one module forces edits in five others | invert the dependency |

---

## In Java

```java
// ❌ Tightly coupled: knows every concrete channel, and formats + sends + routes
class Router {
    void route(String ch, String msg) {
        if (ch.equals("email")) new EmailSender().send(msg.toUpperCase());   // formatting + delivery
        else if (ch.equals("sms")) new SmsSender().send(msg);
        ...
    }
}

// ✅ Low coupling (interface) + high cohesion (each class one job)
interface AlertChannel { String name(); void send(String message); }

class AlertRouter {                       // routing only
    private final Map<String, AlertChannel> channels = new HashMap<>();
    void register(AlertChannel c) { channels.put(c.name(), c); }
    void route(String name, String msg) { channels.get(name).send(msg); }
}
```

---

## Notes

- **Cohesion** is measured by *"does everything in this class change for the same reason?"*
- **Coupling** is measured by *"how much do I have to know to change this class?"*
- Both are also fixed by **SoC** (layer level) and **SRP** (class level).

---

## Common Mistakes

1. Swapping one god class for five classes that still call into each other constantly.
2. Making everything an interface with one implementation (coupling reduced, cohesion lost).
3. Treating coupling as "any dependency" — some coupling is the point of a design.

---

## Related

- [[../00 - Index|Design Principles Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#design-principles #coupling #cohesion #lld #concept
