# Refactor Alert Router (Coupling & Cohesion)

**Source:** AlgoMaster · Low-Level Design Practice · **medium (premium)** · **Principle:** Coupling & Cohesion
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-alert-router)

### Problem

An `AlertRouter` is **tightly coupled** to concrete delivery classes (email, SMS, Slack) via a
`switch`, and mixes routing rules with delivery details (**low cohesion**). Apply the goal of
**low coupling, high cohesion**: depend on an abstraction and keep routing logic in one place.

### The Smell (before)

```java
// ❌ Router knows every concrete channel + does formatting + sending + redirects
class AlertRouter {
    void route(String channel, String message) {
        switch (channel) {
            case "email" -> System.out.println("EMAIL: " + message.toUpperCase() + "!!!");   // formatting
            case "sms"   -> System.out.println("SMS: " + message);                          // delivery
            case "slack" -> System.out.println("SLACK: " + message.substring(0, Math.min(20, message.length())));
            default      -> System.out.println("unknown channel, dropping");
        }
    }
}
```

### The Fix (after)

```java
import java.util.*;

// Low coupling: the router depends only on this abstraction
interface AlertChannel {
    String name();
    void send(String message);
}

class EmailChannel implements AlertChannel {
    public String name() { return "email"; }
    public void send(String message) { System.out.println("EMAIL: " + message.toUpperCase() + "!!!"); }
}
class SmsChannel implements AlertChannel {
    public String name() { return "sms"; }
    public void send(String message) { System.out.println("SMS: " + message); }
}
class SlackChannel implements AlertChannel {
    public String name() { return "slack"; }
    public void send(String message) {
        System.out.println("SLACK: " + message.substring(0, Math.min(20, message.length())));
    }
}

// High cohesion: this class does ONE thing — route by name
class AlertRouter {
    private final Map<String, AlertChannel> channels = new HashMap<>();

    void register(AlertChannel channel) { channels.put(channel.name(), channel); }

    void route(String channelName, String message) {
        AlertChannel channel = channels.get(channelName);
        if (channel == null) throw new IllegalArgumentException("Unknown channel: " + channelName);
        channel.send(message);                 // delegates; no formatting, no switch
    }

    /** Broadcast to every registered channel. */
    void broadcast(String message) { channels.values().forEach(c -> c.send(message)); }
}
```

**Usage**
```java
AlertRouter router = new AlertRouter();
router.register(new EmailChannel());
router.register(new SmsChannel());
router.register(new SlackChannel());

router.route("slack", "Disk usage at 90%");
router.broadcast("Deployment complete");
```

### Design points
- **Low coupling** — the router depends on `AlertChannel`, not on email/SMS/Slack classes.
- **High cohesion** — routing lives in the router; formatting/delivery live in channels.
- **No `switch`** — a new channel registers itself; the router is unchanged (OCP too).
- **Testable** — a fake `AlertChannel` records deliveries for assertions.

**Complexity:** O(1) per route, O(channels) per broadcast · Space O(channels)

---
#design-principles #coupling #cohesion #lld #practice