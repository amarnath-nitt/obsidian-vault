# Design Pub Sub System (Medium)

**Difficulty:** Medium · **Patterns:** Observer, Singleton
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design an in-process pub-sub broker: topics, subscribe/unsubscribe with filters, ordered fan-out, durable replay.

**Functional**
- **Topics**; **subscribe/unsubscribe** with optional filters; **publish** reaches all current subscribers in order.
- **Durable** subscribers replay missed messages; slow subscribers never block publishers.

**Non-functional**
- Publish returns fast (queued fan-out); per-topic ordering only.

### The failure, before

```java
// ❌ Publisher loops over a global listener list inline — one slow subscriber
// blocks every publisher; unsubscribe by name removes the wrong entry; no replay.
public void publish(String m) { for (L l : all) l.on(m); }
```

### The Fix (after)

Broker + topics + queued deliveries + filter predicates.

```java
import java.util.*;
import java.util.concurrent.*;
import java.util.function.Predicate;

class Message {
    final String id, topic, payload; final long ts = System.currentTimeMillis();
    Message(String topic, String payload) { this.id = UUID.randomUUID().toString(); this.topic = topic; this.payload = payload; }
}

interface Subscriber { void onMessage(Message m) throws Exception; }

class Subscription {
    final Subscriber sub; final Predicate<Message> filter; final boolean durable; long offset = 0;
    Subscription(Subscriber sub, Predicate<Message> filter, boolean durable) {
        this.sub = sub; this.filter = filter; this.durable = durable;
    }
}

class Topic {
    final String name;
    final List<Subscription> subs = new CopyOnWriteArrayList<>();
    final List<Message> retained = new ArrayList<>();   // ring in prod; list here
    Topic(String name) { this.name = name; }
}

class Broker {
    private static volatile Broker instance;
    private final Map<String, Topic> topics = new ConcurrentHashMap<>();
    private final BlockingQueue<Runnable> queue = new LinkedBlockingQueue<>();
    private Broker() {
        Thread w = new Thread(() -> { try { while (true) queue.take().run(); } catch (InterruptedException e) { Thread.currentThread().interrupt(); } });
        w.setDaemon(true); w.start();
    }
    public static Broker getInstance() {
        if (instance == null) synchronized (Broker.class) {
            if (instance == null) instance = new Broker();
        }
        return instance;
    }
    public Topic topic(String name) { return topics.computeIfAbsent(name, Topic::new); }

    public void subscribe(String topic, Subscriber s, Predicate<Message> filter, boolean durable) {
        Topic t = topic(topic);
        Subscription reg = new Subscription(s, filter, durable);
        if (durable) {   // replay missed: everything retained so far passes the filter
            for (Message m : t.retained) if (filter.test(m)) deliver(reg, m);
        }
        t.subs.add(reg);
    }
    public void unsubscribe(String topic, Subscriber s) {
        topic(topic).subs.removeIf(reg -> reg.sub == s);   // exact object: no name collisions
    }
    public void publish(String topicName, String payload) {
        Topic t = topic(topicName);
        Message m = new Message(topicName, payload);
        synchronized (t.retained) { t.retained.add(m); }   // retention under one lock
        for (Subscription reg : t.subs)
            if (reg.filter.test(m)) queue.offer(() -> deliver(reg, m));  // queued: publisher never waits
    }
    private void deliver(Subscription reg, Message m) {
        int tries = 0;
        while (true) {
            try { reg.sub.onMessage(m); return; }
            catch (Exception e) {
                if (++tries >= 3) { System.err.println("Dead-letter " + m.id); return; }
                try { Thread.sleep(50L * tries); } catch (InterruptedException ie) { Thread.currentThread().interrupt(); return; }
            }
        }
    }
}
```

**Usage**
```java
Broker b = Broker.getInstance();
Subscriber sms = m -> System.out.println("SMS: " + m.payload);
b.subscribe("orders", sms, m -> m.payload.contains("SHIPPED"), false);
b.publish("orders", "Order SHIPPED #42");
b.unsubscribe("orders", sms);
```

### Design points
- **Queue is the async boundary** — publish enqueues and returns; one slow subscriber stalls nothing.
- **Exact-object unsubscribe** — identity comparison kills the name-collision bug class.
- **Filter at delivery** — publishers stay topic-blind; predicates live with the subscription.
- **Retry then dead-letter** — 3 tries with backoff, then aside; the topic always moves on.

**Complexity:** publish O(subscribers) enqueue · deliver O(1) per message · Space O(topics + retained).

---
#lld #machine-coding #pubsub #medium #practice
