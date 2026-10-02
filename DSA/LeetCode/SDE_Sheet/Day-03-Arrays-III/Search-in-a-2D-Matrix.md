# Search in a 2D Matrix

**LeetCode 74** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/search-a-2d-matrix/)

### Problem
Matrix where each row is sorted and first integer of each row > last integer of previous row.
Search for a target value efficiently.

### Approach

**Key insight:** Treat the matrix as a **flattened sorted array** → apply Binary Search.

- Total elements: `m * n`
- `mid` element at position `p` → `matrix[p/n][p%n]`

### Java Solution

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int lo = 0, hi = m * n - 1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int val = matrix[mid / n][mid % n];
            if (val == target) return true;
            else if (val < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return false;
    }
}
```

**Complexity:** Time O(log(m×n)) · Space O(1)

> **Variant (LC 240):** Each row & column is sorted but not globally → start from top-right corner, move left or down.

---
