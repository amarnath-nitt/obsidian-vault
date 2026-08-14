# Day 12 — Heaps / Priority Queue

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Heaps · Priority Queue
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Kth Largest Element in Array]] | 215 | Medium | ⬜ |
| 2 | [[#Top K Frequent Elements]] | 347 | Medium | ⬜ |
| 3 | [[#K Closest Points to Origin]] | 973 | Medium | ⬜ |
| 4 | [[#Merge K Sorted Lists]] | 23 | Hard | ⬜ |
| 5 | [[#Find Median from Data Stream]] | 295 | Hard | ⬜ |
| 6 | [[#Task Scheduler]] | 621 | Medium | ⬜ |

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

## Kth Largest Element in Array

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

## Top K Frequent Elements

**LeetCode 347** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/top-k-frequent-elements/)

### Problem
Return k most frequent elements.

### Approach (Min-Heap + Frequency Map)

1. Build frequency map
2. Maintain min-heap of size k by frequency
3. Elements in heap are the top-k frequent

### Java Solution

```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int n : nums) freq.merge(n, 1, Integer::sum);

        // min-heap by frequency
        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> freq.get(a) - freq.get(b));
        for (int n : freq.keySet()) {
            heap.offer(n);
            if (heap.size() > k) heap.poll();
        }

        int[] result = new int[k];
        for (int i = 0; i < k; i++) result[i] = heap.poll();
        return result;
    }
}
```

**Complexity:** Time O(n log k) · Space O(n)

**Alternative:** Bucket Sort — O(n) time

```java
// Bucket approach
List<Integer>[] bucket = new List[nums.length + 1];
// ... fill buckets by frequency
// ... collect from end
```

---

## K Closest Points to Origin

**LeetCode 973** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/k-closest-points-to-origin/)

### Problem
Return k points closest to the origin.

### Approach (Max-Heap of size K)

- Keep a max-heap of size k by distance
- If heap exceeds k, remove the farthest

### Java Solution

```java
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // max-heap by distance squared
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (a, b) -> (b[0]*b[0] + b[1]*b[1]) - (a[0]*a[0] + a[1]*a[1])
        );

        for (int[] p : points) {
            maxHeap.offer(p);
            if (maxHeap.size() > k) maxHeap.poll();
        }

        return maxHeap.toArray(new int[0][]);
    }
}
```

**Complexity:** Time O(n log k) · Space O(k)

---

## Merge K Sorted Lists

**LeetCode 23** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/merge-k-sorted-lists/)

### Problem
Merge k sorted linked lists into one sorted list.

### Approach (Min-Heap)

- Add first node of each list to a min-heap
- Poll the minimum, add to result, push next node from that list

### Java Solution

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> heap = new PriorityQueue<>((a, b) -> a.val - b.val);

        for (ListNode node : lists)
            if (node != null) heap.offer(node);

        ListNode dummy = new ListNode(0), curr = dummy;
        while (!heap.isEmpty()) {
            ListNode node = heap.poll();
            curr.next = node;
            curr = curr.next;
            if (node.next != null) heap.offer(node.next);
        }
        return dummy.next;
    }
}
```

**Complexity:** Time O(N log k) where N = total nodes · Space O(k)

---

## Find Median from Data Stream

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

## Task Scheduler

**LeetCode 621** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/task-scheduler/)

### Problem
Schedule tasks with cooldown n. Find minimum intervals needed.

### Approach (Greedy + Math)

- Most frequent task determines the structure
- `minTime = (maxFreq - 1) * (n + 1) + countOfMaxFreq`
- Answer = `max(minTime, tasks.length)` (can't be less than total tasks)

### Java Solution

```java
class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] freq = new int[26];
        for (char t : tasks) freq[t - 'A']++;
        Arrays.sort(freq);

        int maxFreq = freq[25];
        int countOfMax = 0;
        for (int f : freq) if (f == maxFreq) countOfMax++;

        int minTime = (maxFreq - 1) * (n + 1) + countOfMax;
        return Math.max(minTime, tasks.length);
    }
}
```

**Complexity:** Time O(n) · Space O(1)

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
