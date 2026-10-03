# Print FooBar Alternately - Practice

## Key Concepts
- **Two threads strictly alternate** — one boolean turn flag is the whole design
- `while (wrong turn) wait()` + **flip the flag and `notifyAll()` under the same lock**
- The wait/notify sits **inside the per-iteration loop** — one handover per pair

## Common Moves in LLD
1. **Turn flag** — `fooTurn` records whose turn it is (durable state, survives early arrival)
2. **Loop of rendezvous** — each iteration waits, prints, hands over
3. **`notifyAll()`** — the other side re-checks its own predicate
4. **Exactly `n` callbacks each** — the loop bound is the contract

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Print FooBar Alternately](solutions/Print-FooBar-Alternately.md) — AlgoMaster · medium · Ordering — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/print-foobar-alternately)

---

## Extra Practice (self-study)

- [ ] Reimplement with a `Semaphore(1)` / `Semaphore(0)` pair instead of wait/notify
- [ ] Extend to three threads printing `foo-bar-baz` in rotation (hint: integer `step % 3`)

## Tips
- Say **"one boolean flag plus a wait loop inside the for-loop"** — that sentence is the answer
- **Signal-before-wait is the trap**: the flag makes early arrival safe
- Never create threads — the judge supplies them; you only coordinate the two methods
