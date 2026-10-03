# Building H2O Molecule — Concept

## What Is It?

Hydrogen threads call `hydrogen(releaseHydrogen)`, oxygen threads call `oxygen(releaseOxygen)`.
Coordinate them so threads pass a barrier in molecule groups — exactly **2 H + 1 O** per group —
and all three atoms of one molecule bond before any atom of the next begins.

| | |
|---|---|
| **Pattern** | Barrier / rendezvous with fixed stoichiometry (2:1) |
| **Core** | count H released toward the current molecule + `while` wait loop + `notifyAll()` |
| **Java** | `synchronized`, `wait/notifyAll` (or `Semaphore(2)` + `CyclicBarrier(3)`) |

---

## When to Use

> **Trigger keywords:** "groups of", "exactly two X and one Y", "bond before the next", "pass a barrier together"

| Need | Move |
|------|------|
| Fixed-size groups pass together | barrier counter + release-all on completion |
| **Fixed-ratio groups (2:1)** | **count the majority part; the minority part waits for a full set** — this package |
| Reusable N-thread rendezvous | `CyclicBarrier` / phased barrier |

---

## The shape

```java
public final class H2O {
    private final Object lock = new Object();
    private int hInMolecule = 0;            // H atoms released toward the current molecule (0..2)

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        synchronized (lock) {
            while (hInMolecule == 2) lock.wait();  // molecule full of H → wait for next one
            releaseHydrogen.run();                 // "H"
            hInMolecule++;
            lock.notifyAll();                      // an O may now complete the molecule
        }
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        synchronized (lock) {
            while (hInMolecule < 2) lock.wait();   // WAIT until two H are ready to bond
            releaseOxygen.run();                   // "O" — the molecule is now complete
            hInMolecule = 0;                       // open the next molecule
            lock.notifyAll();                      // wake the waiting H pair
        }
    }
}
```

**Why it works:** oxygen is the *completer* — it cannot proceed until two hydrogens have bonded,
and completing resets the counter so the next molecule starts clean. Every consecutive group of
three outputs is therefore `2H + 1O` in some order (`HHO`, `HOH`, `OHH` all valid).

---

## Notes

- The barrier resets via **counter reset**, not a reusable barrier object — simpler and exact.
- Hydrogen's `while (hInMolecule == 2)` blocks a *third* H from leaking into the next molecule
  before the oxygen closes the current one.
- Alternative: `Semaphore hSem(2)` + hydrogen acquires, oxygen acquires 2 then releases 2 — same
  stoichiometry, expressed with permits.
- `water.length == 3n` with exactly `2n` H and `n` O is guaranteed — no thread exits early.

---

## Common Mistakes

1. Oxygen without the `while (hInMolecule < 2)` gate → lone `O` with no partner Hs.
2. Forgetting to reset the counter → the second molecule never forms.
3. `if` instead of `while` → a spurious wakeup bonds a partial molecule.
4. Creating threads — the judge supplies one thread per atom; you coordinate the two methods.

---

## Related

- [[../00 - Index|Concurrency Problems Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../../Concepts/Semaphores/Concept|Semaphores]] · [[../../Patterns/Signaling-Pattern/Concept|Signaling Pattern]]

---

#concurrency #h2o #lld #concept
