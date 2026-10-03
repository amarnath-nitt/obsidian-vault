# Adapter — Implementations & Examples

**Pattern:** Adapter (Structural) · **Skill:** making incompatible interfaces collaborate

### Approach

- Define the **Target** interface your client expects.
- Wrap the incompatible **Adaptee** in an **Adapter** that implements Target and **delegates**.
- Translate both the method names and the argument shapes.

### Java Solutions

**1. Payment Gateway Adapter**
```java
interface PaymentGateway { void pay(double amount); }          // Target

// third-party, incompatible (Adaptee)
class StripeApi {
    void charge(double amount, String currency) {
        System.out.printf("Stripe charged %.2f %s%n", amount, currency);
    }
}

class StripeAdapter implements PaymentGateway {                // Object Adapter
    private final StripeApi stripe;
    StripeAdapter(StripeApi stripe) { this.stripe = stripe; }
    public void pay(double amount) { stripe.charge(amount, "USD"); }
}

// usage
PaymentGateway gateway = new StripeAdapter(new StripeApi());
gateway.pay(49.99);
```

**2. Media Player Adapter**
```java
interface MediaPlayer { void play(String file); }              // Target

class VlcPlayer {                                              // Adaptee
    void playVlc(String file) { System.out.println("VLC playing " + file); }
}

class VlcAdapter implements MediaPlayer {
    private final VlcPlayer vlc = new VlcPlayer();
    public void play(String file) { vlc.playVlc(file); }
}
```

**3. Logger Adapter**
```java
interface AppLogger { void log(String level, String msg); }    // Target

class ThirdPartyLogger {                                       // Adaptee
    void write(String text) { System.out.println("[3P] " + text); }
}

class LoggerAdapter implements AppLogger {
    private final ThirdPartyLogger logger;
    LoggerAdapter(ThirdPartyLogger l) { this.logger = l; }
    public void log(String level, String msg) { logger.write(level + ": " + msg); }
}
```

**4. Two-way Adapter**
```java
interface Audio { String play(); }
interface Video { String stream(); }

class Media implements Audio, Video {                          // adapts both ways
    private final String name;
    Media(String n) { name = n; }
    public String play()   { return "audio " + name; }
    public String stream() { return "video " + name; }
}
```

**5. Class Adapter (inheritance)**
```java
class LegacyLogger { void print(String s) { System.out.println(s); } }

class LegacyLoggerAdapter extends LegacyLogger implements AppLogger {
    public void log(String level, String msg) { print(level + " " + msg); }  // inherits adaptee
}
```

**Complexity:** O(1) per delegated call · Space O(1) per adapter

**Design note:** put the adapter at the **boundary** of your system so third-party types never leak into the domain. Pair with a [[../../../Creational/03 - Abstract Factory/Concept|Factory]] to choose the gateway at runtime.