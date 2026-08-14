# Find Median from Data Stream

**Difficulty:** Hard  
**Category:** Heap / Priority Queue  
**LeetCode Link:** [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

---

## Problem Statement

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

Implement the MedianFinder class:
- `MedianFinder()` initializes the object.
- `void addNum(int num)` adds the integer `num` to the data structure.
- `double findMedian()` returns the median of all elements so far.

**Example:**
```
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Output
[null, null, null, 1.5, null, 2.0]
```

**Constraints:**
- `-10^5 <= num <= 10^5`
- At most `5 * 10^4` calls to `addNum` and `findMedian`.

---

## Intuition

Use two heaps: a max heap for the smaller half and a min heap for the larger half. The median is always at the top of one or both heaps.

---

## Approach 1: Sorting (Naive)

### Algorithm
1. Store all numbers in a list
2. Sort the list each time to find median

### Java Code
```java
class MedianFinder {
    private List<Integer> nums;
    
    public MedianFinder() {
        nums = new ArrayList<>();
    }
    
    public void addNum(int num) {
        nums.add(num);
    }
    
    public double findMedian() {
        Collections.sort(nums);
        int n = nums.size();
        if (n % 2 == 0) {
            return (nums.get(n/2 - 1) + nums.get(n/2)) / 2.0;
        } else {
            return nums.get(n/2);
        }
    }
}
```

### Complexity Analysis
- **addNum:** O(1)
- **findMedian:** O(n log n) - Sorting
- **Space:** O(n)

### Drawbacks
- ❌ Very slow for frequent median queries
- ❌ Sorting every time is wasteful

---

## Approach 2: Two Heaps (Optimized)

### Algorithm
1. **Max heap (left):** Stores smaller half of numbers
2. **Min heap (right):** Stores larger half of numbers
3. **Invariant:** Max heap size = Min heap size OR Max heap size = Min heap size + 1
4. **Median:** If sizes equal, average of two tops; else top of max heap

### Java Code
```java
class MedianFinder {
    private PriorityQueue<Integer> maxHeap;  // Smaller half
    private PriorityQueue<Integer> minHeap;  // Larger half
    
    public MedianFinder() {
        maxHeap = new PriorityQueue<>((a, b) -> b - a);  // Max heap
        minHeap = new PriorityQueue<>();                  // Min heap
    }
    
    public void addNum(int num) {
        // Add to max heap first
        maxHeap.offer(num);
        
        // Balance: ensure max heap's top <= min heap's top
        minHeap.offer(maxHeap.poll());
        
        // Balance sizes: max heap should have equal or one more element
        if (maxHeap.size() < minHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
    }
    
    public double findMedian() {
        if (maxHeap.size() > minHeap.size()) {
            return maxHeap.peek();
        } else {
            return (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
    }
}
```

### Complexity Analysis
- **addNum:** O(log n) - Heap operations
- **findMedian:** O(1) - Just peek at tops
- **Space:** O(n) - Store all numbers

### Why This is Better
- ✅ O(log n) insertion vs O(n log n) median finding
- ✅ O(1) median query
- ✅ Efficient for streaming data
- ✅ Maintains sorted order implicitly

---

## Key Takeaways

1. **Pattern:** Two heaps for running median
2. **Max heap:** Stores smaller half (top is largest of small)
3. **Min heap:** Stores larger half (top is smallest of large)
4. **Balance:** Keep sizes equal or differ by 1
5. **Median:** Always at heap tops

---

## Visual Example

After adding [1, 2, 3]:
```
MaxHeap (smaller half): [2, 1]  (max heap, so 2 on top)
MinHeap (larger half):  [3]

Median = 2 (top of max heap since it has more elements)
```

After adding 4:
```
MaxHeap: [2, 1]
MinHeap: [3, 4]

Median = (2 + 3) / 2 = 2.5
```

---

## Edge Cases

- Single element: Median is that element
- Two elements: Average of both
- Odd count: Top of max heap
- Even count: Average of both tops

---

## Tags
#heap #design #two-heaps #hard #blind75

---

## Visualization

- Embed: `![](../assets/find-median/step-1.svg)`
- Obsidian embed: `![[../assets/find-median/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="140">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <text x="20" y="28" fill="#222">Two heaps: maxHeap (left) and minHeap (right)</text>
    <g transform="translate(20,50)">
        <rect x="0" y="0" width="120" height="60" fill="#fff6e6" stroke="#d4a017"/>
        <text x="60" y="34" text-anchor="middle">maxHeap</text>
        <rect x="160" y="0" width="120" height="60" fill="#e6f7ff" stroke="#4b9be6"/>
        <text x="220" y="34" text-anchor="middle">minHeap</text>
    </g>
</svg>
