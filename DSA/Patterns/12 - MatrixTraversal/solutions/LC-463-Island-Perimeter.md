# Island Perimeter (LC 463)

**Difficulty**: Easy  
**Pattern**: Matrix Traversal  
**LeetCode**: https://leetcode.com/problems/island-perimeter/

## Problem Statement
You are given `row x col` `grid` representing a map where `grid[i][j] = 1` represents land and `grid[i][j] = 0` represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
Determine the perimeter of the island.

**Example:**
```
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
```

## Approach: Counting

### Intuition
Iterate through each cell.
If cell is land, add 4 to perimeter.
Then subtract for each neighbor that is also land (since they share an edge, that edge is not perimeter).
Optimization: Only check "Right" and "Down" neighbors. If neighbor is land, subtract 2 (one for current, one for neighbor).

### Java Code
```java
class Solution {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    perimeter += 4;
                    
                    // Check down neighbor
                    if (r + 1 < rows && grid[r + 1][c] == 1) {
                        perimeter -= 2;
                    }
                    
                    // Check right neighbor
                    if (c + 1 < cols && grid[r][c + 1] == 1) {
                        perimeter -= 2;
                    }
                }
            }
        }
        
        return perimeter;
    }
}
```

### Complexity
- **Time**: O(M * N)
- **Space**: O(1)

## Key Takeaways
- Contribution technique: +4 for land, -2 for shared edge
