# Building H2O Molecule - Practice

## Key Concepts
- **Barrier with stoichiometry 2H + 1O** — oxygen is the *completer* that closes each molecule
- `hInMolecule` counter (0..2) + `while` wait loops + `notifyAll()` under one lock
- Completing the molecule **resets the counter** — that reset is the barrier reuse

## Common Moves in LLD
1. **Count the majority part** — H increments toward 2; a third H parks
2. **Gate the minority part** — O waits until two H are bonded and ready
3. **Reset on completion** — O emits, zeroes the counter, wakes the next H pair
4. **No partner matching needed** — any two H plus any O form a valid molecule

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Building H2O Molecule](solutions/Building-H2O-Molecule.md) — AlgoMaster · medium · Barrier — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/building-h2o)

---

## Extra Practice (self-study)

- [ ] Reimplement with `Semaphore(2)` for H plus a 3-party `CyclicBarrier`
- [ ] Generalise: `H2SO4` groups (2 H + 1 S + 4 O) — which part completes the molecule?

## Tips
- Say **"oxygen is the completer; the counter reset is the barrier"** — one sentence, full marks
- Any order inside the group is valid (`HHO`, `HOH`, `OHH`) — the judge checks groups of three, not positions
- Never create threads — the judge supplies one thread per atom character
