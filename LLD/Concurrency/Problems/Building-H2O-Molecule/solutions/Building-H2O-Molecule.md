# Building H2O Molecule (Barrier)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Pattern:** Barrier / rendezvous (2:1)
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/building-h2o)

### Problem

```java
class H2O {
    void hydrogen(Runnable releaseHydrogen);   // outputs "H"
    void oxygen(Runnable releaseOxygen);       // outputs "O"
}
```

The judge creates one thread per character of `water` (`3n` chars: exactly `2n` H, `n` O,
`1 <= n <= 20`). A thread must wait until a complete molecule can form: every consecutive group
of three outputs must contain exactly two H and one O, and all three atoms of one molecule bond
before any of the next. You coordinate the two methods; you don't create threads.

Example: `water = "HOH"` → `HHO` (any of `HHO`/`HOH`/`OHH` valid). `water = "HHOHHO"` →
e.g. `HOHHHO` — two consecutive valid triples.

### The failure, before

```java
// ❌ No coordination: scheduler order decides; an O can emit with zero or one H,
// and molecule boundaries drift — groups of three fail the 2H+1O check
public void hydrogen(Runnable r) { r.run(); }
public void oxygen(Runnable r)   { r.run(); }
```

### The Fix (after)

An **`hInMolecule` counter (0..2)** with oxygen as the **completer**.

```java
public class H2O {
    private final Object lock = new Object();
    private int hInMolecule = 0;                          // H bonded toward current molecule

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        synchronized (lock) {
            while (hInMolecule == 2) lock.wait();         // molecule full of H → wait for O
            releaseHydrogen.run();                        // "H"
            hInMolecule++;                                // 0→1→2
            lock.notifyAll();                             // O may now complete the molecule
        }
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        synchronized (lock) {
            while (hInMolecule < 2) lock.wait();          // WAIT for two Hs to bond with
            releaseOxygen.run();                          // "O" — molecule complete
            hInMolecule = 0;                              // open the next molecule
            lock.notifyAll();                             // wake the next H pair
        }
    }
}
```

**Usage**
```java
H2O h2o = new H2O();
// 2n threads call h2o.hydrogen(h); n threads call h2o.oxygen(o);
// output splits into triples, each with exactly 2 H and 1 O
```

### Design points
- **Oxygen completes** — it is gated on `hInMolecule == 2`, so a lone O can never emit.
- **Hydrogen is gated on `< 2`** — a third H can't leak into the next molecule before O closes
  the current one; molecule boundaries stay exact.
- **Reset is the barrier reuse** — `hInMolecule = 0` opens molecule `k+1` with no extra object.
- **`while`, not `if`** — a spurious wakeup must re-check, never bond a partial molecule.
- **State change + notify under one lock** — a woken thread always sees the fresh counter.

**Complexity:** O(1) per atom · Space O(1).

---
#concurrency #h2o #lld #practice
