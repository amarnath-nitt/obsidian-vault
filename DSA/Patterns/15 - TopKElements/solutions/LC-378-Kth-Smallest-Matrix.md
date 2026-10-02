---
solved: false
difficulty: Medium
pattern: Top KElements
lc_number: 378
date_solved: 
tags:
  - dsa
  - top-kelements
  - medium
---
# Kth Smallest Element in a Sorted Matrix (LC 378)

**Difficulty**: Medium  
**Pattern**: Top K Elements / Binary Search  
**LeetCode**: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

## Problem Statement
Given an `n x n` matrix where each of the rows and columns is sorted in ascending order, return the `k`th smallest element in the matrix.
Note that it is the `k`th smallest element in the sorted order, not the `k`th distinct element.
You must find a solution with a memory complexity better than `O(n^2)`.

**Example:**
```
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
```

## Approach 1: Min-Heap

### Intuition
Put first element of each row into Min-Heap.
Pop min, assume it came from row `r`, push `matrix[r][c+1]`.
Repeat `k` times.
Similar to "Merge k Sorted Lists".

### Java Code
```java
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        
        for (int i = 0; i < n; i++) {
            minHeap.offer(new int[]{matrix[i][0], i, 0});
        }
        
        for (int i = 0; i < k - 1; i++) {
            int[] curr = minHeap.poll();
            int val = curr[0];
            int r = curr[1];
            int c = curr[2];
            
            if (c + 1 < n) {
                minHeap.offer(new int[]{matrix[r][c + 1], r, c + 1});
            }
        }
        
        return minHeap.peek()[0];
    }
}
```

## Approach 2: Binary Search on Value

### Intuition
Range of answers: `[min(matrix), max(matrix)]`.
Guess a value `mid`. Count how many elements <= `mid`.
If `count < k`, answer must be larger (`low = mid + 1`).
Else, answer is `mid` or smaller (`high = mid`).

### Complexity
- **Time**: O(K log N) Heap, O(N log(Max-Min)) Binary Search
- **Space**: O(N) Heap, O(1) Binary Search

## Key Takeaways
- Heap approach treats matrix rows as sorted lists
- Binary Search on Value is powerful for "Kth smallest" where validation is easy
