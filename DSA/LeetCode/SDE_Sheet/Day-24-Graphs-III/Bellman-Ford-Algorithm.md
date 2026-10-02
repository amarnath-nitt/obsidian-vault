# Bellman-Ford Algorithm

### Problem
Shortest path from source. Handles **negative weights**. Detects negative cycles.

### Approach

- Relax all edges **V-1 times** (longest shortest path can have V-1 edges)
- If any edge can be relaxed on the Vth iteration → negative cycle

### Java Solution

```java
public int[] bellmanFord(int src, int n, int[][] edges) {
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;

    for (int i = 0; i < n - 1; i++) { // V-1 iterations
        for (int[] edge : edges) { // [u, v, weight]
            int u = edge[0], v = edge[1], w = edge[2];
            if (dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    // Check for negative cycle
    for (int[] edge : edges) {
        int u = edge[0], v = edge[1], w = edge[2];
        if (dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v])
            throw new RuntimeException("Negative cycle detected!");
    }
    return dist;
}
```

**Complexity:** Time O(V×E) · Space O(V)

---
