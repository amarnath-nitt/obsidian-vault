# Number of Islands (LC 200)

**Difficulty**: Medium  
**Pattern**: Depth-First Search / Matrix Traversal  
**LeetCode**: https://leetcode.com/problems/number-of-islands/

## Existing Solution
This problem is solved in Blind75: → [Solution](../../../LeetCode/Blind75/Graphs/Number-of-Islands.md)

## Problem Statement
Given a 2D grid of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is formed by connecting adjacent lands horizontally or vertically.

**Example:**
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Approach 1: BFS

### Java Code
```java
class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    bfs(grid, i, j);
                }
            }
        }
        
        return count;
    }
    
    private void bfs(char[][] grid, int r, int c) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{r, c});
        grid[r][c] = '0';
        
        int[][] dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            
            for (int[] dir : dirs) {
                int nr = cell[0] + dir[0];
                int nc = cell[1] + dir[1];
                
                if (nr >= 0 && nr < grid.length && 
                    nc >= 0 && nc < grid[0].length && 
                    grid[nr][nc] == '1') {
                    queue.offer(new int[]{nr, nc});
                    grid[nr][nc] = '0';
                }
            }
        }
    }
}
```

### Complexity
- **Time**: O(m × n)
- **Space**: O(min(m, n)) - Queue size

## Approach 2: DFS (Optimized)

### Java Code
```java
class Solution {
    public int numIslands(char[][] grid) {
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
    
    private void dfs(char[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || 
            c < 0 || c >= grid[0].length || 
            grid[r][c] == '0') {
            return;
        }
        
        grid[r][c] = '0'; // Mark as visited
        
        dfs(grid, r+1, c);
        dfs(grid, r-1, c);
        dfs(grid, r, c+1);
        dfs(grid, r, c-1);
    }
}
```

### Complexity
- **Time**: O(m × n)
- **Space**: O(m × n) - Recursion stack worst case

## Key Takeaways
- DFS simpler and more intuitive than BFS for this problem
- Mark cells as visited by changing '1' to '0'
- Each island triggers one DFS traversal
- Classic grid traversal pattern
