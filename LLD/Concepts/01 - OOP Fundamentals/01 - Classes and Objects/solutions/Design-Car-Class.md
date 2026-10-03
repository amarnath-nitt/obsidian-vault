# Design Car Class

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Topic:** Classes and Objects
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-car-class)

### Problem (contract)

Design a `Car` that remembers its identity (brand, model) and its current speed as it is driven.

- `Car(String brand, String model)` — every new car starts at **0 km/h**.
- `int accelerate(int amount)` — increases speed by `amount`, **stores** it, returns the new speed.
- `int brake(int amount)` — decreases speed by `amount`, stores it, returns the new speed; never below `0`.
- `int getSpeed()` — returns the current speed without changing it.
- `String describe()` — returns `"<brand> <model> at <speed> km/h"`.

All calls operate on the **same object** — state must be remembered between calls.

### Approach

- Model **identity** as `final` fields and **mutable state** (`speed`) as an instance field.
- A class is state + behaviour: the methods mutate the object's own state rather than returning a value
  computed from a parameter alone.

### Java Solution

```java
public class Car {

    private final String brand;      // identity — never changes
    private final String model;      // identity — never changes
    private int speed;               // mutable state, starts at 0

    public Car(String brand, String model) {
        this.brand = brand;
        this.model = model;
    }

    public int accelerate(int amount) { speed += amount;            return speed; }
    public int brake(int amount)      { speed = Math.max(0, speed - amount); return speed; }
    public int getSpeed()             { return speed; }

    public String describe() {
        return brand + " " + model + " at " + speed + " km/h";
    }
}
```

**Usage**
```java
Car car = new Car("Toyota", "Corolla");
car.describe();          // "Toyota Corolla at 0 km/h"
car.accelerate(20);      // 20
car.accelerate(15);      // 35  ← accumulates, does not replace
car.brake(100);          // 0   ← clamped at zero
```

### Design points
- **Constructor sets identity, not speed** — `speed` starts at `0` internally, not passed in.
- **State is stored** — `accelerate`/`brake` change the field and return the new value.
- **`getSpeed` is a pure read** — it observes without mutating.
- **`describe` reads live values** — never a stale copy.

**Complexity:** O(1) per operation · Space O(1)

---
#oop #classes #lld #practice