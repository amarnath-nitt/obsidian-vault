# Number of Islands

**Difficulty:** Medium  
**Category:** Graphs  
**LeetCode Link:** [Number of Islands](https://leetcode.com/problems/number-of-islands/)

---

## Approach: DFS

### Java Code
```java
class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        
        return count;
    }
    
    private void dfs(char[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] != '1') {
            return;
        }
        
        grid[i][j] = '0';  // Mark as visited
        dfs(grid, i + 1, j);
        dfs(grid, i - 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i, j - 1);
    }
}
```

### Complexity
- **Time:** O(m × n)
- **Space:** O(m × n)

---

## Tags
#graphs #dfs #medium #blind75

---

## Visualization

- Embed: `![](../assets/number-of-islands/step-1.svg)`
- Obsidian embed: `![[../assets/number-of-islands/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="180">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <text x="20" y="28" fill="#222">Grid with islands (1) and water (0):</text>
    <g transform="translate(20,40)">
        <rect x="0" y="0" width="30" height="30" fill="#cfe8ff" stroke="#9cc3ff"/>
        <text x="15" y="20" text-anchor="middle">1</text>
        <rect x="34" y="0" width="30" height="30" fill="#f6f6f6" stroke="#ddd"/>
        <text x="49" y="20" text-anchor="middle">0</text>
        <rect x="68" y="0" width="30" height="30" fill="#cfe8ff" stroke="#9cc3ff"/>
        <text x="83" y="20" text-anchor="middle">1</text>
    </g>
</svg>
