# M-Coloring Problem

**Problem:** Given an undirected graph and M colors, determine if the graph can be colored with M colors such that no two adjacent vertices have the same color.

### Approach

- Assign colors to vertices one by one
- For each vertex, try colors 1 to M
- Check if the color is safe (no adjacent vertex has same color)
- Backtrack if no color works

### Java Solution

```java
public class MColoring {
    static boolean isSafe(boolean[][] graph, int[] color, int vertex, int c, int n) {
        for (int i = 0; i < n; i++)
            if (graph[vertex][i] && color[i] == c) return false;
        return true;
    }

    static boolean solve(boolean[][] graph, int[] color, int vertex, int m, int n) {
        if (vertex == n) return true;
        for (int c = 1; c <= m; c++) {
            if (isSafe(graph, color, vertex, c, n)) {
                color[vertex] = c;
                if (solve(graph, color, vertex + 1, m, n)) return true;
                color[vertex] = 0; // backtrack
            }
        }
        return false;
    }

    static boolean graphColoring(boolean[][] graph, int m, int n) {
        int[] color = new int[n];
        return solve(graph, color, 0, m, n);
    }
}
```

**Complexity:** Time O(M^V) · Space O(V)

---
