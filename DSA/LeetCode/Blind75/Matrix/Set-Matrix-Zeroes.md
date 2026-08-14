# Set Matrix Zeroes

**Difficulty:** Medium  
**Category:** Matrix  
**LeetCode Link:** [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

---

## Problem Statement

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it **in place**.

**Example 1:**
```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2:**
```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

**Constraints:**
- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

---

## Intuition

We need to mark which rows and columns should be zeroed, then zero them. The challenge is doing this in-place without extra space.

---

## Approach 1: Extra Space (Naive)

### Algorithm
1. Use two sets to track rows and columns to zero
2. First pass: find all zeros, mark their rows/columns
3. Second pass: set marked rows/columns to zero

### Java Code
```java
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        Set<Integer> zeroRows = new HashSet<>();
        Set<Integer> zeroCols = new HashSet<>();
        
        // Find all zeros
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    zeroRows.add(i);
                    zeroCols.add(j);
                }
            }
        }
        
        // Set rows to zero
        for (int row : zeroRows) {
            for (int j = 0; j < n; j++) {
                matrix[row][j] = 0;
            }
        }
        
        // Set columns to zero
        for (int col : zeroCols) {
            for (int i = 0; i < m; i++) {
                matrix[i][col] = 0;
            }
        }
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m + n) - Two sets

---

## Approach 2: Use First Row/Column as Markers (Optimized)

### Algorithm
1. Use first row and first column to mark zeros
2. Use separate variables for first row and first column themselves
3. Process matrix using markers
4. Finally handle first row and column

### Java Code
```java
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean firstRowZero = false, firstColZero = false;
        
        // Check if first row should be zero
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                firstRowZero = true;
                break;
            }
        }
        
        // Check if first column should be zero
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true;
                break;
            }
        }
        
        // Use first row and column as markers
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;  // Mark row
                    matrix[0][j] = 0;  // Mark column
                }
            }
        }
        
        // Set zeros based on markers
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        
        // Handle first row
        if (firstRowZero) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }
        
        // Handle first column
        if (firstColZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(m × n)
- **Space Complexity:** O(1) - Only two boolean variables

### Why This is Better
- ✅ O(1) space vs O(m + n)
- ✅ In-place modification
- ✅ Clever use of existing matrix
- ✅ Meets the challenge requirement

---

## Key Takeaways

1. **Pattern:** Use matrix itself for storage
2. **First row/column:** Special handling needed
3. **Two passes:** Mark then modify
4. **Space optimization:** O(m+n) → O(1)

---

## Tags
#matrix #array #medium #blind75
