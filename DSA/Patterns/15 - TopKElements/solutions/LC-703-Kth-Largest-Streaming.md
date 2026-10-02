---
solved: false
difficulty: Easy
pattern: Top KElements
lc_number: 703
date_solved: 
tags:
  - dsa
  - top-kelements
  - easy
---
# Kth Largest Element in a Stream (LC 703)

**Difficulty**: Easy  
**Pattern**: Top K Elements / Heap  
**LeetCode**: https://leetcode.com/problems/kth-largest-element-in-a-stream/

## Problem Statement
Design a class to find the `k`th largest element in a stream. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.
Implement `KthLargest` class:
- `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)` Appends the integer `val` to the stream and returns the element representing the `k`th largest element in the stream.

**Example:**
```
Input: ["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output: [null, 4, 5, 5, 8, 8]
```

## Approach: Min-Heap

### Intuition
Maintain a Min-Heap of size `k`.
The root of the heap is the `k`th largest element seen so far.
When adding a new value, push to heap. If size > k, pop smallest.

### Java Code
```java
class KthLargest {
    private PriorityQueue<Integer> minHeap;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.minHeap = new PriorityQueue<>();
        for (int num : nums) {
            add(num);
        }
    }
    
    public int add(int val) {
        minHeap.offer(val);
        if (minHeap.size() > k) {
            minHeap.poll();
        }
        return minHeap.peek();
    }
}
```

### Complexity
- **Time**: O(log K) for add
- **Space**: O(K)

## Key Takeaways
- Classic application of Min-Heap for "Top K" streaming data
