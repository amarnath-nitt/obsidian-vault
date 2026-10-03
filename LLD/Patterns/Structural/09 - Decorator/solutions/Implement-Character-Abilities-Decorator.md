# Implement Character Abilities Decorator

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Decorator
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/implement-character-abilities-decorator)

### Problem

A game character has base stats and abilities. **Power-ups** (shield, invisibility, speed boost) can
be attached and removed dynamically, each altering the character's abilities/stats. Model this so
abilities can be **stacked at runtime** without editing the character class.

### Approach — Decorator

- **Component** = `Character` (`describe`, `powerLevel`, `hasAbility`).
- **ConcreteComponent** = `BaseCharacter`.
- **Decorator** = abstract `CharacterDecorator`.
- **ConcreteDecorators** = `Shield`, `Invisibility`, `SpeedBoost`.

### Java Solution

```java
import java.util.*;

interface Character {
    String description();
    int powerLevel();
    boolean hasAbility(String ability);
    Set<String> abilities();
}

class BaseCharacter implements Character {
    private final String name;
    BaseCharacter(String name) { this.name = name; }
    public String description()          { return name; }
    public int powerLevel()              { return 10; }
    public boolean hasAbility(String a)  { return false; }
    public Set<String> abilities()       { return Set.of(); }
}

abstract class CharacterDecorator implements Character {
    protected final Character inner;
    protected CharacterDecorator(Character inner) { this.inner = inner; }
    public String description()         { return inner.description(); }
    public int powerLevel()             { return inner.powerLevel(); }
    public boolean hasAbility(String a) { return inner.hasAbility(a); }
    public Set<String> abilities()      { return inner.abilities(); }
}

class Shield extends CharacterDecorator {
    Shield(Character c) { super(c); }
    public String description()         { return super.description() + " [Shield]"; }
    public int powerLevel()             { return super.powerLevel() + 5; }
    public boolean hasAbility(String a) { return a.equals("shield") || super.hasAbility(a); }
    public Set<String> abilities()      { return union(super.abilities(), "shield"); }
    private Set<String> union(Set<String> s, String a) { var t = new HashSet<>(s); t.add(a); return t; }
}

class Invisibility extends CharacterDecorator {
    Invisibility(Character c) { super(c); }
    public String description()         { return super.description() + " [Invisible]"; }
    public int powerLevel()             { return super.powerLevel() + 3; }
    public boolean hasAbility(String a) { return a.equals("invisibility") || super.hasAbility(a); }
    public Set<String> abilities()      { var t = new HashSet<>(super.abilities()); t.add("invisibility"); return t; }
}

class SpeedBoost extends CharacterDecorator {
    SpeedBoost(Character c) { super(c); }
    public String description()         { return super.description() + " [Fast]"; }
    public int powerLevel()             { return super.powerLevel() + 4; }
    public boolean hasAbility(String a) { return a.equals("speed") || super.hasAbility(a); }
    public Set<String> abilities()      { var t = new HashSet<>(super.abilities()); t.add("speed"); return t; }
}
```

**Usage**
```java
Character hero = new SpeedBoost(new Shield(new BaseCharacter("Ranger")));
System.out.println(hero.description());          // Ranger [Shield] [Fast]
System.out.println(hero.powerLevel());            // 19
System.out.println(hero.hasAbility("shield"));    // true
```

### Design points
- **Runtime stacking** — abilities are wrapped on, not compiled in.
- **Delegating decorators** — each adds to `powerLevel` and merges into `abilities`.
- **Same interface** — decorated and undecorated characters are interchangeable.

**Complexity:** O(depth) per query · Space O(depth + abilities)

---
#decorator #games #lld #practice