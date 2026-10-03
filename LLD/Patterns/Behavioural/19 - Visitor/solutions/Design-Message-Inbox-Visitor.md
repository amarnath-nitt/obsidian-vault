# Design a Message Inbox Visitor

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Visitor
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-message-inbox-visitor)

### Problem

An inbox holds messages of several types — **email**, **SMS**, **push notification**. You need to run
different operations over them: count unread, export to a summary, or compute storage used. New
operations should be addable **without editing the message classes**.

### Approach — Visitor (double dispatch)

- **Elements** = `Message` with `accept(visitor)` — `Email`, `Sms`, `Push`.
- **Visitor** = `MessageVisitor` with a `visit(...)` per message type.
- Each operation is a concrete visitor.

### Java Solution

```java
// Visitor
interface MessageVisitor<R> {
    R visit(Email email);
    R visit(Sms sms);
    R visit(Push push);
}

// Element
abstract class Message {
    final boolean read;
    protected Message(boolean read) { this.read = read; }
    abstract <R> R accept(MessageVisitor<R> visitor);   // double dispatch
}

class Email extends Message {
    final String subject; final int bodySize;
    Email(boolean read, String subject, int bodySize) { super(read); this.subject = subject; this.bodySize = bodySize; }
    @Override <R> R accept(MessageVisitor<R> v) { return v.visit(this); }
}
class Sms extends Message {
    final String text;
    Sms(boolean read, String text) { super(read); this.text = text; }
    @Override <R> R accept(MessageVisitor<R> v) { return v.visit(this); }
}
class Push extends Message {
    final String title;
    Push(boolean read, String title) { super(read); this.title = title; }
    @Override <R> R accept(MessageVisitor<R> v) { return v.visit(this); }
}

// Operation 1 — count unread
class UnreadCountVisitor implements MessageVisitor<Integer> {
    public Integer visit(Email e) { return e.read ? 0 : 1; }
    public Integer visit(Sms s)   { return s.read ? 0 : 1; }
    public Integer visit(Push p)  { return p.read ? 0 : 1; }
}

// Operation 2 — storage usage (bytes)
class StorageVisitor implements MessageVisitor<Integer> {
    public Integer visit(Email e) { return e.bodySize; }
    public Integer visit(Sms s)   { return s.text.length() * 2; }
    public Integer visit(Push p)  { return (p.title.length() + 64) * 2; }
}

// Operation 3 — render a summary line
class SummaryVisitor implements MessageVisitor<String> {
    public String visit(Email e) { return "[email] " + e.subject; }
    public String visit(Sms s)   { return "[sms] " + s.text; }
    public String visit(Push p)  { return "[push] " + p.title; }
}
```

**Usage**
```java
List<Message> inbox = List.of(
        new Email(false, "Welcome", 2048),
        new Sms(true, "Your code is 1234"),
        new Push(false, "New follower"));

UnreadCountVisitor unread = new UnreadCountVisitor();
StorageVisitor storage = new StorageVisitor();
SummaryVisitor summary = new SummaryVisitor();

int unreadCount = 0, bytes = 0;
for (Message m : inbox) {
    unreadCount += m.accept(unread);
    bytes       += m.accept(storage);
    System.out.println(m.accept(summary));
}
System.out.println("Unread=" + unreadCount + " bytes=" + bytes);
```

### Design points
- **Operations live outside the elements** — `Email`/`Sms`/`Push` never change for a new operation.
- **Double dispatch** — `accept` picks the element's `visit` method.
- **Trade-off** — adding a new **message type** forces a new method on **every** visitor.

**Complexity:** O(n) over the inbox per operation · Space O(1)

---
#visitor #lld #practice