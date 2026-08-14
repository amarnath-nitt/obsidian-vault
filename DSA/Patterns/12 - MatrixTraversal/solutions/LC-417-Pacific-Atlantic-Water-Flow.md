# Pacific Atlantic Water Flow (LC 417)

**Difficulty**: Medium  
**Pattern**: Matrix Traversal  
**LeetCode**: https://leetcode.com/problems/pacific-atlantic-water-flow/

## Existing Solution Reference
This problem is in Blind75: → [Solution](../../../LeetCode/Blind75/Graphs/Pacific-Atlantic-Water-Flow.md)

## Problem Statement
There is an `m x n` rectangular island that borders the **Pacific Ocean** and **Atlantic Ocean**.
- Pacific Ocean touches left and top edges.
- Atlantic Ocean touches right and bottom edges.

Rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates `result` where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to **both** the Pacific and Atlantic oceans.

## Approach: Two-Pass DFS/BFS from Oceans

### Intuition
Instead of simulation flow FROM each cell (inefficient), simulate flow from the oceans UP to the cells.
1. Find all cells reachable from Pacific (start from top/left edges, flow uphill).
2. Find all cells reachable from Atlantic (start from bottom/right edges, flow uphill).
3. The intersection of these two sets is the answer.

### Java Code
```java
class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();
        if (heights == null || heights.length == 0) return result;
        
        int m = heights.length;
        int n = heights[0].length;
        
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        
        // DFS from top and bottom
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j, Integer.MIN_VALUE);
            dfs(heights, atlantic, m-1, j, Integer.MIN_VALUE);
        }
        
        // DFS from left and right
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0, Integer.MIN_VALUE);
            dfs(heights, atlantic, i, n-1, Integer.MIN_VALUE);
        }
        
        // Find intersection
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        
        return result;
    }
    
    private void dfs(int[][] heights, boolean[][] visited, int r, int c, int prevHeight) {
        if (r < 0 || r >= heights.length || c < 0 || c >= heights[0].length || 
            visited[r][c] || heights[r][c] < prevHeight) {
            return;
        }
        
        visited[r][c] = true;
        
        dfs(heights, visited, r+1, c, heights[r][c]);
        dfs(heights, visited, r-1, c, heights[r][c]);
        dfs(heights, visited, r, c+1, heights[r][c]);
        dfs(heights, visited, r, c-1, heights[r][c]);
    }
}
```

### Complexity
- **Time**: O(m × n) - Two traversals
- **Space**: O(m × n) - Visited arrays

## Key Takeaways
- "Flow from ocean" strategy reduces complexity from O((mn)²) to O(mn)
- Need two visited arrays (one for each ocean)
- Flow uphill: `heights[curr] >= heights[prev]`
- Intersection of reachable sets is the answer
