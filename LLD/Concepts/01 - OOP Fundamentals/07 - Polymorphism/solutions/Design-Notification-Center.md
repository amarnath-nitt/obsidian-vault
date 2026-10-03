# Design Notification Center (Polymorphism)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Topic:** Polymorphism
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-notification-center)

### Problem

Design a notification center that can deliver a message through several channels (email, SMS, push).
The center should handle every channel **the same way**, relying on **polymorphism** rather than a
`switch` over channel types.

### Approach

- Define a `Notifier` interface (`channel()`, `send(recipient, message)`).
- Implement a concrete notifier per channel.
- The center holds a collection of `Notifier` and dispatches uniformly.

### Java Solution

```java
import java.util.*;

public interface Notifier {
    String channel();
    void send(String recipient, String message);
}

class EmailNotifier implements Notifier {
    public String channel() { return "email"; }
    public void send(String recipient, String message) {
        System.out.println("📧 to " + recipient + ": " + message);
    }
}
class SmsNotifier implements Notifier {
    public String channel() { return "sms"; }
    public void send(String recipient, String message) {
        System.out.println("📱 to " + recipient + ": " + message);
    }
}
class PushNotifier implements Notifier {
    public String channel() { return "push"; }
    public void send(String recipient, String message) {
        System.out.println("🔔 to " + recipient + ": " + message);
    }
}

public class NotificationCenter {
    private final List<Notifier> notifiers = new ArrayList<>();

    public void add(Notifier notifier) { notifiers.add(notifier); }

    public void broadcast(String recipient, String message) {
        for (Notifier n : notifiers) {                  // one call site, many forms
            n.send(recipient, message);
        }
    }
}
```

**Usage**
```java
NotificationCenter center = new NotificationCenter();
center.add(new EmailNotifier());
center.add(new SmsNotifier());
center.add(new PushNotifier());

center.broadcast("alice", "Your order shipped");
// 📧 / 📱 / 🔔 — the same send() call, three different behaviours
```

### Design points
- **One interface, many forms** — `n.send(...)` dispatches at runtime.
- **No `switch` on channel** — add a `SlackNotifier` without touching the center.
- **Uniform handling** — the center treats every channel identically.

**Complexity:** O(channels) per broadcast · Space O(channels)

---
#oop #polymorphism #lld #practice