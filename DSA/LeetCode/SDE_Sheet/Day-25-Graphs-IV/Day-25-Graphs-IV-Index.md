# Day 25 — Graphs IV (MST, DSU, Bridges)

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Graph — MST, Union-Find, Bridges, Articulation Points
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Disjoint Set Union (DSU / Union-Find)](Disjoint-Set-Union-DSU-Union-Find.md) | LeetCode — | Core DS | [LeetCode search](https://leetcode.com/problemset/?search=Disjoint+Set+Union+%28DSU+%2F+Union-Find%29)
- [ ] [Kruskal's MST Algorithm](Kruskal-s-MST-Algorithm.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Kruskal%27s+MST+Algorithm)
- [ ] [Prim's MST Algorithm](Prim-s-MST-Algorithm.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Prim%27s+MST+Algorithm)
- [ ] [Number of Operations to Make Network Connected](Number-of-Operations-to-Make-Network-Connected.md) | LeetCode 1319 | Medium | [LeetCode](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)
- [ ] [Accounts Merge](Accounts-Merge.md) | LeetCode 721 | Medium | [LeetCode](https://leetcode.com/problems/accounts-merge/)
- [ ] [Critical Connections (Bridges)](Critical-Connections-Bridges.md) | LeetCode 1192 | Hard | [LeetCode](https://leetcode.com/problems/critical-connections-in-a-network/)

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

## MST vs Shortest Path

| Problem | Algorithm |
|---------|-----------|
| Minimum spanning tree | Kruskal / Prim |
| Single-source shortest path | Dijkstra / Bellman-Ford |
| Connected components | DSU / DFS |
| Bridges / Articulation points | Tarjan's DFS |
| Dynamic connectivity | DSU |

#sde-sheet #graphs #mst #dsu #day25
