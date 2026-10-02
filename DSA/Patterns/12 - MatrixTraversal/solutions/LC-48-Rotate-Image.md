---
solved: false
difficulty: Medium
pattern: Matrix Traversal
lc_number: 48
date_solved: 
tags:
  - dsa
  - matrix-traversal
  - medium
---
# Rotate Image (LC 48)

**Difficulty**: Medium  
**Pattern**: Matrix Traversal  
**LeetCode**: https://leetcode.com/problems/rotate-image/

## Problem Statement
You are given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

**Example:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

## Approach: Transpose then Reflect

### Intuition
Rotating 90 degrees clockwise can be achieved by:
1. Transpose the matrix (swap `matrix[i][j]` with `matrix[j][i]`).
2. Reverse each row (swap `matrix[i][j]` with `matrix[i][n-1-j]`).

### Java Code
```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        
        // Transpose
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) { // j starts at i+1 to avoid re-swapping
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        // Reflect (Reverse rows)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = temp;
            }
        }
    }
}
```

### Complexity
- **Time**: O(N^2)
- **Space**: O(1)

## Key Takeaways
- Linear Algebra trick: Rotation = Transpose + Reflection
- In-place modification requirement met
