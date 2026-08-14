# Range Sum Query 2D - Immutable (LC 304)

**Difficulty**: Medium  
**Pattern**: Prefix Sum  
**LeetCode**: https://leetcode.com/problems/range-sum-query-2d-immutable/

## Problem Statement
Given a 2D matrix `matrix`, handle multiple queries of the following type:
- Calculate the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.

**Example:**
```
Input: matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
sumRegion(2, 1, 4, 3) -> 8
```

## Approach: 2D Prefix Sum

### Intuition
`dp[i][j]` = sum of rectangle from `(0,0)` to `(i,j)`.
Formula: `dp[i][j] = matrix[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]` (inclusion-exclusion principle). OR (top + left - top left + current cell)
Sum Region `(r1, c1, r2, c2)` = `dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1]`. OR (total - top - left + top left)

### Java Code
```java
class NumMatrix {
    private int[][] prefixSum;

    public NumMatrix(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return;
        int m = matrix.length;
        int n = matrix[0].length;
        
        prefixSum = new int[m + 1][n + 1];
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefixSum[i][j] =  matrix[i-1][j-1] 
		                           + prefixSum[i][j - 1] 
		                           + prefixSum[i - 1][j] 
		                           - prefixSum[i-1][j-1];
            }
        }
    }
    
    public int sumRegion(int r1, int c1, int r2, int c2) {
        return prefixSum[r2 + 1][c2 + 1] 
               - prefixSum[r1][c2 + 1] 
               - prefixSum[r2 + 1][c1] 
               + prefixSum[r1][c1];
    }
}
```

### Complexity
- **Time**: O(mn) constructor, O(1) query
- **Space**: O(mn)

## Key Takeaways
- Extension of 1D prefix sum to 2D
- Inclusion-Exclusion principle handles overlap subtraction/addition
- +1 padding for DP array handles boundaries cleanly
