# Design an Enemy Spawner

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Prototype
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-enemy-spawner)

### Problem (contract)

A game spawns enemies by **copying named prototypes**. A prototype goblin carries the health, speed
and loot every goblin starts with; each spawned goblin is a **copy** that then takes its own damage
and picks up its own loot.

Implement the prototype contract and the clone method:

- Declare `Prototype` with `clone()`; complete `Enemy.clone()`.
- `Enemy(type, health, speed, loot)` keeps the loot list it is given, exposes getters,
  `addLoot(item)`, `takeDamage(amount)` (never below 0) and
  `describe()` → `"Goblin (hp 30, speed 5) loot [dagger, coin]"`.
- `clone()` must return a **new** Enemy with the same type/health/speed and a **new loot list**
  holding the same items.
- The supplied `EnemySpawner` (registerPrototype / spawn / damage / addInstanceLoot / describe /
  instanceCount) must work unmodified.

### Approach

- A `Prototype` interface with `clone()`.
- `clone()` copies scalars by value and **deep-copies the loot list** so instances stay independent.

### Java Solution

```java
import java.util.*;

interface Prototype {
    Prototype clone();
}

class Enemy implements Prototype {

    private final String type;
    private int health;                 // mutated by damage
    private final int speed;
    private final List<String> loot;    // mutable per instance

    Enemy(String type, int health, int speed, List<String> loot) {
        this.type = type;
        this.health = health;
        this.speed = speed;
        this.loot = loot;               // keep the list it is given
    }

    public void addLoot(String item) { loot.add(item); }
    public void takeDamage(int amount) { health = Math.max(0, health - amount); }

    public String describe() {
        return type + " (hp " + health + ", speed " + speed + ") loot " + loot;
    }

    @Override
    public Enemy clone() {
        // scalars copied by value; loot is a NEW list holding the SAME items
        return new Enemy(type, health, speed, new ArrayList<>(loot));
    }
}
```

**Driver (provided — do not modify)**
```java
class EnemySpawner {
    private final Map<String, Enemy>     prototypes = new HashMap<>();
    private final Map<String, Enemy>     instances  = new HashMap<>();

    boolean registerPrototype(String name, String type, int health, int speed) {
        if (name.isEmpty() || health < 1 || prototypes.containsKey(name)) return false;
        prototypes.put(name, new Enemy(type, health, speed, new ArrayList<>()));
        return true;
    }
    boolean addLoot(String name, String item) {
        Enemy p = prototypes.get(name);
        if (p == null) return false;
        p.addLoot(item); return true;
    }
    boolean spawn(String name, String id) {
        Enemy p = prototypes.get(name);
        if (p == null || id.isEmpty() || instances.containsKey(id)) return false;
        instances.put(id, p.clone());          // ← your clone() does the copying
        return true;
    }
    boolean damage(String id, int amount) {
        Enemy e = instances.get(id);
        if (e == null || amount < 1) return false;
        e.takeDamage(amount); return true;
    }
    boolean addInstanceLoot(String id, String item) {
        Enemy e = instances.get(id);
        if (e == null) return false;
        e.addLoot(item); return true;
    }
    String describe(String id)          { Enemy e = instances.get(id);   return e == null ? "MISSING" : e.describe(); }
    String describePrototype(String n)  { Enemy e = prototypes.get(n);   return e == null ? "MISSING" : e.describe(); }
    int instanceCount() { return instances.size(); }
}
```

### Why it works
- **Scalars by value** — damage to one instance never touches the prototype or its siblings.
- **Loot list deep-copied** — `new ArrayList<>(loot)` gives each enemy its own list, so loot added to
  one instance never appears on others, and loot added to the prototype later never leaks back.
- **`clone()` is the single copy operation** — the spawner never copies fields itself.

**Complexity:** O(loot) per clone · Space O(loot) per instance

---
#prototype #games #lld #practice