# Kth Largest Element in Array

**LeetCode 215** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/kth-largest-element-in-an-array/)

### Problem
Find the kth largest element.

### Approach 1 — Min-Heap of size K

- Maintain a min-heap of size k
- Heap top is always the kth largest

### Approach 2 — QuickSelect O(n) average

- Partition like QuickSort; recurse on the relevant half

### Java Solution (Min-Heap)

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int num : nums) {
            minHeap.offer(num);
            if (minHeap.size() > k) minHeap.poll();
        }
        return minHeap.peek();
    }
}
```

**Complexity:** Time O(n log k) · Space O(k)

---
