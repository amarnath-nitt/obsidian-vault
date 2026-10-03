# Mediator — Implementations & Examples

**Pattern:** Mediator (Behavioural) · **Skill:** centralising communication between colleagues

### Approach

- Define a **Mediator** interface that colleagues call.
- Implement a **ConcreteMediator** that knows the colleagues and routes messages.
- Each **Colleague** holds a reference to the mediator and talks **only** through it.

### Java Solutions

**1. Chat Room**
```java
import java.util.*;

interface ChatMediator { void send(String message, User sender); void addUser(User u); }

class ChatRoom implements ChatMediator {
    private final List<User> users = new ArrayList<>();
    public void addUser(User u) { users.add(u); }
    public void send(String message, User sender) {
        for (User u : users) {
            if (u != sender) u.receive(message);          // route to everyone else
        }
    }
}

abstract class User {
    protected final ChatMediator mediator;
    protected final String name;
    protected User(ChatMediator mediator, String name) { this.mediator = mediator; this.name = name; }
    abstract void send(String message);
    abstract void receive(String message);
}
class ChatUser extends User {
    ChatUser(ChatMediator m, String name) { super(m, name); }
    void send(String message) { System.out.println(name + " sends: " + message); mediator.send(message, this); }
    void receive(String message) { System.out.println("  " + name + " receives: " + message); }
}
// usage
ChatMediator room = new ChatRoom();
User alice = new ChatUser(room, "Alice");
User bob   = new ChatUser(room, "Bob");
room.addUser(alice); room.addUser(bob);
alice.send("Hi all!");
```

**2. Air Traffic Control**
```java
import java.util.*;

interface ATCMediator { void registerFlight(Flight f); boolean requestLanding(Flight f); }

class ControlTower implements ATCMediator {
    private final List<Flight> flights = new ArrayList<>();
    private Flight runwayInUse;
    public void registerFlight(Flight f) { flights.add(f); }
    public boolean requestLanding(Flight f) {
        if (runwayInUse == null || runwayInUse == f) {     // simple arbitration
            runwayInUse = f;
            return true;
        }
        return false;
    }
}
class Flight {
    private final ATCMediator tower;
    private final String id;
    Flight(ATCMediator tower, String id) { this.tower = tower; this.id = id; }
    void land() {
        if (tower.requestLanding(this)) System.out.println(id + " landing ✔");
        else System.out.println(id + " must hold (runway busy)");
    }
}
```

**3. UI Dialog Coordination**
```java
interface DialogMediator { void widgetChanged(Widget w); }
abstract class Widget {
    protected final DialogMediator dialog;
    protected Widget(DialogMediator d) { dialog = d; }
    abstract void changed();
}
class CheckBox extends Widget {
    boolean checked;
    CheckBox(DialogMediator d) { super(d); }
    void setChecked(boolean v) { checked = v; dialog.widgetChanged(this); }
    void changed() { System.out.println("Checkbox changed"); }
}
class TextField extends Widget {
    String text = "";
    TextField(DialogMediator d) { super(d); }
    void setText(String t) { text = t; dialog.widgetChanged(this); }
    void changed() { System.out.println("Text field changed"); }
}
class SignupDialog implements DialogMediator {
    private CheckBox terms; private TextField email;
    void setWidgets(CheckBox cb, TextField tf) { terms = cb; email = tf; }
    public void widgetChanged(Widget w) {
        if (w == terms && terms.checked && email.text.isBlank())
            System.out.println("Enable email field");      // coordination rule
    }
}
```

**4. Smart Home Hub (event bus style)**
```java
import java.util.*;
import java.util.concurrent.*;

interface Device { void onEvent(String event); }

class SmartHub {                                          // Mediator
    private final Map<String, List<Device>> subscribers = new ConcurrentHashMap<>();
    void subscribe(String event, Device d) {
        subscribers.computeIfAbsent(event, k -> new CopyOnWriteArrayList<>()).add(d);
    }
    void publish(String event) {
        subscribers.getOrDefault(event, List.of()).forEach(d -> d.onEvent(event));
    }
}
```

**Complexity:** routing O(k) for k colleagues · Space O(colleagues)

**Design note:** the event-bus variant is the practical, modern mediator — colleagues never hold direct references to one another, only to the bus.