# Pacific Atlantic Water Flow

**Difficulty:** Medium  
**Category:** Graphs  
**LeetCode Link:** [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

---

## Approach: DFS from Oceans

### Java Code
```java
class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();
        int m = heights.length, n = heights[0].length;
        
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0);
            dfs(heights, atlantic, i, n - 1);
        }
        
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j);
            dfs(heights, atlantic, m - 1, j);
        }
        
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
            if (ni >= 0 && ni < heights.length && nj >= 0 && nj < heights[0].length &&
                !visited[ni][nj] && heights[ni][nj] >= heights[i][j]) {
                dfs(heights, visited, ni, nj);
            }
        }
    }
}
```

### Complexity
- **Time:** O(m × n)
- **Space:** O(m × n)

---

## Tags
#graphs #dfs #medium #blind75
