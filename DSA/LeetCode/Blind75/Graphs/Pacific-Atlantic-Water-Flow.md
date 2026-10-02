# Pacific Atlantic Water Flow

**Difficulty:** Medium
**Category:** Graphs
**LeetCode Link:** [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

---

## Problem Statement

Given an `m x n` matrix of heights, water can flow to adjacent cells (up/down/left/right) if the neighbor's height is ≤ current height. Water can flow to the Pacific (top/left edges) and Atlantic (bottom/right edges). Return all cells from which water can flow to both oceans.

**Example:**
```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

---

## Intuition

Instead of simulating water flowing downward from every cell (expensive), reverse the direction: start from ocean borders and flow upward (to equal or higher cells). Any cell reachable from both Pacific and Atlantic borders is an answer.

---

## Approach: Reverse DFS from Ocean Borders

### Algorithm
1. Create two boolean grids: `pacific` and `atlantic`
2. Run DFS from all Pacific border cells (top row + left column), marking reachable cells
3. Run DFS from all Atlantic border cells (bottom row + right column), marking reachable cells
4. Collect all cells where both grids are `true`

### Java Code
```java
class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();
        int m = heights.length, n = heights[0].length;

        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];

        // DFS from Pacific borders (top row + left column)
        for (int i = 0; i < m; i++) dfs(heights, pacific, i, 0);
        for (int j = 0; j < n; j++) dfs(heights, pacific, 0, j);

        // DFS from Atlantic borders (bottom row + right column)
        for (int i = 0; i < m; i++) dfs(heights, atlantic, i, n - 1);
        for (int j = 0; j < n; j++) dfs(heights, atlantic, m - 1, j);

        // Collect cells reachable from both
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }

        return result;
    }

    private void dfs(int[][] heights, boolean[][] visited, int i, int j) {
        visited[i][j] = true;
        int[][] dirs = {{0,1},{1,0},{0,-1},{-1,0}};

        for (int[] dir : dirs) {
            int ni = i + dir[0], nj = j + dir[1];
            if (ni >= 0 && ni < heights.length && nj >= 0 && nj < heights[0].length
                && !visited[ni][nj] && heights[ni][nj] >= heights[i][j]) {
                dfs(heights, visited, ni, nj);
            }
        }
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(m × n) — each cell visited at most twice
- **Space Complexity:** O(m × n) — two visited grids + recursion stack

---

## Key Takeaways

1. **Reverse flow:** Flow uphill from ocean borders instead of downhill from every cell
2. **Two separate DFS passes:** One per ocean, then intersect results
3. **Condition:** Move to neighbor only if `neighbor height >= current height` (reverse of water flow)

---

## Tags
#graphs #dfs #medium #blind75
