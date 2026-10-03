# Condition Variables - Practice

## Key Concepts
- **Wait until a predicate becomes true** — park, let others run, wake on signal
- Four rules: **inside the lock · `while` not `if` · `wait()` releases the monitor · signal under the lock**
- A notification is **not durable** unless the condition is stored as state

## Common Moves in LLD
1. **Flag + loop** — `while (!ready) lock.wait();`
2. **Queue-depth condition** — `while (queue.isEmpty()) notEmpty.wait();`
3. **Versioned signal** — store a counter so late waiters still see progress
4. **`notifyAll()`** when waiters may have different predicates

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Versioned Signal](solutions/Design-Versioned-Signal.md) — AlgoMaster · medium · Condition Variables — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-versioned-signal)

---

## Extra Practice (self-study)

- [ ] Build a bounded buffer with `notEmpty`/`notFull` conditions
- [ ] Break it deliberately: change `while` to `if` and observe the missed wakeup

## Tips
- The **`while`-not-`if`** rule is the single most-asked condition-variable question
- *"Signals must be persistent"* is the insight behind the versioned-signal problem: state, not events
- `wait()` **releases** the monitor; `sleep()` does **not** — memorise the pair
