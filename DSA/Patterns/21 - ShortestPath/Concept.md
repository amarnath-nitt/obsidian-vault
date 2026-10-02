# Shortest Path — Concept

## What Is It?

Shortest Path algorithms find the minimum-cost path between nodes in a **weighted graph**. The choice of algorithm depends on whether edges have negative weights and whether you need single-source or all-pairs.

---

## When to Use

> **Trigger keywords:** "shortest path", "minimum cost", "cheapest", "network delay", "weighted graph"

---

## Algorithm Selection

| Condition | Algorithm | Time |
|-----------|-----------|------|
| Unweighted graph | **BFS** | O(V + E) |
| Non-negative weights | **Dijkstra** | O((V+E) log V) |
| Negative weights, no negative cycles | **Bellman-Ford** | O(V × E) |
| At most K stops | **Bellman-Ford (K iterations)** | O(K × E) |
| All-pairs | **Floyd-Warshall** | O(V³) |

---

## Templates

### Dijkstra's Algorithm
```java
int[] dist = new int[n];
Arrays.fill(dist, Integer.MAX_VALUE);
dist[src] = 0;

// {distance, node}
PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
pq.offer(new int[]{0, src});

while (!pq.isEmpty()) {
    int[] curr = pq.poll();
    int d = curr[0], u = curr[1];
    
    if (d > dist[u]) continue; // skip outdated
    
    for (int[] edge : graph[u]) {
        int v = edge[0], w = edge[1];
        if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
            pq.offer(new int[]{dist[v], v});
        }
    }
}
```

### Bellman-Ford
```java
int[] dist = new int[n];
Arrays.fill(dist, Integer.MAX_VALUE);
dist[src] = 0;

for (int i = 0; i < n - 1; i++) {
    for (int[] edge : edges) { // [u, v, weight]
        if (dist[edge[0]] != Integer.MAX_VALUE
            && dist[edge[0]] + edge[2] < dist[edge[1]]) {
            dist[edge[1]] = dist[edge[0]] + edge[2];
        }
    }
}
```

---

## Visual Walkthrough

### Dijkstra on Network Delay
```
Graph: 1→2(1), 1→3(4), 2→3(2), 2→4(6), 3→4(3)

Start: node 1
dist = [0, ∞, ∞, ∞]

Process 1: update 2→1, 3→4    dist = [0, 1, 4, ∞]
Process 2: update 3→min(4,3)=3, 4→7  dist = [0, 1, 3, 7]
Process 3: update 4→min(7,6)=6  dist = [0, 1, 3, 6]

Network delay = max(dist) = 6
```

---

## Time/Space Complexity

| Algorithm | Time | Space |
|-----------|------|-------|
| BFS | O(V + E) | O(V) |
| Dijkstra (heap) | O((V+E) log V) | O(V) |
| Bellman-Ford | O(V × E) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |

---

## Common Mistakes

1. **Using Dijkstra with negative weights** → Use Bellman-Ford instead
2. **Not skipping outdated entries** → `if (d > dist[u]) continue` in Dijkstra
3. **Integer overflow** → Check `dist[u] != MAX_VALUE` before adding weight

---

## Related Patterns

- [[10 - BreadthFirstSearch/Concept|BFS]] — Shortest path in unweighted graphs
- [[11 - DepthFirstSearch/Concept|DFS]] — Not for shortest path, but for reachability
- [[20 - DynamicProgramming/Concept|Dynamic Programming]] — Bellman-Ford is essentially DP on graphs

---

#shortest-path #graph #dijkstra #dsa #concept
