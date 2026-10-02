# Find Median from Data Stream

**LeetCode 295** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/find-median-from-data-stream/)

### Problem
Design a data structure that supports adding numbers and finding the median.

### Approach (Two Heaps)

- `maxHeap` (left half) — stores smaller half
- `minHeap` (right half) — stores larger half
- **Invariant:** `maxHeap.size() == minHeap.size()` or `maxHeap.size() == minHeap.size() + 1`
- Median: if sizes equal → average of tops; else → maxHeap top

### Java Solution

```java
class MedianFinder {
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder()); // left half
    PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // right half

    public void addNum(int num) {
        maxHeap.offer(num);
        minHeap.offer(maxHeap.poll()); // balance: push max of left to right

        if (minHeap.size() > maxHeap.size()) { // keep left >= right
            maxHeap.offer(minHeap.poll());
        }
    }

    public double findMedian() {
        if (maxHeap.size() > minHeap.size()) return maxHeap.peek();
        return (maxHeap.peek() + minHeap.peek()) / 2.0;
    }
}
```

**Complexity:** addNum O(log n) · findMedian O(1)

---
