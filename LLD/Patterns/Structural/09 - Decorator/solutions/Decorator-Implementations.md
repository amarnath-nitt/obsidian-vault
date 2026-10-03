# Decorator — Implementations & Examples

**Pattern:** Decorator (Structural) · **Skill:** adding behaviour dynamically by wrapping

### Approach

- Define a **Component** interface.
- Implement the base object as a **ConcreteComponent**.
- Create an abstract **Decorator** that implements Component and holds another Component.
- Concrete decorators add behaviour before/after delegating to the wrapped object.

### Java Solutions

**1. Coffee with Condiments**
```java
interface Coffee { String description(); double cost(); }

class Espresso implements Coffee {
    public String description() { return "Espresso"; }
    public double cost() { return 2.00; }
}

abstract class CoffeeDecorator implements Coffee {
    protected final Coffee inner;
    protected CoffeeDecorator(Coffee inner) { this.inner = inner; }
    public String description() { return inner.description(); }
    public double cost() { return inner.cost(); }
}
class Milk extends CoffeeDecorator {
    Milk(Coffee c) { super(c); }
    public String description() { return super.description() + ", Milk"; }
    public double cost() { return super.cost() + 0.50; }
}
class Mocha extends CoffeeDecorator {
    Mocha(Coffee c) { super(c); }
    public String description() { return super.description() + ", Mocha"; }
    public double cost() { return super.cost() + 0.75; }
}
class Whip extends CoffeeDecorator {
    Whip(Coffee c) { super(c); }
    public String description() { return super.description() + ", Whip"; }
    public double cost() { return super.cost() + 0.60; }
}

// usage — stack any combination
Coffee order = new Whip(new Mocha(new Milk(new Espresso())));
System.out.println(order.description() + " = $" + order.cost());
// Espresso, Milk, Mocha, Whip = $3.85
```

**2. HTTP Middleware Chain**
```java
interface Handler { String handle(String request); }

class BaseHandler implements Handler {
    public String handle(String request) { return "200 OK for " + request; }
}

abstract class HandlerDecorator implements Handler {
    protected final Handler next;
    protected HandlerDecorator(Handler next) { this.next = next; }
    public String handle(String request) { return next.handle(request); }
}
class LoggingHandler extends HandlerDecorator {
    LoggingHandler(Handler n) { super(n); }
    public String handle(String request) {
        System.out.println("LOG: " + request);
        return super.handle(request);
    }
}
class AuthHandler extends HandlerDecorator {
    AuthHandler(Handler n) { super(n); }
    public String handle(String request) {
        if (!request.contains("token")) return "401 Unauthorized";
        return super.handle(request);
    }
}
// usage
Handler handler = new LoggingHandler(new AuthHandler(new BaseHandler()));
System.out.println(handler.handle("GET /orders?token=abc"));
```

**3. Java I/O Style Decorator**
```java
interface DataSource { void writeData(String data); void readData(); }

class FileDataSource implements DataSource {
    private String data;
    public void writeData(String d) { data = d; }
    public void readData() { System.out.println("file:" + data); }
}
abstract class DataSourceDecorator implements DataSource {
    protected final DataSource wrappee;
    protected DataSourceDecorator(DataSource s) { wrappee = s; }
    public void writeData(String d) { wrappee.writeData(d); }
    public void readData() { wrappee.readData(); }
}
class EncryptionDecorator extends DataSourceDecorator {
    EncryptionDecorator(DataSource s) { super(s); }
    public void writeData(String d) { super.writeData("ENC(" + d + ")"); }
}
class CompressionDecorator extends DataSourceDecorator {
    CompressionDecorator(DataSource s) { super(s); }
    public void writeData(String d) { super.writeData("ZIP(" + d + ")"); }
}
// usage
DataSource src = new EncryptionDecorator(new CompressionDecorator(new FileDataSource()));
src.writeData("secret");   // stored as ENC(ZIP(secret))
src.readData();
```

**4. Order-Sensitive Pricing**
```java
interface Price { double amount(); }
class BasePrice implements Price { public double amount() { return 100.0; } }
abstract class PriceDecorator implements Price {
    protected final Price p; PriceDecorator(Price p) { this.p = p; }
    public double amount() { return p.amount(); }
}
class Discount extends PriceDecorator {          // applied BEFORE tax
    Discount(Price p) { super(p); }
    public double amount() { return super.amount() * 0.9; }   // -10% first
}
class Tax extends PriceDecorator {               // applied AFTER discount
    Tax(Price p) { super(p); }
    public double amount() { return super.amount() * 1.18; }  // +18% last
}
// discount-then-tax: new Tax(new Discount(new BasePrice())).amount() == 106.2
```

**Complexity:** each decoration O(1) · Space O(depth) per call chain

**Design note:** the wrapper **must implement the same interface** as the wrapped object — that is what makes the decoration transparent to the client.