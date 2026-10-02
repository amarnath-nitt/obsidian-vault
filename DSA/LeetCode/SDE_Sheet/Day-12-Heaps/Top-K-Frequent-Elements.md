# Top K Frequent Elements

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
