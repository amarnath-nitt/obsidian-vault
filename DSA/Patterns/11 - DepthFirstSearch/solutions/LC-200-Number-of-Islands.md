---
solved: false
difficulty: Medium
pattern: Depth First Search
lc_number: 200
date_solved: 
tags:
  - dsa
  - depth-first-search
  - medium
---
# Number of Islands

[Problem Link](https://leetcode.com/problems/number-of-islands/)

## Problem Statement
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Approach
DFS (or BFS).
1.  Iterate through every cell.
2.  If cell is `'1'`, it's a new island. Increment count.
3.  Call `dfs` to flood fill (mark as visited) all connected lands. We can change `'1'` to `'0'` to mark visited.

## Time and Space Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N) worst case stack space.

## Code
```java
class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }
    
    private void dfs(char[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] == '0') {
            return;
        }
        
        grid[i][j] = '0'; // Mark as visited
        
        dfs(grid, i + 1, j);
        dfs(grid, i - 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i, j - 1);
    }
}
```
