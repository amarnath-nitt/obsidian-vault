# Design a Chat Room

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Mediator
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-chat-room)

### Problem

In a chat room, users send messages to everyone else. If each user held a reference to every other
user, the participant graph would be dense and hard to maintain. Route all communication through a
central **chat room mediator** so users do not know each other.

### Approach — Mediator

- **Mediator** = `ChatRoom` — knows the participants and routes messages.
- **Colleague** = `User` — holds a reference to the mediator only, never to other users.

### Java Solution

```java
import java.util.*;
import java.util.concurrent.CopyOnWriteArrayList;

interface ChatMediator {
    void join(User user);
    void leave(User user);
    void broadcast(String message, User sender);   // deliver to everyone but the sender
}

abstract class User {
    protected final ChatMediator room;
    protected final String name;
    protected User(ChatMediator room, String name) { this.room = room; this.name = name; }

    abstract void receive(String from, String message);

    /** A user only talks to the mediator. */
    void send(String message) { room.broadcast(message, this); }
    String name() { return name; }
}

class ChatUser extends User {
    ChatUser(ChatMediator room, String name) { super(room, name); }
    @Override void receive(String from, String message) {
        System.out.println("  " + name + " ← " + from + ": " + message);
    }
}

class ChatRoom implements ChatMediator {                  // Mediator
    private final List<User> users = new CopyOnWriteArrayList<>();

    public void join(User user) {
        users.add(user);
        System.out.println(user.name() + " joined");
    }
    public void leave(User user) {
        users.remove(user);
        System.out.println(user.name() + " left");
    }
    public void broadcast(String message, User sender) {
        for (User u : users) {
            if (u != sender) u.receive(sender.name(), message);   // route to everyone else
        }
    }
}
```

**Usage**
```java
ChatMediator room = new ChatRoom();
User alice = new ChatUser(room, "Alice");
User bob   = new ChatUser(room, "Bob");
User carol = new ChatUser(room, "Carol");

room.join(alice); room.join(bob); room.join(carol);
alice.send("Hi all!");     // Bob and Carol receive, Alice does not
room.leave(bob);
carol.send("Bye");          // only Alice receives
```

### Design points
- **Colleagues decoupled** — `User` code never references another `User`.
- **Star topology** — O(n) references instead of O(n²).
- **Centralised routing** — the "who receives what" rule lives in the mediator.

**Complexity:** O(users) per message · Space O(users)

---
#mediator #lld #practice