# Set Matrix Zeroes

**LeetCode 73** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/set-matrix-zeroes/)

### Problem
Given an `m x n` matrix, if an element is `0`, set its entire row and column to `0`.
Do it **in-place**.

### Approach

**Brute Force — O(m×n×(m+n)) time, O(1) space:**
- For each cell with 0, mark entire row and column with -1 (sentinel)
- Then convert all -1 to 0
- ⚠️ Breaks if original matrix contains -1

**Better — O(m×n) time, O(m+n) space:**
- Use two boolean arrays: `rowZero[m]` and `colZero[n]`
- First pass: mark rows and cols that have a zero
- Second pass: set cells to 0 based on markers

**Optimal — O(m×n) time, O(1) space:** ✅
- Use **first row and first column** as markers
- Track separately if row[0] or col[0] itself has zero

### Java Solution

```java
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean firstRowZero = false, firstColZero = false;

        // Check if first row has zero
        for (int j = 0; j < n; j++)
            if (matrix[0][j] == 0) firstRowZero = true;

        // Check if first col has zero
        for (int i = 0; i < m; i++)
            if (matrix[i][0] == 0) firstColZero = true;

        // Use first row/col as markers
        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }

        // Set zeros based on markers
        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;

        // Handle first row
        if (firstRowZero)
            for (int j = 0; j < n; j++) matrix[0][j] = 0;

        // Handle first col
        if (firstColZero)
            for (int i = 0; i < m; i++) matrix[i][0] = 0;
    }
}
```

**Complexity:** Time O(m×n) · Space O(1)

---
