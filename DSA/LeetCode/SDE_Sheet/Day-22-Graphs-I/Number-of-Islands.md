# Number of Islands

**LeetCode 200** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/number-of-islands/)

### Approach

- DFS/BFS from each unvisited '1' cell
- Mark all connected '1's as visited
- Count the number of DFS/BFS calls

### Java Solution (DFS)

```java
class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length, n = grid[0].length, count = 0;

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
        return count;
    }

    private void dfs(char[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] != '1')
            return;
        grid[i][j] = '0'; // mark visited
        dfs(grid, i+1, j); dfs(grid, i-1, j);
        dfs(grid, i, j+1); dfs(grid, i, j-1);
    }
}
```

**Complexity:** Time O(m×n) · Space O(m×n) stack

---
