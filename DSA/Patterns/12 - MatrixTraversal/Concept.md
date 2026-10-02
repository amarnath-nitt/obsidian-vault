# Matrix Traversal — Concept

## What Is It?

Matrix Traversal applies BFS/DFS to 2D grids, treating each cell as a graph node connected to its 4 (or 8) neighbors. Common for island problems, shortest path in grids, and flood fill.

---

## When to Use

> **Trigger keywords:** "grid", "matrix", "island", "flood fill", "surrounded regions", "shortest path in grid"

---

## Template

```java
int[][] directions = {{0,1},{0,-1},{1,0},{-1,0}};

void dfs(int[][] grid, int r, int c, boolean[][] visited) {
    if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length
        || visited[r][c] || grid[r][c] == 0) return;
    
    visited[r][c] = true;
    for (int[] d : directions) {
        dfs(grid, r + d[0], c + d[1], visited);
    }
}
```

---

## Visual Walkthrough

### Number of Islands
```
Grid:            After DFS from (0,0):
1 1 0 0 0        X X 0 0 0
1 1 0 0 0   →    X X 0 0 0    Island #1
0 0 1 0 0        0 0 1 0 0
0 0 0 1 1        0 0 0 1 1

After DFS from (2,2):         After DFS from (3,3):
X X 0 0 0        X X 0 0 0
X X 0 0 0   →    X X 0 0 0
0 0 X 0 0        0 0 X 0 0    Island #3
0 0 0 1 1        0 0 0 X X

Answer: 3 islands
```

---

## Time/Space Complexity

| Metric | Complexity |
|--------|-----------|
| Time | O(m × n) |
| Space | O(m × n) for visited, O(m × n) worst-case stack |

---

## Common Mistakes

1. **Forgetting bounds check** → Always validate `r, c` before accessing `grid[r][c]`
2. **Not marking visited in BFS before enqueue** → Duplicate processing
3. **Modifying input grid** → Mark visited in-place (grid[r][c] = 0) or use separate array

---

## Related Patterns

- [[10 - BreadthFirstSearch/Concept|BFS]] — For shortest path in grid
- [[11 - DepthFirstSearch/Concept|DFS]] — For connected component counting
- [[21 - ShortestPath/Concept|Shortest Path]] — Weighted grid traversal

---

#matrix #grid #dsa #concept
