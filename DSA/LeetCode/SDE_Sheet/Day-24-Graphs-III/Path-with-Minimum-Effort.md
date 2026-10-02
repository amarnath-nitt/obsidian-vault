# Path with Minimum Effort

**LeetCode 1631** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/path-with-minimum-effort/)

### Problem
Find path from top-left to bottom-right minimizing the maximum absolute difference.

### Approach (Dijkstra variant — "effort" = max diff along path)

```java
class Solution {
    public int minimumEffortPath(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        int[][] dist = new int[m][n];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        dist[0][0] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{0, 0, 0}); // [effort, row, col]
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int effort = curr[0], r = curr[1], c = curr[2];
            if (r == m-1 && c == n-1) return effort;
            if (effort > dist[r][c]) continue;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int newEffort = Math.max(effort, Math.abs(heights[nr][nc] - heights[r][c]));
                    if (newEffort < dist[nr][nc]) {
                        dist[nr][nc] = newEffort;
                        pq.offer(new int[]{newEffort, nr, nc});
                    }
                }
            }
        }
        return 0;
    }
}
```

---
