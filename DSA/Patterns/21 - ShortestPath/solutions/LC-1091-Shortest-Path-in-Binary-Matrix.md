# Shortest Path in Binary Matrix (LC 1091)

**Difficulty**: Medium  
**Pattern**: Shortest Path / BFS  
**LeetCode**: https://leetcode.com/problems/shortest-path-in-binary-matrix/

## Problem Statement
Given an `n x n` binary matrix `grid`, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (0, 0) to the bottom-right cell (n-1, n-1) such that:
1. All the visited cells of the path are 0.
2. All the adjacent cells of the path are 8-directionally connected.

**Example:**
```
Input: grid = [[0,1],[1,0]]
Output: 2
```

## Approach: BFS

### Intuition
Standard BFS finds shortest path in unweighted graphs.
8 directions instead of 4.
Level-by-level traversal ensures first time we reach target is shortest.

### Java Code
```java
class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;
        
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0});
        grid[0][0] = 1; // Mark visited by changing to 1
        
        int[][] dirs = {
            {-1,-1}, {-1,0}, {-1,1},
            {0,-1},          {0,1},
            {1,-1},  {1,0},  {1,1}
        };
        
        int pathLen = 1;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] curr = queue.poll();
                int r = curr[0];
                int c = curr[1];
                
                if (r == n - 1 && c == n - 1) return pathLen;
                
                for (int[] dir : dirs) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];
                    
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                        queue.offer(new int[]{nr, nc});
                        grid[nr][nc] = 1; // Mark visited
                    }
                }
            }
            pathLen++;
        }
        
        return -1;
    }
}
```

### Complexity
- **Time**: O(N^2)
- **Space**: O(N^2)

## Key Takeaways
- 8-directional BFS
- Modify input grid to save visited space (if allowed)
