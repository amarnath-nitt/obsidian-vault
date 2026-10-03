# Control a Home Theater

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Facade
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/control-home-theater)

### Problem

Watching a movie means turning on and configuring several devices in the right order: dim the lights,
turn on the projector, switch on the amplifier, set the volume, and start the DVD. Doing this by hand
couples the caller to every device. Provide a **facade** with a single `watchMovie()` / `endMovie()`
that orchestrates the subsystem.

### Approach — Facade

- Keep each device as its own class (unchanged subsystem).
- Add `HomeTheaterFacade` with coarse-grained `watchMovie(movie)` / `endMovie()` methods.
- The facade **delegates**; it does not implement device behaviour.

### Java Solution

```java
// Subsystem classes (unchanged)
class Amplifier {
    void on()  { System.out.println("Amp on"); }
    void off() { System.out.println("Amp off"); }
    void setVolume(int v) { System.out.println("Volume " + v); }
}
class Projector {
    void on()  { System.out.println("Projector on"); }
    void off() { System.out.println("Projector off"); }
}
class DvdPlayer {
    void on()  { System.out.println("DVD on"); }
    void off() { System.out.println("DVD off"); }
    void play(String movie) { System.out.println("Playing " + movie); }
    void stop() { System.out.println("DVD stop"); }
}
class Lights {
    void dim(int percent) { System.out.println("Lights " + percent + "%"); }
}

// Facade
class HomeTheaterFacade {
    private final Amplifier amp;
    private final Projector projector;
    private final DvdPlayer dvd;
    private final Lights lights;

    HomeTheaterFacade(Amplifier amp, Projector projector, DvdPlayer dvd, Lights lights) {
        this.amp = amp; this.projector = projector; this.dvd = dvd; this.lights = lights;
    }

    void watchMovie(String movie) {
        System.out.println("Get ready to watch a movie...");
        lights.dim(10);
        projector.on();
        amp.on();
        amp.setVolume(5);
        dvd.on();
        dvd.play(movie);
    }

    void endMovie() {
        System.out.println("Shutting the theater down...");
        dvd.stop();
        dvd.off();
        amp.off();
        projector.off();
        lights.dim(100);
    }
}
```

**Usage**
```java
HomeTheaterFacade theater = new HomeTheaterFacade(
        new Amplifier(), new Projector(), new DvdPlayer(), new Lights());
theater.watchMovie("Inception");
theater.endMovie();
```

### Design points
- **One call replaces many** — the caller no longer knows the device sequence.
- **Subsystem still available** — power users can drive devices directly.
- **Delegation, not logic** — the facade orders calls, it does not implement them.

**Complexity:** O(k) for k subsystem calls · Space O(1)

---
#facade #lld #practice