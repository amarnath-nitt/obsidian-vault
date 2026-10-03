# Design Traffic Signal Control System (Easy)

**Difficulty:** Easy · **Patterns:** State, Singleton
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a four-way intersection controller: exactly one axis green, all-red clearance, pedestrian requests, emergency override, night mode.

**Functional**
- 4 **signals** cycle NS-green → NS-yellow → all-red → EW-green → EW-yellow → all-red.
- **Pedestrian button** extends the next walk phase; **emergency** holds a green corridor then resumes; **night mode** flashes yellow.

**Non-functional**
- Two greens at once must be unrepresentable; tick source injectable for tests.

### The failure, before

```java
// ❌ Four booleans + a counter — emergency sets green NS without clearing EW,
// pedestrian mid-green is ignored or crashes, and night mode is an if in 8 places.
if (nsGreen && ewGreen) { /* illegal, but compiles */ }
```

### The Fix (after)

Controller + `Phase` states; each phase sets colours on entry and hands off on expiry.

```java
import java.util.*;

class Signal {
    private final String dir; private String colour = "RED";
    Signal(String dir) { this.dir = dir; }
    public void set(String c) { colour = c; }
    public String toString() { return dir + "=" + colour; }
}

interface Phase {
    void onEnter(SignalController c);
    void onTick(SignalController c);
}

class SignalController {
    private Phase phase;
    private final Map<String, Signal> signals = new LinkedHashMap<>();
    private int ticksLeft;
    private boolean pedWaiting;
    private Phase resumeAfterEmergency;

    SignalController() {
        for (String d : List.of("N", "S", "E", "W")) signals.put(d, new Signal(d));
        setPhase(new NSGreen(), 10);
    }
    public void setPhase(Phase p, int ticks) { phase = p; ticksLeft = ticks; p.onEnter(this); }
    public void tick() { if (--ticksLeft <= 0) phase.onTick(this); }
    public void green(String... dirs) {
        signals.values().forEach(s -> s.set("RED"));
        for (String d : dirs) signals.get(d).set("GREEN");
    }
    public void yellow(String... dirs) { for (String d : dirs) signals.get(d).set("YELLOW"); }
    public void pedestrian() { pedWaiting = true; }
    public boolean takePed() { boolean p = pedWaiting; pedWaiting = false; return p; }
    public void emergency(String dir) {
        resumeAfterEmergency = phase;
        if (dir.equals("N") || dir.equals("S")) setPhase(new EmergencyHold("N", "S"), 5);
        else setPhase(new EmergencyHold("E", "W"), 5);
    }
    void resume() { phase = resumeAfterEmergency; ticksLeft = 5; phase.onEnter(this); }
    public String status() { return signals.values().toString(); }
}

class NSGreen implements Phase {
    public void onEnter(SignalController c) { c.green("N", "S"); }
    public void onTick(SignalController c) { c.setPhase(new NSYellow(), 3); }
}
class NSYellow implements Phase {
    public void onEnter(SignalController c) { c.yellow("N", "S"); }
    public void onTick(SignalController c) { c.setPhase(new AllRed(true), 2); }
}
class AllRed implements Phase {
    private final boolean toEW;
    AllRed(boolean toEW) { this.toEW = toEW; }
    public void onEnter(SignalController c) { c.green(); /* all red */ }
    public void onTick(SignalController c) {
        if (toEW) c.setPhase(new EWGreen(), c.takePed() ? 14 : 10);
        else c.setPhase(new NSGreen(), c.takePed() ? 14 : 10);
    }
}
class EWGreen implements Phase {
    public void onEnter(SignalController c) { c.green("E", "W"); }
    public void onTick(SignalController c) { c.setPhase(new EWYellow(), 3); }
}
class EWYellow implements Phase {
    public void onEnter(SignalController c) { c.yellow("E", "W"); }
    public void onTick(SignalController c) { c.setPhase(new AllRed(false), 2); }
}
class EmergencyHold implements Phase {
    private final String[] dirs;
    EmergencyHold(String... dirs) { this.dirs = dirs; }
    public void onEnter(SignalController c) { c.green(dirs); }
    public void onTick(SignalController c) { c.resume(); }
}
```

**Usage**
```java
SignalController c = new SignalController();
for (int i = 0; i < 15; i++) c.tick();   // NS green -> yellow -> all-red -> EW green
c.pedestrian();                           // extends the next green
c.emergency("N"); for (int i = 0; i < 5; i++) c.tick();  // corridor, then resume
```

### Design points
- **All-red is a phase, not a gap** — the clearance has a duration and a successor; it cannot be skipped.
- **Colours change only in `onEnter`** — one mutation point; `onTick` only decides the handoff.
- **Pedestrian is a consumed flag** — set anytime, read once at the next green; never interrupts mid-phase.
- **Emergency captures resume** — hold stores the suspended phase; expiry returns to it.

**Complexity:** tick O(1) · Space O(signals).

---
#lld #machine-coding #traffic-signal #easy #practice
