---
solved: false
difficulty: Hard
pattern: Monotonic Stack
lc_number: 85
date_solved: 
tags:
  - dsa
  - monotonic-stack
  - hard
---
# Maximal Rectangle (LC 85)

**Difficulty**: Hard  
**Pattern**: Monotonic Stack  
**LeetCode**: https://leetcode.com/problems/maximal-rectangle/

## Problem Statement
Given a `rows x cols` binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

**Example:**
```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
```

## Approach: Histogram Max Area (LC 84)

### Intuition
Treat each row as the base of a histogram.
Height of bar at `col` increases if `matrix[row][col] == '1'`, resets to 0 if '0'.
For each row, solve "Largest Rectangle in Histogram" (LC 84) using Monotonic Stack.

### Java Code
```java
class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0) return 0;
        int n = matrix[0].length;
        int[] heights = new int[n];
        int maxArea = 0;
        
        for (char[] row : matrix) {
            // Update heights
            for (int i = 0; i < n; i++) {
                if (row[i] == '1') {
                    heights[i] += 1;
                } else {
                    heights[i] = 0;
                }
            }
            // Calculate max area for current row's histogram
            maxArea = Math.max(maxArea, largestRectangleArea(heights));
        }
        
        return maxArea;
    }
    
    private int largestRectangleArea(int[] heights) {
        int max = 0;
        Deque<Integer> stack = new ArrayDeque<>(); // Indices
        stack.push(-1);
        
        for (int i = 0; i < heights.length; i++) {
            while (stack.peek() != -1 && heights[stack.peek()] >= heights[i]) {
                int h = heights[stack.pop()];
                int w = i - stack.peek() - 1;
                max = Math.max(max, h * w);
            }
            stack.push(i);
        }
        
        while (stack.peek() != -1) {
            int h = heights[stack.pop()];
            int w = heights.length - stack.peek() - 1;
            max = Math.max(max, h * w);
        }
        
        return max;
    }
}
```

### Complexity
- **Time**: O(R * C)
- **Space**: O(C)

## Key Takeaways
- Reducing 2D problem to 1D Histogram problem
- Reusing LC 84 solution
