# Day 12 — Heaps / Priority Queue

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Heaps · Priority Queue
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Kth Largest Element in Array](Kth-Largest-Element-in-Array.md) | LeetCode 215 | Medium | [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [ ] [Top K Frequent Elements](Top-K-Frequent-Elements.md) | LeetCode 347 | Medium | [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)
- [ ] [K Closest Points to Origin](K-Closest-Points-to-Origin.md) | LeetCode 973 | Medium | [LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/)
- [ ] [Merge K Sorted Lists](Merge-K-Sorted-Lists.md) | LeetCode 23 | Hard | [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)
- [ ] [Find Median from Data Stream](Find-Median-from-Data-Stream.md) | LeetCode 295 | Hard | [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/)
- [ ] [Task Scheduler](Task-Scheduler.md) | LeetCode 621 | Medium | [LeetCode](https://leetcode.com/problems/task-scheduler/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Kth Largest Element in Array | Sort and index. O(n log n). | Min-heap of size k. O(n log k). | Quickselect. O(n) average, O(1) extra space. |
| Top K Frequent Elements | Count, then sort by frequency. O(n log n). | Min-heap of size k over frequencies. O(n log k). | Bucket sort by frequency. O(n). |
| K Closest Points to Origin | Sort all points by distance. O(n log n). | Max-heap of size k. O(n log k). | Quickselect by squared distance. O(n) average. |
| Merge K Sorted Lists | Collect all values, sort, rebuild. O(N log N). | Merge lists one by one. O(k*N). | Min-heap of current list heads. O(N log k). |
| Find Median from Data Stream | Sort all numbers on every query. O(n log n). | Maintain sorted list with insertion. O(n) insert. | Two heaps: max-heap lower half, min-heap upper half. O(log n) add, O(1) median. |
| Task Scheduler | Simulate time slots directly. | Max-heap with cooldown queue. O(n log 26). | Math from max frequency and idle slots. O(n). |

---

## Heap Quick Reference

```java
// Min-heap (smallest at top)
PriorityQueue<Integer> minHeap = new PriorityQueue<>();

// Max-heap (largest at top)
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

// Custom comparator
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);

// Operations
pq.offer(x);  // add - O(log n)
pq.poll();    // remove top - O(log n)
pq.peek();    // view top - O(1)
pq.size();
```

---

## Heap Patterns

| Pattern | Heap Type | Use Case |
|---|---|---|
| Kth largest | Min-heap size k | Keep k largest |
| Kth smallest | Max-heap size k | Keep k smallest |
| Top-k frequent | Min-heap size k by freq | |
| Streaming median | Two heaps (max+min) | |
| Merge k sorted | Min-heap with (val, list) | |
| Sliding window max | Monotonic deque | |

#sde-sheet #heaps #priority-queue #day12
