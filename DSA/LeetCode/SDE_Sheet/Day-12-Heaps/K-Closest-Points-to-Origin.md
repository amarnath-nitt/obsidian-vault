# K Closest Points to Origin

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
