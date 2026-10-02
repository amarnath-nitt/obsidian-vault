# Dijkstra's Algorithm

**LeetCode 743** · Medium

### Problem
Find shortest path from source to all vertices in a weighted graph (non-negative weights).

### Approach (Min-Heap / Priority Queue)

1. Start with `dist[src] = 0`, all others = ∞
2. Use min-heap: `(distance, node)`
3. Pop minimum, relax all neighbors
4. Only process if current distance < recorded distance

### Java Solution

```java
public int[] dijkstra(int src, int n, List<List<int[]>> adj) {
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;

    // PQ: [distance, node]
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    pq.offer(new int[]{0, src});

    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int d = curr[0], node = curr[1];

        if (d > dist[node]) continue; // outdated entry

        for (int[] edge : adj.get(node)) {
            int neighbor = edge[0], weight = edge[1];
            if (dist[node] + weight < dist[neighbor]) {
                dist[neighbor] = dist[node] + weight;
                pq.offer(new int[]{dist[neighbor], neighbor});
            }
        }
    }
    return dist;
}
```

**Complexity:** Time O((V+E) log V) · Space O(V+E)

> ⚠️ Dijkstra fails with **negative weights** — use Bellman-Ford instead.

---
