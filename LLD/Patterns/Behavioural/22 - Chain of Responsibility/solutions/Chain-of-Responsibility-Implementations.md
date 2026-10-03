# Chain of Responsibility — Implementations & Examples

**Pattern:** Chain of Responsibility (Behavioural) · **Skill:** passing requests along handlers

### Approach

- Give each **Handler** a `next` reference and a `handle(request)` method.
- A handler either processes the request or forwards it to `next`.
- The **client** assembles the chain and submits to the first handler.

### Java Solutions

**1. Logging Levels**
```java
abstract class Logger {
    enum Level { INFO, DEBUG, ERROR }
    protected Level level;
    protected Logger next;
    protected Logger(Level level) { this.level = level; }
    Logger setNext(Logger next) { this.next = next; return next; }   // fluent linking

    void log(Level msgLevel, String message) {
        if (msgLevel.ordinal() >= level.ordinal()) write(message);
        if (next != null) next.log(msgLevel, message);              // impure: may also forward
    }
    protected abstract void write(String message);
}
class InfoLogger  extends Logger { InfoLogger()  { super(Level.INFO); }  protected void write(String m) { System.out.println("INFO: " + m); } }
class DebugLogger extends Logger { DebugLogger() { super(Level.DEBUG); } protected void write(String m) { System.out.println("DEBUG: " + m); } }
class ErrorLogger extends Logger { ErrorLogger() { super(Level.ERROR); } protected void write(String m) { System.out.println("ERROR: " + m); } }

// usage
Logger chain = new InfoLogger();
chain.setNext(new DebugLogger()).setNext(new ErrorLogger());
chain.log(Logger.Level.ERROR, "disk full");
```

**2. Approval Workflow (pure chain)**
```java
abstract class Approver {
    protected Approver next;
    Approver setNext(Approver next) { this.next = next; return next; }
    abstract void approve(double amount);

    protected void forward(double amount) {
        if (next != null) next.approve(amount);
        else System.out.println("No one can approve " + amount);
    }
}
class Manager extends Approver {
    void approve(double amount) {
        if (amount <= 1000) System.out.println("Manager approved " + amount);
        else forward(amount);
    }
}
class Director extends Approver {
    void approve(double amount) {
        if (amount <= 10_000) System.out.println("Director approved " + amount);
        else forward(amount);
    }
}
class CEO extends Approver {
    void approve(double amount) { System.out.println("CEO approved " + amount); }
}
// usage
Approver chain = new Manager();
chain.setNext(new Director()).setNext(new CEO());
chain.approve(500);      // Manager
chain.approve(50_000);   // CEO
```

**3. ATM Cash Dispensing**
```java
abstract class CashHandler {
    protected CashHandler next;
    CashHandler setNext(CashHandler n) { this.next = n; return n; }
    void dispense(int amount) {
        if (amount == 0) return;
        if (next != null) next.dispense(amount);
        else System.out.println("Cannot dispense " + amount);
    }
}
class Note2000 extends CashHandler {
    void dispense(int amount) {
        int count = amount / 2000;
        if (count > 0) System.out.println("2000 x " + count);
        super.dispense(amount % 2000);
    }
}
class Note500 extends CashHandler {
    void dispense(int amount) {
        int count = amount / 500;
        if (count > 0) System.out.println("500 x " + count);
        super.dispense(amount % 500);
    }
}
class Note100 extends CashHandler {
    void dispense(int amount) {
        int count = amount / 100;
        if (count > 0) System.out.println("100 x " + count);
        super.dispense(amount % 100);
    }
}
// usage
CashHandler atm = new Note2000(); atm.setNext(new Note500()).setNext(new Note100());
atm.dispense(3800);   // 2000 x 1, 500 x 3, 100 x 3
```

**4. Middleware Pipeline (impure, pre/post)**
```java
interface Middleware { boolean handle(String request); }

abstract class MiddlewareBase implements Middleware {
    protected Middleware next;
    MiddlewareBase setNext(Middleware n) { this.next = n; return this; }
    protected boolean forward(String request) { return next == null || next.handle(request); }
}

class AuthMiddleware extends MiddlewareBase {
    public boolean handle(String request) {
        if (!request.contains("token")) { System.out.println("401 Unauthorized"); return false; }
        return forward(request);
    }
}
class RateLimitMiddleware extends MiddlewareBase {
    public boolean handle(String request) { System.out.println("Rate-limit OK"); return forward(request); }
}
class OrderHandler extends MiddlewareBase {
    public boolean handle(String request) { System.out.println("Handled order: " + request); return true; }
}
// usage
MiddlewareBase pipeline = new AuthMiddleware();
pipeline.setNext(new RateLimitMiddleware()).setNext(new OrderHandler());
pipeline.handle("GET /orders?token=abc");
```

**5. Configurable Chain Order**
```java
import java.util.*;

class ChainBuilder {
    static Middleware build(List<java.util.function.Supplier<MiddlewareBase>> suppliers) {
        MiddlewareBase head = suppliers.get(0).get(), current = head;
        for (int i = 1; i < suppliers.size(); i++) current = current.setNext(suppliers.get(i).get());
        return head;
    }
}
```

**Complexity:** O(chain length) worst case per request · Space O(handlers)

**Design note:** always terminate with a **catch-all** handler (or the middleware variant returns `true`) so requests are never silently swallowed.