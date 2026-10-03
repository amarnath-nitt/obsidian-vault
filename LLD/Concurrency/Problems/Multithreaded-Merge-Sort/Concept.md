# Multi-threaded Merge Sort — Concept

## What Is It?

A reusable sorter (`ParallelMergeSorter(maxThreads)`) that sorts an array in place with merge
sort, processing independent halves concurrently **without creating an unbounded number of
threads**. At most `maxThreads` participating threads (including the caller) may be active; when
no worker capacity is available the current thread continues **sequentially instead of waiting**.
An `onMerge` callback fires exactly once before every merge (`max(0, n-1)` times for length n)
so the judge can verify real parallel progress within the worker budget.

| | |
|---|---|
| **Pattern** | Fork-join with a worker budget (bounded parallelism) |
| **Core** | `Semaphore(permits)` as the worker budget; `tryAcquire` ⇒ fork, else ⇒ sequential |
| **Java** | `Semaphore` + `Thread` join (or `ExecutorService` with bounded pool) |

---

## When to Use

> **Trigger keywords:** "at most N threads", "may process concurrently", "continue sequentially if no capacity", "observation callback"

| Need | Move |
|------|------|
| Unbounded divide-and-conquer | naive fork per half (thread explosion) |
| **Bounded divide-and-conquer** | **permit-gated fork** — this package |
| Async task graphs with dependencies | thread pool / `CompletableFuture` DAG |

---

## The shape

```java
public final class ParallelMergeSorter {
    private final Semaphore budget;                 // worker permits (excludes the caller)

    public ParallelMergeSorter(int maxThreads) {
        this.budget = new Semaphore(Math.max(0, maxThreads - 1));
    }

    public void sort(int[] a, Runnable onMerge) throws InterruptedException {
        sortRange(a, 0, a.length, onMerge);
    }

    private void sortRange(int[] a, int lo, int hi, Runnable onMerge) throws InterruptedException {
        if (hi - lo <= 1) return;                   // one element: sorted
        int mid = (lo + hi) >>> 1;

        if (budget.tryAcquire()) {                  // capacity? fork the left half…
            Thread left = new Thread(() -> {
                try { sortRange(a, lo, mid, onMerge); }
                catch (InterruptedException e) { Thread.currentThread().interrupt(); }
                finally { budget.release(); }       // …and always pay the permit back
            });
            left.start();
            sortRange(a, mid, hi, onMerge);         // caller takes the right half
            left.join();                            // rendezvous before merging
        } else {
            sortRange(a, lo, mid, onMerge);         // no capacity? both halves sequential
            sortRange(a, mid, hi, onMerge);
        }

        onMerge.run();                              // exactly once, immediately before…
        merge(a, lo, mid, hi);                      // …every merge
    }

    private static void merge(int[] a, int lo, int mid, int hi) { /* standard merge */ }
}
```

**Why it works:** the semaphore counts *spare workers*. `tryAcquire` never blocks — it either
grants a fork (left half on a new thread, right half inline, `join` before merging) or declines
(both halves inline). Permits are always released, so the budget never leaks, and `onMerge`
fires once per internal node — exactly `n-1` times — regardless of the fork/sequential mix.

---

## Notes

- `maxThreads` **includes the caller** — the semaphore holds `maxThreads - 1` spare permits.
- Merge callbacks for disjoint ranges may overlap when `maxThreads > 1`, but never more than
  `maxThreads` may be active at once — the permit count enforces it structurally.
- The callback returns normally and never touches the array — pure observation hook.
- Same instance may sort again; `sort` is never called concurrently on one instance.

---

## Common Mistakes

1. `acquire()` (blocking) instead of `tryAcquire()` — threads pile up waiting for permits instead
   of doing the sequential work themselves.
2. Forgetting `release()` on an exception path → budget leak → later sorts go fully sequential.
3. `onMerge` after the merge (or skipped on the sequential path) → judge count mismatch.
4. Forking without `join` before `merge` → merging a half-sorted range.

---

## Related

- [[../00 - Index|Concurrency Problems Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../../Patterns/Thread-Pool-Pattern/Concept|Thread Pool Pattern]] · [[../../Concepts/Semaphores/Concept|Semaphores]]

---

#concurrency #merge-sort #lld #concept
