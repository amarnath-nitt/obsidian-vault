# Max Area of Island (LC 695)

**Difficulty**: Medium  
**Pattern**: Matrix Traversal / DFS  
**LeetCode**: https://leetcode.com/problems/max-area-of-island/

## Problem Statement
You are given an `m x n` binary matrix `grid`. An island is a group of `1`s (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value `1` in the island.

Return the maximum area of an island in `grid`. If there is no island, return `0`.

**Example:**
```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],...]
Output: 6
```

## Approach 1: DFS

### Intuition
Iterate through the grid. When a '1' is found, start a DFS to compute the area of that island. Mark visited cells as '0' to avoid recounting. Keep track of maximum area.

### Java Code
```java
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        int m = grid.length;
        int n = grid[0].length;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    maxArea = Math.max(maxArea, dfs(grid, i, j));
                }
            }
        }
        
        return maxArea;
    }
    
    private int dfs(int[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] == 0) {
            return 0;
        }
        
        grid[r][c] = 0; // Mark visited
        
        return 1 + dfs(grid, r+1, c) + 
                   dfs(grid, r-1, c) + 
                   dfs(grid, r, c+1) + 
                   dfs(grid, r, c-1);
    }
}
```

### Complexity
- **Time**: O(m × n)
- **Space**: O(m × n)

## Key Takeaways
- Similar to "Number of Islands" but returns sum of nodes in component
- Modifying grid is efficient for visited tracking
- Return 0 for base cases, 1 + sum of neighbors for recursive step
