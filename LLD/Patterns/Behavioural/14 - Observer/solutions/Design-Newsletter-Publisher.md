# Design a Newsletter Publisher

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Observer
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-newsletter-publisher)

### Problem

A newsletter publisher sends each new issue to all current **subscribers**. Subscribers can join and
leave at any time, and adding a new subscriber type must not require changing the publisher.

### Approach — Observer

- **Subject** = `Newsletter` (`subscribe`, `unsubscribe`, `publish`).
- **Observer** = `Subscriber` (`receive(issue)`).
- The subject holds a list of subscribers and notifies them on `publish`.

### Java Solution

```java
import java.util.*;
import java.util.concurrent.CopyOnWriteArrayList;

interface Subscriber {
    void receive(String issue);
}

class EmailSubscriber implements Subscriber {
    private final String email;
    EmailSubscriber(String email) { this.email = email; }
    @Override public void receive(String issue) { System.out.println(email + " got: " + issue); }
}

class Newsletter {                                        // Subject
    private final List<Subscriber> subscribers = new CopyOnWriteArrayList<>();
    private String latest;

    public void subscribe(Subscriber s)   { subscribers.add(s); }
    public void unsubscribe(Subscriber s) { subscribers.remove(s); }

    public void publish(String issue) {
        latest = issue;
        System.out.println("Publishing: " + issue);
        for (Subscriber s : subscribers) s.receive(issue);   // notify a safe snapshot
    }

    public String latest() { return latest; }
}
```

**Usage**
```java
Newsletter newsletter = new Newsletter();
Subscriber alice = new EmailSubscriber("alice@example.com");
Subscriber bob   = new EmailSubscriber("bob@example.com");

newsletter.subscribe(alice);
newsletter.subscribe(bob);
newsletter.publish("Issue #1");     // both notified

newsletter.unsubscribe(bob);
newsletter.publish("Issue #2");     // only Alice notified
```

### Design points
- **One-to-many** — a single `publish` reaches every current subscriber.
- **Dynamic membership** — subscribe/unsubscribe at runtime; the publisher is unaware of concrete types.
- **Safe iteration** — `CopyOnWriteArrayList` lets a subscriber add/remove itself during notify.

**Complexity:** O(n) per publish · Space O(n)

---
#observer #lld #practice