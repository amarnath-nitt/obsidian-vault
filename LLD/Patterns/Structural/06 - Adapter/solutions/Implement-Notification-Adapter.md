# Implement Notification Adapter

**Source:** AlgoMaster · Low-Level Design Practice · **medium (premium)** · **Pattern:** Adapter
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

An application sends notifications through a single `Notifier` interface. Two third-party SDKs must
be integrated: a **Slack** client with `postMessage(channel, text)` and an **Email** client with
`sendMail(to, subject, body)`. Neither matches the `Notifier` contract. Wrap each in an adapter so
the application can treat every channel uniformly.

### Approach

- **Target** = `Notifier.send(recipient, message)`.
- **Adaptees** = `SlackClient`, `EmailClient` (incompatible signatures).
- **Adapters** = `SlackNotifierAdapter`, `EmailNotifierAdapter` — each translates the call.

### Java Solution

```java
// Target
interface Notifier {
    void send(String recipient, String message);
}

// Adaptees (third-party SDKs — do not modify)
class SlackClient {
    void postMessage(String channel, String text) {
        System.out.println("Slack #" + channel + ": " + text);
    }
}
class EmailClient {
    void sendMail(String to, String subject, String body) {
        System.out.println("Email to " + to + " [" + subject + "]: " + body);
    }
}

// Adapters
class SlackNotifierAdapter implements Notifier {
    private final SlackClient slack;
    SlackNotifierAdapter(SlackClient slack) { this.slack = slack; }
    @Override public void send(String recipient, String message) {
        slack.postMessage(recipient, message);                 // map recipient → channel
    }
}

class EmailNotifierAdapter implements Notifier {
    private final EmailClient email;
    EmailNotifierAdapter(EmailClient email) { this.email = email; }
    @Override public void send(String recipient, String message) {
        email.sendMail(recipient, "Notification", message);    // supply a default subject
    }
}
```

**Client — uniform use of every channel**
```java
class AlertService {
    private final java.util.List<Notifier> channels = new java.util.ArrayList<>();
    void addChannel(Notifier n) { channels.add(n); }
    void alert(String recipient, String message) {
        channels.forEach(n -> n.send(recipient, message));
    }
}

// usage
AlertService svc = new AlertService();
svc.addChannel(new SlackNotifierAdapter(new SlackClient()));
svc.addChannel(new EmailNotifierAdapter(new EmailClient()));
svc.alert("ops", "Deployment succeeded");
```

### Why it works
- **One uniform contract** — `AlertService` only knows `Notifier`.
- **Extra parameters supplied by the adapter** — Email needs a subject, so the adapter provides one.
- **New channel = one adapter** — add Teams/Telegram without touching the service.

**Complexity:** O(channels) per alert · Space O(channels)

---
#adapter #notifications #lld #practice