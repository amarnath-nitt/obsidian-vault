# Day 25 — Graphs IV (MST, DSU, Bridges)

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Graph — MST, Union-Find, Bridges, Articulation Points
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Disjoint Set Union (DSU / Union-Find)]] | — | Core DS | ⬜ |
| 2 | [[#Kruskal's MST Algorithm]] | — | Medium | ⬜ |
| 3 | [[#Prim's MST Algorithm]] | — | Medium | ⬜ |
| 4 | [[#Number of Operations to Make Network Connected]] | 1319 | Medium | ⬜ |
| 5 | [[#Accounts Merge]] | 721 | Medium | ⬜ |
| 6 | [[#Critical Connections (Bridges)]] | 1192 | Hard | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Disjoint Set Union | Answer connectivity by DFS/BFS each time. O(V+E) per query. | Quick union/find. | Path compression plus union by rank/size. Near O(1) amortized. |
| Kruskal's MST Algorithm | Try edge subsets and check spanning tree. Exponential. | Sort edges and add safe edges using DSU. O(E log E). | DSU with path compression/rank; stop after V-1 edges. |
| Prim's MST Algorithm | Grow MST by scanning all edges each step. O(V*E). | Adjacency matrix version. O(V^2). | Min-heap adjacency list. O(E log V). |
| Network Connected | DFS components and manually count spare edges. O(V+E). | DSU count components and redundant edges. | Early reject if edges < n-1, then DSU components. O(E alpha(V)). |
| Accounts Merge | Compare every pair of accounts for shared email. O(A^2*E). | Build email graph and DFS components. | DSU over emails/accounts, then collect sorted groups. |
| Critical Connections | Remove each edge and test connectivity. O(E*(V+E)). | Tarjan low-link DFS. O(V+E). | Same discovery/low arrays with parent edge handling. |

---

## Disjoint Set Union (DSU / Union-Find)

**The most important graph data structure to implement from scratch!**

### Implementation (with Path Compression + Union by Rank)

```java
class DSU {
    int[] parent, rank;

    DSU(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]); // path compression
        return parent[x];
    }

    boolean union(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false; // already same component
        if (rank[px] < rank[py]) { int tmp = px; px = py; py = tmp; }
        parent[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
        return true;
    }

    boolean connected(int x, int y) { return find(x) == find(y); }
}
```

**Complexity:** find/union ≈ O(α(n)) ≈ O(1) amortized (inverse Ackermann)

---

## Kruskal's MST Algorithm

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

## Prim's MST Algorithm

### Approach (Greedy + Min-Heap)

1. Start from any vertex, add it to MST
2. Use min-heap to always pick the minimum weight edge connecting MST to non-MST vertex
3. Add picked vertex to MST, add its edges to heap

### Java Solution

```java
public int primMST(int n, List<List<int[]>> adj) {
    boolean[] inMST = new boolean[n];
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    pq.offer(new int[]{0, 0}); // [weight, node]
    int totalWeight = 0;

    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int w = curr[0], node = curr[1];
        if (inMST[node]) continue;
        inMST[node] = true;
        totalWeight += w;
        for (int[] edge : adj.get(node)) {
            if (!inMST[edge[0]]) pq.offer(new int[]{edge[1], edge[0]});
        }
    }
    return totalWeight;
}
```

**Complexity:** Time O(E log V) · Space O(V+E)

---

## Number of Operations to Make Network Connected

**LeetCode 1319** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

### Problem
Minimum cable moves to connect all computers. Return -1 if not enough cables.

### Approach (DSU)

- Count connected components
- Need at least `n-1` cables to connect `n` computers
- Answer = number of components - 1

```java
class Solution {
    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) return -1; // not enough cables

        DSU dsu = new DSU(n);
        int components = n;
        for (int[] c : connections)
            if (dsu.union(c[0], c[1])) components--;

        return components - 1;
    }
}
```

---

## Accounts Merge

**LeetCode 721** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/accounts-merge/)

### Problem
Merge accounts that share common emails.

### Approach (DSU on emails)

1. Map each email to an account index
2. For each account, union all emails with the first email
3. Group emails by their root (representative)
4. Build result

```java
class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        DSU dsu = new DSU(accounts.size());
        Map<String, Integer> emailToAccount = new HashMap<>();

        for (int i = 0; i < accounts.size(); i++) {
            for (int j = 1; j < accounts.get(i).size(); j++) {
                String email = accounts.get(i).get(j);
                if (emailToAccount.containsKey(email)) {
                    dsu.union(i, emailToAccount.get(email));
                } else {
                    emailToAccount.put(email, i);
                }
            }
        }

        Map<Integer, List<String>> rootToEmails = new HashMap<>();
        for (Map.Entry<String, Integer> entry : emailToAccount.entrySet()) {
            int root = dsu.find(entry.getValue());
            rootToEmails.computeIfAbsent(root, k -> new ArrayList<>()).add(entry.getKey());
        }

        List<List<String>> result = new ArrayList<>();
        for (Map.Entry<Integer, List<String>> entry : rootToEmails.entrySet()) {
            List<String> emails = entry.getValue();
            Collections.sort(emails);
            emails.add(0, accounts.get(entry.getKey()).get(0)); // add name
            result.add(emails);
        }
        return result;
    }
}
```

---

## Critical Connections (Bridges)

**LeetCode 1192** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/critical-connections-in-a-network/)

### Problem
Find all bridges — edges whose removal disconnects the graph.

### Approach (Tarjan's Bridge Finding Algorithm)

- Maintain `disc[]` (discovery time) and `low[]` (lowest disc reachable)
- An edge `(u, v)` is a bridge if `low[v] > disc[u]`

```java
class Solution {
    List<List<Integer>> result = new ArrayList<>();
    int[] disc, low;
    int timer = 0;

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        disc = new int[n]; low = new int[n];
        Arrays.fill(disc, -1);
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (List<Integer> c : connections) {
            adj.get(c.get(0)).add(c.get(1));
            adj.get(c.get(1)).add(c.get(0));
        }
        dfs(0, -1, adj);
        return result;
    }

    void dfs(int u, int parent, List<List<Integer>> adj) {
        disc[u] = low[u] = timer++;
        for (int v : adj.get(u)) {
            if (disc[v] == -1) {
                dfs(v, u, adj);
                low[u] = Math.min(low[u], low[v]);
                if (low[v] > disc[u]) result.add(Arrays.asList(u, v)); // bridge
            } else if (v != parent) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
    }
}
```

**Complexity:** Time O(V+E) · Space O(V+E)

---

## MST vs Shortest Path

| Problem | Algorithm |
|---------|-----------|
| Minimum spanning tree | Kruskal / Prim |
| Single-source shortest path | Dijkstra / Bellman-Ford |
| Connected components | DSU / DFS |
| Bridges / Articulation points | Tarjan's DFS |
| Dynamic connectivity | DSU |

#sde-sheet #graphs #mst #dsu #day25
