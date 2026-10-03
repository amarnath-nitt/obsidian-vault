# Mutex - Practice

## Key Concepts
- **Only one thread in the critical section** at a time
- Java: `synchronized` (block-scoped, can't forget) or `ReentrantLock` (tryLock/timeout/fairness)
- Lock on a **`private final`** object; always unlock in **`finally`**

## Common Moves in LLD
1. **Pick the monitor first** — `private final Object lock = new Object()`
2. **`synchronized` for simple exclusion** — it's release-on-exit, exception-safe
3. **`ReentrantLock` when you need** `tryLock`, a timeout, fairness, or interruptibility
4. **Shrink the section** — no I/O, callbacks or `sleep()` while holding

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Thread-Safe Bank Account](solutions/Design-Thread-Safe-Bank-Account.md) — AlgoMaster · medium · Mutex — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-thread-safe-bank-account)

---

## Extra Practice (self-study)

- [ ] Rewrite a `synchronized` method using `ReentrantLock` + `try/finally`
- [ ] Find a lock on `this` in your codebase and replace it with a private final monitor

## Tips
- The bank-account trap is **linearizability of `withdraw`** — the balance check and the subtraction
  must be one atomic step, or two concurrent withdrawals overdraw the account
- Say **"private final monitor"** — it shows you've been burned by locking on `this`
- A mutex also establishes **happens-before**, so the next acquirer sees your writes
