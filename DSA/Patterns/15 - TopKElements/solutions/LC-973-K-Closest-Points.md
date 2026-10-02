---
solved: false
difficulty: Medium
pattern: Top KElements
lc_number: 973
date_solved: 
tags:
  - dsa
  - top-kelements
  - medium
---
# K Closest Points to Origin (LC 973)

**Difficulty**: Medium  
**Pattern**: Top 'K' Elements  
**LeetCode**: https://leetcode.com/problems/k-closest-points-to-origin/

## Problem Statement
Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.
The distance between two points on the X-Y plane is the Euclidean distance (i.e., `√(x1 - x2)² + (y1 - y2)²`).

**Example 1:**
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
Distance [1,3] is sqrt(10).
Distance [-2,2] is sqrt(8).
Since sqrt(8) < sqrt(10), [-2,2] is closer.
```

## Approach 1: Sorting

### Intuition
Calculate distance for all points, sort them, and pick the first k. We don't need actual square root for comparison, just `x² + y²`.

### Java Code
```java
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Arrays.sort(points, (a, b) -> {
            int distA = a[0]*a[0] + a[1]*a[1];
            int distB = b[0]*b[0] + b[1]*b[1];
            return distA - distB;
        });
        
        return Arrays.copyOfRange(points, 0, k);
    }
}
```

### Complexity
- **Time**: O(n log n)
- **Space**: O(log n) for sort

## Approach 2: Max-Heap (Optimized)

### Intuition
Use a Max-Heap of size k. Keep the k smallest distances found so far. The root will be the largest among the k closest, so if we find a closer point, we pop root and push new point.

### Java Code
```java
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // Max Heap: stores furthest points among the closest k
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> {
            int distA = a[0]*a[0] + a[1]*a[1];
            int distB = b[0]*b[0] + b[1]*b[1];
            return distB - distA; // Descending order
        });
        
        for (int[] point : points) {
            maxHeap.add(point);
            if (maxHeap.size() > k) {
                maxHeap.poll(); // Remove the furthest one
            }
        }
        
        int[][] result = new int[k][2];
        for (int i = 0; i < k; i++) {
            result[i] = maxHeap.poll();
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(n log k)
- **Space**: O(k)

## Key Takeaways
- Use Max-Heap to keep track of *smallest* k elements (keeps the limit on largest values)
- No need to compute square root for distance comparison
