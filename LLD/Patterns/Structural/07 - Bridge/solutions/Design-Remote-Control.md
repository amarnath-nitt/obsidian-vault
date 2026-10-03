# Design a Remote Control

**Source:** AlgoMaster · Low-Level Design Practice · **hard (premium)** · **Pattern:** Bridge
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

A **remote control** can operate many **devices** (TV, Radio, Speaker). Remotes come in flavours
(basic remote, advanced remote with extra features) and devices have different capabilities. Design
it so remotes and devices **vary independently** — a new device should not require a new remote, and
a new remote should work with every existing device.

### Approach — Bridge

- **Abstraction** = `Remote` (advanced remote refines it).
- **Implementor** = `Device` (TV, Radio, Speaker).
- The remote holds a `Device` reference — the bridge — and delegates every action.

### Java Solution

```java
// Implementor — the device dimension
interface Device {
    boolean isEnabled();
    void enable();
    void disable();
    int getVolume();
    void setVolume(int percent);
    String name();
}

class Tv implements Device {
    private boolean on; private int volume = 30;
    public boolean isEnabled() { return on; }
    public void enable()       { on = true; }
    public void disable()      { on = false; }
    public int getVolume()     { return volume; }
    public void setVolume(int v) { volume = Math.max(0, Math.min(100, v)); }
    public String name()       { return "TV"; }
}

class Radio implements Device {
    private boolean on; private int volume = 20;
    public boolean isEnabled() { return on; }
    public void enable()       { on = true; }
    public void disable()      { on = false; }
    public int getVolume()     { return volume; }
    public void setVolume(int v) { volume = Math.max(0, Math.min(100, v)); }
    public String name()       { return "Radio"; }
}

// Abstraction — the remote dimension
class Remote {
    protected final Device device;                 // ← the bridge
    Remote(Device device) { this.device = device; }

    String togglePower() {
        if (device.isEnabled()) device.disable(); else device.enable();
        return device.name() + (device.isEnabled() ? " on" : " off");
    }
    String volumeUp()   { device.setVolume(device.getVolume() + 10); return device.name() + " vol " + device.getVolume(); }
    String volumeDown() { device.setVolume(device.getVolume() - 10); return device.name() + " vol " + device.getVolume(); }
}

// RefinedAbstraction — an advanced remote adds features (e.g. mute)
class AdvancedRemote extends Remote {
    AdvancedRemote(Device device) { super(device); }
    String mute() { device.setVolume(0); return device.name() + " muted"; }
}
```

**Usage — any remote, any device**
```java
Remote basic = new Remote(new Tv());
System.out.println(basic.togglePower());     // TV on

AdvancedRemote adv = new AdvancedRemote(new Radio());
System.out.println(adv.mute());              // Radio muted
```

### Design points
- **Remotes and devices are independent hierarchies** — `Remote` never references `Tv`/`Radio` concretely.
- **Delegation, not inheritance** — `Remote` should not extend `Tv`.
- **New device = 1 class**; **new remote = 1 class** — no multiplicative growth.

**Complexity:** O(1) per command · Space O(1)

---
#bridge #lld #practice