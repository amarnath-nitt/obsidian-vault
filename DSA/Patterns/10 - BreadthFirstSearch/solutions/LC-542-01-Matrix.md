# 01 Matrix (LC 542)

**Difficulty**: Medium  
**Pattern**: Breadth-First Search  
**LeetCode**: https://leetcode.com/problems/01-matrix/

## Problem Statement
Given an `m x n` binary matrix `mat`, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

**Example:**
```
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
```

## Approach: Multi-Source BFS

### Intuition
Start BFS from *all* 0s simultaneously.
Initialize `dist` array with MAX_VALUE, set 0-cells to 0.
Queue initially contains all 0-cells.
Propagate distance layer by layer.

### Java Code
```java
class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int[][] dist = new int[m][n];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    queue.offer(new int[]{i, j});
                    dist[i][j] = 0;
                } else {
                    dist[i][j] = Integer.MAX_VALUE;
                }
            }
        }
        
        int[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];
            
            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    if (dist[nr][nc] > dist[r][c] + 1) {
                        dist[nr][nc] = dist[r][c] + 1;
                        queue.offer(new int[]{nr, nc});
                    }
                }
            }
        }
        
        return dist;
    }
}
```

### Complexity
- **Time**: O(m * n)
- **Space**: O(m * n)

## Key Takeaways
- Multi-source BFS for calculating distance from set of targets
- Avoid O(N^2) naive BFS from each cell
