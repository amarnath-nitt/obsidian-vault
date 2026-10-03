# Design a Beverage Station

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Template Method
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-beverage-station)

### Problem

A beverage station prepares different drinks by the same fixed sequence — boil water, brew, pour into
a cup, then optionally add condiments. The overall recipe must be fixed, but each drink supplies its
own brewing and condiment steps.

### Approach — Template Method

- `Beverage` defines the `final` `prepare()` skeleton.
- Abstract `brew()` / `addCondiments()` are the varying steps.
- `customerWantsCondiments()` is an optional **hook**.

### Java Solution

```java
abstract class Beverage {
    // Template method — the fixed recipe
    final void prepare() {
        boilWater();
        brew();                               // abstract step
        pourInCup();
        if (customerWantsCondiments()) {      // hook (optional)
            addCondiments();                  // abstract step
        }
        System.out.println("--- ready: " + name() + " ---");
    }

    abstract String name();
    protected abstract void brew();
    protected abstract void addCondiments();

    private void boilWater() { System.out.println("Boiling water"); }
    private void pourInCup() { System.out.println("Pouring into cup"); }
    protected boolean customerWantsCondiments() { return true; }   // default hook
}

class Tea extends Beverage {
    String name() { return "Tea"; }
    protected void brew()          { System.out.println("Steeping tea bag"); }
    protected void addCondiments() { System.out.println("Adding lemon"); }
}
class Coffee extends Beverage {
    String name() { return "Coffee"; }
    protected void brew()          { System.out.println("Dripping coffee"); }
    protected void addCondiments() { System.out.println("Adding milk & sugar"); }
    @Override protected boolean customerWantsCondiments() { return false; }   // overrides hook
}
class HotChocolate extends Beverage {
    String name() { return "Hot chocolate"; }
    protected void brew()          { System.out.println("Dissolving cocoa"); }
    protected void addCondiments() { System.out.println("Adding marshmallows"); }
}
```

**Usage**
```java
new Tea().prepare();
new Coffee().prepare();          // note: no condiments (hook overridden)
```

### Design points
- **Sequence locked** — `prepare()` is `final`, so subclasses cannot reorder the recipe.
- **Hollywood Principle** — the base class calls the subclass steps.
- **Hooks for optional steps** — `customerWantsCondiments()` has a sensible default.

**Complexity:** O(steps) per drink · Space O(1)

---
#template-method #lld #practice