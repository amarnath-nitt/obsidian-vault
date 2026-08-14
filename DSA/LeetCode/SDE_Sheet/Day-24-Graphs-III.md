# Day 24 — Graphs III (Shortest Paths)

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Graph — Dijkstra, Bellman-Ford, Floyd-Warshall
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Dijkstra's Algorithm]] | 743 | Medium | ⬜ |
| 2 | [[#Bellman-Ford Algorithm]] | — | Medium | ⬜ |
| 3 | [[#Floyd-Warshall (All Pairs)]] | — | Medium | ⬜ |
| 4 | [[#Network Delay Time]] | 743 | Medium | ⬜ |
| 5 | [[#Cheapest Flights Within K Stops]] | 787 | Medium | ⬜ |
| 6 | [[#Path with Minimum Effort]] | 1631 | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Dijkstra's Algorithm | Repeatedly scan all unvisited vertices for minimum distance. O(V^2). | Min-heap with adjacency list. O((V+E) log V). | Same heap version for sparse graphs; matrix scan can be best for dense graphs. |
| Bellman-Ford Algorithm | Enumerate paths up to V-1 edges. Exponential. | Relax all edges V-1 times. O(V*E). | Stop early if a pass makes no updates; extra pass detects negative cycles. |
| Floyd-Warshall | Run single-source shortest path from every node. O(V*E log V) or more. | DP over intermediate vertices. O(V^3). | In-place distance matrix update. O(V^3), O(1) extra. |
| Network Delay Time | Explore all possible paths from source. Exponential. | Dijkstra over directed weighted graph. O((V+E) log V). | Heap Dijkstra with adjacency list and max final distance. |
| Cheapest Flights Within K Stops | DFS every route up to k stops. Exponential. | Bellman-Ford style k+1 relaxations. O(k*E). | Priority queue/BFS state with stops and distance pruning. |
| Path with Minimum Effort | Enumerate all paths and take minimum max edge. Exponential. | Binary search effort and BFS reachability. O(E log W). | Dijkstra where path cost is max edge seen so far. O(E log V). |

---

## Dijkstra's Algorithm

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

## Bellman-Ford Algorithm

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

## Floyd-Warshall (All Pairs Shortest Path)

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

## Network Delay Time

**LeetCode 743** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/network-delay-time/)

### Problem
Find time for signal to reach all nodes from source k (weighted directed graph).

### Java Solution (Dijkstra)

```java
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for (int[] t : times) adj.get(t[0]).add(new int[]{t[1], t[2]});

        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{0, k});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            if (curr[0] > dist[curr[1]]) continue;
            for (int[] edge : adj.get(curr[1])) {
                int newDist = dist[curr[1]] + edge[1];
                if (newDist < dist[edge[0]]) {
                    dist[edge[0]] = newDist;
                    pq.offer(new int[]{newDist, edge[0]});
                }
            }
        }

        int maxDist = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == Integer.MAX_VALUE) return -1;
            maxDist = Math.max(maxDist, dist[i]);
        }
        return maxDist;
    }
}
```

---

## Cheapest Flights Within K Stops

**LeetCode 787** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

### Approach (Modified Bellman-Ford — K+1 iterations)

- Relax edges exactly **K+1 times** (K stops = K+1 edges)
- Use a **copy** of dist array to avoid using edges from same iteration

```java
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;

        for (int i = 0; i <= k; i++) { // K stops = K+1 edges
            int[] temp = Arrays.copyOf(dist, n);
            for (int[] flight : flights) {
                int u = flight[0], v = flight[1], w = flight[2];
                if (dist[u] != Integer.MAX_VALUE && dist[u] + w < temp[v])
                    temp[v] = dist[u] + w;
            }
            dist = temp;
        }
        return dist[dst] == Integer.MAX_VALUE ? -1 : dist[dst];
    }
}
```

**Complexity:** Time O(K×E) · Space O(V)

---

## Path with Minimum Effort

**LeetCode 1631** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/path-with-minimum-effort/)

### Problem
Find path from top-left to bottom-right minimizing the maximum absolute difference.

### Approach (Dijkstra variant — "effort" = max diff along path)

```java
class Solution {
    public int minimumEffortPath(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        int[][] dist = new int[m][n];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        dist[0][0] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{0, 0, 0}); // [effort, row, col]
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int effort = curr[0], r = curr[1], c = curr[2];
            if (r == m-1 && c == n-1) return effort;
            if (effort > dist[r][c]) continue;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int newEffort = Math.max(effort, Math.abs(heights[nr][nc] - heights[r][c]));
                    if (newEffort < dist[nr][nc]) {
                        dist[nr][nc] = newEffort;
                        pq.offer(new int[]{newEffort, nr, nc});
                    }
                }
            }
        }
        return 0;
    }
}
```

---

## Shortest Path Algorithm Selection

| Condition | Algorithm |
|---|---|
| Unweighted graph | BFS |
| Weighted, non-negative | Dijkstra O((V+E)logV) |
| Negative weights, no negative cycle | Bellman-Ford O(VE) |
| All-pairs shortest path | Floyd-Warshall O(V³) |
| DAG | Topo sort + DP O(V+E) |
| With constraint (K stops) | Modified Bellman-Ford |

#sde-sheet #graphs #shortest-paths #dijkstra #day24
