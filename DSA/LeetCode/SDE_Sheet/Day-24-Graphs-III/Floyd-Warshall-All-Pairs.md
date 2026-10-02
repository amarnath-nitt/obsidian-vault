# Floyd-Warshall (All Pairs)

### Approach

- DP: `dist[i][j]` = min distance from i to j
- For each intermediate vertex k: `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

### Java Solution

```java
public int[][] floydWarshall(int n, int[][] edges) {
    int[][] dist = new int[n][n];
    for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE / 2);
    for (int i = 0; i < n; i++) dist[i][i] = 0;
    for (int[] e : edges) dist[e[0]][e[1]] = e[2]; // for directed

    for (int k = 0; k < n; k++)       // intermediate
        for (int i = 0; i < n; i++)   // source
            for (int j = 0; j < n; j++) // destination
                dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);

    return dist;
}
```

**Complexity:** Time O(V³) · Space O(V²)

---
