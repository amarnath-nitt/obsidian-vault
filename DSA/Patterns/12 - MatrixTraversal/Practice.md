# Matrix Traversal - Practice Notes

## Pattern Overview
Traversing 2D matrices/grids using DFS, BFS, or other techniques to solve grid-based problems.

## Key Concepts
- **DFS**: For island/region problems
- **BFS**: For shortest path in grids
- **Directions**: 4-directional or 8-directional movement
- **Time Complexity**: O(rows × cols)

## Template Code

### DFS on Matrix
```java
int[][] dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};

public void dfs(int[][] grid, int row, int col, boolean[][] visited) {
    int m = grid.length, n = grid[0].length;
    if (row < 0 || row >= m || col < 0 || col >= n || 
        visited[row][col]) {
        return;
    }
    
    visited[row][col] = true;
    
    for (int[] dir : dirs) {
        int newRow = row + dir[0];
        int newCol = col + dir[1];
        dfs(grid, newRow, newCol, visited);
    }
}
```

### BFS on Matrix
```java
int[][] dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};

public void bfs(int[][] grid, int startRow, int startCol) {
    int m = grid.length, n = grid[0].length;
    boolean[][] visited = new boolean[m][n];
    Queue<int[]> queue = new LinkedList<>();
    queue.offer(new int[]{startRow, startCol});
    visited[startRow][startCol] = true;
    
    while (!queue.isEmpty()) {
        int[] pos = queue.poll();
        int row = pos[0], col = pos[1];
        
        for (int[] dir : dirs) {
            int newRow = row + dir[0];
            int newCol = col + dir[1];
            
            if (newRow >= 0 && newRow < m && newCol >= 0 && 
                newCol < n && !visited[newRow][newCol]) {
                visited[newRow][newCol] = true;
                queue.offer(new int[]{newRow, newCol});
            }
        }
    }
}
```

## Practice Problems

### Easy
- [ ] [Flood Fill](https://leetcode.com/problems/flood-fill/) (LC 733) → [Solution](solutions/LC-733-Flood-Fill.md)
- [ ] [Island Perimeter](https://leetcode.com/problems/island-perimeter/) (LC 463) → [Solution](solutions/LC-463-Island-Perimeter.md)

### Medium
- [ ] [Number of Islands](https://leetcode.com/problems/number-of-islands/) (LC 200) → [Solution](solutions/LC-200-Number-of-Islands.md)
- [ ] [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) (LC 695) → [Solution](solutions/LC-695-Max-Area-of-Island.md)
- [ ] [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) (LC 994) → [Solution](../BreadthFirstSearch/solutions/LC-994-Rotting-Oranges.md)
- [ ] [01 Matrix](https://leetcode.com/problems/01-matrix/) (LC 542) → [Solution](../BreadthFirstSearch/solutions/LC-542-01-Matrix.md)
- [ ] [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) (LC 417) → [Solution](solutions/LC-417-Pacific-Atlantic-Water-Flow.md)
- [ ] [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) (LC 130) → [Solution](solutions/LC-130-Surrounded-Regions.md)
- [ ] [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) (LC 54) → [Solution](solutions/LC-54-Spiral-Matrix.md)
- [ ] [Rotate Image](https://leetcode.com/problems/rotate-image/) (LC 48) → [Solution](solutions/LC-48-Rotate-Image.md)
- [ ] [Word Search](https://leetcode.com/problems/word-search/) (LC 79) → [Solution](solutions/LC-79-Word-Search.md)

### Hard
- [ ] [Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/) (LC 305) → [Solution](solutions/LC-305-Number-of-Islands-II.md)
- [ ] [Shortest Path in a Grid with Obstacles Elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) (LC 1293) → [Solution](solutions/LC-1293-Shortest-Path-Obstacles.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gTzGdT93)
