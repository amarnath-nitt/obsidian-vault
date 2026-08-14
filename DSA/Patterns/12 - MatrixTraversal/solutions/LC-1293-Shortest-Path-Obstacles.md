# Shortest Path in a Grid with Obstacles Elimination

[Problem Link](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

## Problem Statement
You are given an `m x n` integer matrix `grid` where each cell is either `0` (empty) or `1` (obstacle). You can move up, down, left, or right from and to an empty cell.
Return the length of the shortest path to walk from `(0, 0)` to `(m - 1, n - 1)` eliminating at most `k` obstacles. If no such path exists, return `-1`.

## Approach
BFS with State (row, col, remaining_k).
State `(r, c, k)`: minimum steps to reach `(r, c)` with `k` eliminations left.
Use `visited[r][c]` storing max `k` remaining seen so far. If we reach `(r, c)` with fewer `k`, prune. Or simply `visited[r][c][k]`.
Optimization: If `k >= m + n - 2`, shortest path is Manhattan distance `m + n - 2` (ignoring all obstacles).

## Time and Space Complexity
- **Time Complexity:** O(M * N * K).
- **Space Complexity:** O(M * N * K).

## Code
```java
class Solution {
    public int shortestPath(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        
        if (k >= m + n - 2) return m + n - 2;
        
        // Queue: [row, col, k_remaining, steps]
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0, k, 0});
        
        boolean[][][] visited = new boolean[m][n][k + 1];
        visited[0][0][k] = true;
        
        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0], c = curr[1], curK = curr[2], steps = curr[3];
            
            if (r == m - 1 && c == n - 1) return steps;
            
            for (int[] d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];
                
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int nextK = curK - grid[nr][nc];
                    
                    if (nextK >= 0 && !visited[nr][nc][nextK]) {
                        visited[nr][nc][nextK] = true;
                        queue.offer(new int[]{nr, nc, nextK, steps + 1});
                    }
                }
            }
        }
        return -1;
    }
}
```
