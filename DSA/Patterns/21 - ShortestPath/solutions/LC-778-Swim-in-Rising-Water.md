---
solved: false
difficulty: Hard
pattern: Shortest Path
lc_number: 778
date_solved: 
tags:
  - dsa
  - shortest-path
  - hard
---
# Swim in Rising Water (LC 778)

**Difficulty**: Hard  
**Pattern**: Shortest Path / Dijkstra  
**LeetCode**: https://leetcode.com/problems/swim-in-rising-water/

## Problem Statement
You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point (t).
At time `t`, the depth of water everywhere is `t`. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most `t`.
You start at `(0, 0)` and must reach `(n-1, n-1)`. Return the least time until you can reach the target.

**Example:**
```
Input: grid = [[0,2],[1,3]]
Output: 3
```

## Approach: Dijkstra (Min-Heap)

### Intuition
We want to minimize the *maximum* elevation encountered on the path.
Modified Dijkstra:
- Priority Queue stores `{max_elevation_on_path, r, c}`.
- Initially `{grid[0][0], 0, 0}`.
- Extract min. Update max elevation. Explore neighbors.
- Optimization: `visited` set to avoid cycles.

### Java Code
```java
class Solution {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        boolean[][] visited = new boolean[n][n];
        
        pq.offer(new int[]{grid[0][0], 0, 0}); // time, r, c
        visited[0][0] = true;
        
        int[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int time = curr[0];
            int r = curr[1];
            int c = curr[2];
            
            if (r == n - 1 && c == n - 1) return time;
            
            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    // The time needed to enter (nr, nc) is at least max(current_time, grid[nr][nc])
                    pq.offer(new int[]{Math.max(time, grid[nr][nc]), nr, nc});
                }
            }
        }
        
        return -1;
    }
}
```

### Complexity
- **Time**: O(N^2 log N)
- **Space**: O(N^2)

## Key Takeaways
- Path minimizing maximum edge weight -> Dijkstra or Union Find (MST)
- Weight is dynamic `max(path_max, current_node)`
