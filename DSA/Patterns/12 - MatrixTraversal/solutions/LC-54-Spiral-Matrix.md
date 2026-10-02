---
solved: false
difficulty: Medium
pattern: Matrix Traversal
lc_number: 54
date_solved: 
tags:
  - dsa
  - matrix-traversal
  - medium
---
# Spiral Matrix (LC 54)

**Difficulty**: Medium  
**Pattern**: Matrix Traversal  
**LeetCode**: https://leetcode.com/problems/spiral-matrix/

## Problem Statement
Given an `m x n` matrix, return all elements of the matrix in spiral order.

**Example:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

## Approach: Layer by Layer (Simulation)

### Intuition
Maintain boundaries: `top, bottom, left, right`.
Iterate:
1. Left -> Right (increment top)
2. Top -> Bottom (decrement right)
3. Right -> Left (decrement bottom)
4. Bottom -> Top (increment left)
Check bounds after each sub-loop.

### Java Code
```java
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0) return result;
        
        int top = 0;
        int bottom = matrix.length - 1;
        int left = 0;
        int right = matrix[0].length - 1;
        
        while (top <= bottom && left <= right) {
            // Traverse Right
            for (int i = left; i <= right; i++) {
                result.add(matrix[top][i]);
            }
            top++;
            
            // Traverse Down
            for (int i = top; i <= bottom; i++) {
                result.add(matrix[i][right]);
            }
            right--;
            
            if (top <= bottom) {
                // Traverse Left
                for (int i = right; i >= left; i--) {
                    result.add(matrix[bottom][i]);
                }
                bottom--;
            }
            
            if (left <= right) {
                // Traverse Up
                for (int i = bottom; i >= top; i--) {
                    result.add(matrix[i][left]);
                }
                left++;
            }
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(m * n)
- **Space**: O(1)

## Key Takeaways
- Careful boundary management
- `if (top <= bottom)` check before traversing left (to avoid duplicate row processing)
