# Detect Cycle in Undirected Graph

### Approach (BFS / DFS with parent tracking)

- In undirected graph: cycle exists if we visit a visited node that is **not the parent**

```java
boolean hasCycleUndirected(int n, List<List<Integer>> adj) {
    boolean[] visited = new boolean[n];
    for (int i = 0; i < n; i++)
        if (!visited[i] && dfs(i, -1, adj, visited)) return true;
    return false;
}

boolean dfs(int node, int parent, List<List<Integer>> adj, boolean[] visited) {
    visited[node] = true;
    for (int neighbor : adj.get(node)) {
        if (!visited[neighbor]) {
            if (dfs(neighbor, node, adj, visited)) return true;
        } else if (neighbor != parent) return true; // back edge = cycle
    }
    return false;
}
```

---
