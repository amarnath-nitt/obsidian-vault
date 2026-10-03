# Multi-threaded Merge Sort (Parallel algorithm)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Pattern:** Bounded fork-join
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-parallel-merge-sorter)

### Problem

```java
class ParallelMergeSorter {
    ParallelMergeSorter(int maxThreads);         // 1..8 participating threads, caller included
    void sort(int[] values, Runnable onMerge);  // in-place nondecreasing sort, returns when done
}
```

Recursively halve, sort both halves, merge. Halves **may** run concurrently when worker capacity
is available; otherwise continue **sequentially in the current thread** (never wait for a slot).
Call `onMerge` exactly once immediately before every merge — `max(0, n-1)` times for length n
(4 elements ⇒ 3 merges). Disjoint-range callbacks may overlap when `maxThreads > 1`, but at most
`maxThreads` may be active at once. The callback returns normally and never touches `values`.
Reusable across calls; `sort` is never concurrent on one instance; instances independent.
`0 <= n <= 100_000`.

Example: `maxThreads = 4, values = [5,2,3,1]` → `[1,2,3,5]`, `onMerge` × 3.

### The failure, before

```java
// ❌ Fork per half with no budget: sorting 100k elements spawns ~200k threads —
// memory/OS exhaustion. And blocking acquire() for a permit parks threads that
// could just sort sequentially instead.
Thread l = new Thread(() -> sort(lo, mid)); l.start();   // unbounded!
Thread r = new Thread(() -> sort(mid, hi)); r.start();
```

### The Fix (after)

A **`Semaphore(maxThreads - 1)` budget** with **`tryAcquire` fork / sequential fallback**.

```java
import java.util.concurrent.Semaphore;

public final class ParallelMergeSorter {
    private final Semaphore budget;                     // spare workers beyond the caller

    public ParallelMergeSorter(int maxThreads) {
        if (maxThreads < 1) throw new IllegalArgumentException("maxThreads >= 1");
        this.budget = new Semaphore(maxThreads - 1);    // caller counts as a worker
    }

    public void sort(int[] values, Runnable onMerge) throws InterruptedException {
        sortRange(values, 0, values.length, onMerge);
    }

    private void sortRange(int[] a, int lo, int hi, Runnable onMerge) throws InterruptedException {
        if (hi - lo <= 1) return;
        int mid = (lo + hi) >>> 1;

        if (budget.tryAcquire()) {                      // capacity? fork left…
            Thread left = new Thread(() -> {
                try { sortRange(a, lo, mid, onMerge); }
                catch (InterruptedException e) { Thread.currentThread().interrupt(); }
                finally { budget.release(); }           // always repay, even on failure
            });
            left.start();
            sortRange(a, mid, hi, onMerge);             // caller sorts right inline
            left.join();                                // rendezvous BEFORE merging
        } else {
            sortRange(a, lo, mid, onMerge);             // no capacity? sequential, no waiting
            sortRange(a, mid, hi, onMerge);
        }

        onMerge.run();                                  // once, immediately before…
        merge(a, lo, mid, hi);                          // …every merge, on every path
    }

    private static void merge(int[] a, int lo, int mid, int hi) {
        int[] tmp = new int[hi - lo];
        int i = lo, j = mid, k = 0;
        while (i < mid && j < hi) tmp[k++] = (a[i] <= a[j]) ? a[i++] : a[j++];
        while (i < mid) tmp[k++] = a[i++];
        while (j < hi)  tmp[k++] = a[j++];
        System.arraycopy(tmp, 0, a, lo, tmp.length);
    }
}
```

**Usage**
```java
ParallelMergeSorter sorter = new ParallelMergeSorter(4);
// sorter.sort(new int[]{5, 2, 3, 1}, onMerge); → [1,2,3,5], onMerge × 3
// sorter.sort(other, onMerge);                 // reusable: budget fully repaid
```

### Design points
- **Budget = `maxThreads - 1`** — the calling thread is a participant, not overhead; with
  `maxThreads = 1` the trace is exactly sequential merge sort.
- **`tryAcquire` never blocks** — the fallback does useful sequential work instead of parking;
  thread count stays ≤ `maxThreads` structurally, not by luck.
- **`join` before `merge`** — both halves fully sorted before they combine; no half-sorted merge.
- **`onMerge` on every path** — forked or sequential, each internal node fires once ⇒ exactly
  `n-1` callbacks; the judge's parallelism check and count check both pass.
- **`release()` in `finally`** — exceptions repay the permit; the sorter stays reusable and later
  sorts still fork.

**Complexity:** O(n log n) work, O(n) temp per merge (reusable buffer possible) · Span O(n) worst / O((n log n)/maxThreads) typical · Space O(n + maxThreads).

---
#concurrency #merge-sort #lld #practice
