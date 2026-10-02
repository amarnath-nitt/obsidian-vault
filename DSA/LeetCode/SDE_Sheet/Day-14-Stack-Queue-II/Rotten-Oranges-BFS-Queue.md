# Rotten Oranges (BFS + Queue)

**LeetCode 994** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/rotting-oranges/)

### Problem
Grid with fresh(1), rotten(2), empty(0) oranges. Each minute, rotten spreads to adjacent fresh. Find minimum minutes to rot all, or -1 if impossible.

### Approach (Multi-source BFS)

1. Add all initially rotten oranges to queue
2. BFS level by level (each level = 1 minute)
3. Count remaining fresh; if > 0 → return -1

### Java Solution

```java
class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int fresh = 0;

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) queue.offer(new int[]{i, j});
                if (grid[i][j] == 1) fresh++;
            }

        if (fresh == 0) return 0;

        int minutes = 0;
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        while (!queue.isEmpty()) {
            minutes++;
            for (int size = queue.size(); size > 0; size--) {
                int[] curr = queue.poll();
                for (int[] d : dirs) {
                    int r = curr[0] + d[0], c = curr[1] + d[1];
                    if (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] == 1) {
                        grid[r][c] = 2;
                        fresh--;
                        queue.offer(new int[]{r, c});
                    }
                }
            }
        }
        return fresh == 0 ? minutes - 1 : -1;
    }
}
```

**Complexity:** Time O(m×n) · Space O(m×n)

---
