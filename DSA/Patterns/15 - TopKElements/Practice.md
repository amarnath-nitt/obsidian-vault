# Top K Elements - Practice Notes

## Pattern Overview
Finding the top K largest or smallest elements using Heap (Priority Queue) data structure.

## Key Concepts
- **Min Heap**: Keep K largest elements (root is smallest of K largest)
- **Max Heap**: Keep K smallest elements (root is largest of K smallest)
- **Time Complexity**: O(n log k)
- **Space Complexity**: O(k)

## Template Code

### Top K Largest
```java
PriorityQueue<Integer> minHeap = new PriorityQueue<>();

for (int num : nums) {
    minHeap.offer(num);
    if (minHeap.size() > k) {
        minHeap.poll(); // Remove smallest
    }
}
// minHeap contains K largest elements
```

### Top K Smallest
```java
PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);

for (int num : nums) {
    maxHeap.offer(num);
    if (maxHeap.size() > k) {
        maxHeap.poll(); // Remove largest
    }
}
```

### Top K Frequent
```java
Map<Integer, Integer> freq = new HashMap<>();
for (int num : nums) {
    freq.put(num, freq.getOrDefault(num, 0) + 1);
}

PriorityQueue<Integer> heap = new PriorityQueue<>(
    (a, b) -> freq.get(a) - freq.get(b)
);

for (int num : freq.keySet()) {
    heap.offer(num);
    if (heap.size() > k) {
        heap.poll();
    }
}
```

## Practice Problems

### Easy
- [ ] [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) (LC 703) → [Solution](solutions/LC-703-Kth-Largest-Streaming.md)
- [ ] [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) (LC 1046) → [Solution](solutions/LC-1046-Last-Stone-Weight.md)

### Medium
- [ ] [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (LC 215) → [Solution](solutions/LC-215-Kth-Largest-Element.md)
- [ ] [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (LC 347) → [Solution](../FrequencyCounting/solutions/LC-347-Top-K-Frequent-Elements.md)
- [ ] [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) (LC 973) → [Solution](solutions/LC-973-K-Closest-Points.md)
- [ ] [Reorganize String](https://leetcode.com/problems/reorganize-string/) (LC 767) → [Solution](solutions/LC-767-Reorganize-String.md)
- [ ] [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) (LC 378) → [Solution](solutions/LC-378-Kth-Smallest-Matrix.md)
- [ ] [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) (LC 692) → [Solution](solutions/LC-692-Top-K-Frequent-Words.md) → [Solution](solutions/LC-378-Kth-Smallest-Matrix.md)
- [ ] [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) (LC 692) → [Solution](solutions/LC-692-Top-K-Frequent-Words.md)

### Hard
- [ ] [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) (LC 295) → [Solution](solutions/LC-295-Find-Median-Data-Stream.md)
- [ ] [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (LC 23) → [Solution](solutions/LC-23-Merge-k-Sorted-Lists.md)
- [ ] [IPO](https://leetcode.com/problems/ipo/) (LC 502) → [Solution](solutions/LC-502-IPO.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gFPPYc6w)
