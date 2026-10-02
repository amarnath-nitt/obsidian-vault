# Detect Cycle in Directed Graph

### Approach (DFS with 3-color / recursion stack)

- `visited[v]` = false → unvisited
- `inStack[v]` = true → in current DFS path
- Back edge (neighbor is in stack) → cycle!

```java
boolean hasCycleDirected(int n, List<List<Integer>> adj) {
    boolean[] visited = new boolean[n], inStack = new boolean[n];
    for (int i = 0; i < n; i++)
        if (!visited[i] && dfs(i, adj, visited, inStack)) return true;
    return false;
}

boolean dfs(int node, List<List<Integer>> adj, boolean[] visited, boolean[] inStack) {
    visited[node] = inStack[node] = true;
    for (int neighbor : adj.get(node)) {
        if (!visited[neighbor] && dfs(neighbor, adj, visited, inStack)) return true;
        if (inStack[neighbor]) return true; // cycle
    }
    inStack[node] = false;
    return false;
}
```

---
