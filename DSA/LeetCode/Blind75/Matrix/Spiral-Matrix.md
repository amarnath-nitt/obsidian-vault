# Spiral Matrix

**Difficulty:** Medium  
**Category:** Matrix  
**LeetCode Link:** [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

---

## Problem Statement

Given an `m x n` matrix, return all elements of the matrix in spiral order.

**Example 1:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

**Constraints:**
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`

---

## Intuition

Traverse the matrix in layers, moving right → down → left → up, shrinking boundaries after each direction.

---

## Approach: Four Boundaries

### Algorithm
1. Maintain four boundaries: top, bottom, left, right
2. Move in spiral: right, down, left, up
3. After each direction, shrink that boundary
4. Continue until all elements visited

### Java Code
```java
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0) return result;
        
        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;
        
        while (top <= bottom && left <= right) {
            // Move right
            for (int j = left; j <= right; j++) {
                result.add(matrix[top][j]);
            }
            top++;
            
            // Move down
            for (int i = top; i <= bottom; i++) {
                result.add(matrix[i][right]);
            }
            right--;
            
            // Move left (if still have rows)
            if (top <= bottom) {
                for (int j = right; j >= left; j--) {
                    result.add(matrix[bottom][j]);
                }
                bottom--;
            }
            
            // Move up (if still have columns)
            if (left <= right) {
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

### Complexity Analysis
- **Time Complexity:** O(m × n) - Visit each element once
- **Space Complexity:** O(1) - Not counting output array

---

## Key Takeaways

1. **Pattern:** Layer-by-layer traversal
2. **Four boundaries:** Track current layer limits
3. **Direction order:** Right → Down → Left → Up
4. **Edge cases:** Single row or column

---

## Tags
#matrix #simulation #medium #blind75
