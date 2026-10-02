# Day 22 — Graphs I (BFS / DFS)

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Graph Fundamentals — BFS, DFS, Connected Components
**Difficulty Mix:** Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Number of Islands](Number-of-Islands.md) | LeetCode 200 | Medium | [LeetCode](https://leetcode.com/problems/number-of-islands/)
- [ ] [Clone Graph](Clone-Graph.md) | LeetCode 133 | Medium | [LeetCode](https://leetcode.com/problems/clone-graph/)
- [ ] [Flood Fill](Flood-Fill.md) | LeetCode 733 | Easy | [LeetCode](https://leetcode.com/problems/flood-fill/)
- [ ] [Detect Cycle in Undirected Graph](Detect-Cycle-in-Undirected-Graph.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Detect+Cycle+in+Undirected+Graph)
- [ ] [Detect Cycle in Directed Graph](Detect-Cycle-in-Directed-Graph.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Detect+Cycle+in+Directed+Graph)
- [ ] [Surrounded Regions](Surrounded-Regions.md) | LeetCode 130 | Medium | [LeetCode](https://leetcode.com/problems/surrounded-regions/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Number of Islands | For each land cell, search its component repeatedly. O((m*n)^2). | DFS/BFS with visited marking. O(m*n). | In-place marking or DSU for repeated/dynamic connectivity. |
| Clone Graph | Clone nodes, then search cloned neighbors repeatedly. O(V*E). | DFS/BFS with original-to-clone map. O(V+E). | Iterative BFS map avoids recursion-depth issues. O(V+E). |
| Flood Fill | Repeatedly scan the image for connected color changes. | DFS/BFS from source only. O(m*n). | Same with early return when new color equals old color. |
| Detect Cycle in Undirected Graph | Remove/check edges or try all paths. Costly. | DFS/BFS with parent tracking. O(V+E). | DSU detects an edge connecting an existing component. O(E alpha(V)). |
| Detect Cycle in Directed Graph | Start DFS from every node without memo. O(V*(V+E)). | DFS with recursion-stack/color states. O(V+E). | Kahn topological sort; leftover nodes imply cycle. O(V+E). |
| Surrounded Regions | For each O, search whether it reaches boundary. O((m*n)^2). | Mark boundary-connected O cells with DFS/BFS. O(m*n). | Union-Find with dummy boundary node. O(m*n alpha(m*n)). |

---

## Graph Representations

```java
// Adjacency List (most common)
List<List<Integer>> adj = new ArrayList<>();
for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
adj.get(u).add(v);
adj.get(v).add(u); // undirected

// BFS Template
void bfs(int start, List<List<Integer>> adj, boolean[] visited) {
    Queue<Integer> queue = new LinkedList<>();
    queue.offer(start);
    visited[start] = true;
    while (!queue.isEmpty()) {
        int node = queue.poll();
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                queue.offer(neighbor);
            }
        }
    }
}

// DFS Template
void dfs(int node, List<List<Integer>> adj, boolean[] visited) {
    visited[node] = true;
    for (int neighbor : adj.get(node)) {
        if (!visited[neighbor]) dfs(neighbor, adj, visited);
    }
}
```

---

## BFS vs DFS Decision Guide

| Use BFS when... | Use DFS when... |
|---|---|
| Shortest path (unweighted) | Cycle detection |
| Level-order traversal | Topological sort |
| Multi-source spreading | Connected components |
| Finding nearest neighbor | Finding all paths |

#sde-sheet #graphs #bfs #dfs #day22
