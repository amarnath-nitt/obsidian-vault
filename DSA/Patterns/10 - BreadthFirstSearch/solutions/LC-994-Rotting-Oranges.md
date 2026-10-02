---
solved: false
difficulty: Medium
pattern: Breadth First Search
lc_number: 994
date_solved: 
tags:
  - dsa
  - breadth-first-search
  - medium
---
# Rotting Oranges (LC 994)

**Difficulty**: Medium  
**Pattern**: Breadth First Search  
**LeetCode**: https://leetcode.com/problems/rotting-oranges/

## Problem Statement
You are given an `m x n` grid where each cell can have one of three values:
- `0`: empty cell
- `1`: fresh orange
- `2`: rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

**Example 1:**
```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

## Approach: BFS (Multi-Source)

### Intuition
This is a multi-source BFS problem. We start BFS from ALL rotten oranges simultaneously. Each level of BFS corresponds to 1 minute of time.

### Java Code
```java
class Solution {
    public int orangesRotting(int[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        
        int rows = grid.length;
        int cols = grid[0].length;
        
        Queue<int[]> queue = new LinkedList<>();
        int freshCount = 0;
        
        // Initialize queue with all rotten oranges and count fresh ones
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                } else if (grid[i][j] == 1) {
                    freshCount++;
                }
            }
        }
        
        if (freshCount == 0) return 0;
        
        int minutes = 0;
        int[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            boolean infectedAny = false;
            
            for (int i = 0; i < size; i++) {
                int[] point = queue.poll();
                int r = point[0];
                int c = point[1];
                
                for (int[] dir : dirs) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];
                    
                    // Check boundaries and if fresh
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2; // Make it rotten
                        queue.offer(new int[]{nr, nc});
                        freshCount--;
                        infectedAny = true;
                    }
                }
            }
            
            if (infectedAny) minutes++;
        }
        
        return freshCount == 0 ? minutes : -1;
    }
}
```

### Complexity
- **Time**: O(m × n) - Visit each cell at most once
- **Space**: O(m × n) - Queue size

## Key Takeaways
- Multi-source BFS starts with multiple nodes in the queue
- Count fresh oranges initially to detect impossibility easily
- Modify grid in-place to track visited status
- Only increment time if actual infection happens in that level
