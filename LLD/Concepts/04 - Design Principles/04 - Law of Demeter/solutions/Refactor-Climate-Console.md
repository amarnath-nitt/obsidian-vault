# Refactor Climate Console (Law of Demeter)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Principle:** Law of Demeter
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-climate-console)

### Problem

A climate console reads the temperature by **reaching through** a chain of objects:
`console.room().thermostat().sensor().celsius()`. Each link couples the console to an internal
structure it shouldn't know about. Apply the **Law of Demeter**: talk to your friends, not strangers.

### The Smell (before)

```java
// ❌ Reaching through four objects — brittle; any internal change breaks the console
class ClimateConsole {
    double temperature() {
        return building.getRoom("living").getThermostat().getSensor().getCelsius();
    }
    boolean isComfortable() {
        double t = building.getRoom("living").getThermostat().getSensor().getCelsius();  // duplicated chain
        return t >= 20 && t <= 24;
    }
}
```

### The Fix (after)

Add **delegating methods** so each object exposes what the caller needs, and the caller talks only to
its immediate collaborator.

```java
class Sensor {
    private double celsius;
    double celsius() { return celsius; }
}
class Thermostat {
    private final Sensor sensor;
    Thermostat(Sensor sensor) { this.sensor = sensor; }
    double currentTemperature() { return sensor.celsius(); }   // delegate, don't expose
}
class Room {
    private final Thermostat thermostat;
    Room(Thermostat thermostat) { this.thermostat = thermostat; }
    double temperature() { return thermostat.currentTemperature(); }
}
class Building {
    private final java.util.Map<String, Room> rooms;
    Building(java.util.Map<String, Room> rooms) { this.rooms = rooms; }
    double temperatureOf(String roomName) { return rooms.get(roomName).temperature(); }
}

// The console now talks to ONE friend — the building
class ClimateConsole {
    private final Building building;
    ClimateConsole(Building building) { this.building = building; }

    double temperature()     { return building.temperatureOf("living"); }
    boolean isComfortable()  { double t = temperature(); return t >= 20 && t <= 24; }
}
```

### Design points
- **No reaching through** — `ClimateConsole` calls only `building.temperatureOf(...)`.
- **Delegating methods** — each object hides its internals and answers its own question.
- **Fewer dependencies** — the console no longer knows about `Room`, `Thermostat`, or `Sensor`.
- **Easier changes** — restructuring `Room`/`Thermostat` does not break the console.

> **Law of Demeter:** a method should only call methods on: itself, its own fields, its parameters,
> objects it creates, or its components. `a.getB().getC().doSomething()` violates it.

**Complexity:** O(1) per read · Space O(1)

---
#design-principles #law-of-demeter #lld #practice