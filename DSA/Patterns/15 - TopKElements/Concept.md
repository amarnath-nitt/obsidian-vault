# Top K Elements — Concept

## What Is It?

Top K Elements uses a **Heap (PriorityQueue)** to efficiently find the K largest, smallest, or most frequent elements. A min-heap of size K keeps only the top K elements, achieving O(n log k) instead of O(n log n).

---

## When to Use

> **Trigger keywords:** "k largest", "k smallest", "k most frequent", "k closest", "merge k sorted", "median from stream"

---

## Variants

### 1. Kth Largest (Min-Heap of size K)
```java
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
for (int num : nums) {
    minHeap.offer(num);
    if (minHeap.size() > k) minHeap.poll();
}
return minHeap.peek(); // Kth largest
```

### 2. K Most Frequent (Frequency Map + Heap)
```java
Map<Integer, Integer> freq = new HashMap<>();
for (int num : nums) freq.merge(num, 1, Integer::sum);

PriorityQueue<Integer> heap = new PriorityQueue<>(
    (a, b) -> freq.get(a) - freq.get(b)
);
for (int key : freq.keySet()) {
    heap.offer(key);
    if (heap.size() > k) heap.poll();
}
```

### 3. Merge K Sorted Lists
```java
PriorityQueue<ListNode> heap = new PriorityQueue<>(
    (a, b) -> a.val - b.val
);
for (ListNode list : lists) {
    if (list != null) heap.offer(list);
}
while (!heap.isEmpty()) {
    ListNode node = heap.poll();
    // add to result
    if (node.next != null) heap.offer(node.next);
}
```

---

## Time/Space Complexity

| Approach | Time | Space |
|----------|------|-------|
| Heap of size K | O(n log k) | O(k) |
| Full sort | O(n log n) | O(n) |
| Quickselect | O(n) avg, O(n²) worst | O(1) |
| Merge K lists | O(N log k) | O(k) |

---

## Common Mistakes

1. **Min-heap vs Max-heap confusion** → For Kth **largest**, use **min-heap**; for Kth **smallest**, use **max-heap**
2. **Forgetting to limit heap size** → Poll when `heap.size() > k`
3. **Not handling null in merge K** → Filter null lists before adding to heap

---

## Related Patterns

- [[03 - FrequencyCounting/Concept|Frequency Counting]] — Count first, then heap for top K
- [[13 - MonotonicStack/Concept|Monotonic Stack]] — Alternative for streaming max/min

---

#heap #priority-queue #top-k #dsa #concept
