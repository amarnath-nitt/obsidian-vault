# Kruskal's MST Algorithm

### Approach

1. Sort all edges by weight
2. Process edges in order, add to MST if it doesn't form a cycle (use DSU)
3. Stop when MST has V-1 edges

### Java Solution

```java
public int kruskalMST(int n, int[][] edges) {
    Arrays.sort(edges, (a, b) -> a[2] - b[2]); // sort by weight
    DSU dsu = new DSU(n);
    int totalWeight = 0, edgesUsed = 0;

    for (int[] edge : edges) {
        if (dsu.union(edge[0], edge[1])) { // no cycle
            totalWeight += edge[2];
            edgesUsed++;
            if (edgesUsed == n - 1) break; // MST complete
        }
    }
    return edgesUsed == n - 1 ? totalWeight : -1; // -1 if disconnected
}
```

**Complexity:** Time O(E log E) · Space O(V)

---
