# Find Median from Data Stream

[Problem Link](https://leetcode.com/problems/find-median-from-data-stream/)

## Problem Statement
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
Design a data structure that supports the following operations:
- `void addNum(int num)` - Adds the integer `num` from the data stream to the data structure.
- `double findMedian()` - Returns the median of all elements so far.

## Approach
Use two heaps:
1.  **Max-Heap** (`lowerHalf`): Stores the smaller half of the numbers.
2.  **Min-Heap** (`upperHalf`): Stores the larger half of the numbers.
Balance constraints: `size(lowerHalf) == size(upperHalf)` or `size(lowerHalf) == size(upperHalf) + 1`.

- `addNum()`: Add to one of the heaps, then rebalance.
- `findMedian()`: If sizes are equal, average of tops. If `lowerHalf` has more, top of `lowerHalf`.

## Time and Space Complexity
- **Time Complexity:** O(log N) for `addNum`, O(1) for `findMedian`.
- **Space Complexity:** O(N).

## Code
```java
class MedianFinder {
    private PriorityQueue<Integer> lowerHalf; // Max heap for smaller numbers
    private PriorityQueue<Integer> upperHalf; // Min heap for larger numbers

    public MedianFinder() {
        lowerHalf = new PriorityQueue<>((a, b) -> b - a);
        upperHalf = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        if (lowerHalf.isEmpty() || num <= lowerHalf.peek()) {
            lowerHalf.offer(num);
        } else {
            upperHalf.offer(num);
        }
        
        // Rebalance
        if (lowerHalf.size() > upperHalf.size() + 1) {
            upperHalf.offer(lowerHalf.poll());
        } else if (upperHalf.size() > lowerHalf.size()) {
            lowerHalf.offer(upperHalf.poll());
        }
    }
    
    public double findMedian() {
        if (lowerHalf.size() == upperHalf.size()) {
            return (lowerHalf.peek() + upperHalf.peek()) / 2.0;
        } else {
            return lowerHalf.peek();
        }
    }
}
```
