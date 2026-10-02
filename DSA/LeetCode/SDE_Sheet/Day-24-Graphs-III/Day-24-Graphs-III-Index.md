# Day 24 — Graphs III (Shortest Paths)

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Graph — Dijkstra, Bellman-Ford, Floyd-Warshall
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Dijkstra's Algorithm](Dijkstra-s-Algorithm.md) | LeetCode 743 | Medium | [LeetCode](https://leetcode.com/problems/network-delay-time/)
- [ ] [Bellman-Ford Algorithm](Bellman-Ford-Algorithm.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Bellman-Ford+Algorithm)
- [ ] [Floyd-Warshall (All Pairs)](Floyd-Warshall-All-Pairs.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Floyd-Warshall+%28All+Pairs%29)
- [ ] [Network Delay Time](Network-Delay-Time.md) | LeetCode 743 | Medium | [LeetCode](https://leetcode.com/problems/network-delay-time/)
- [ ] [Cheapest Flights Within K Stops](Cheapest-Flights-Within-K-Stops.md) | LeetCode 787 | Medium | [LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
- [ ] [Path with Minimum Effort](Path-with-Minimum-Effort.md) | LeetCode 1631 | Medium | [LeetCode](https://leetcode.com/problems/path-with-minimum-effort/)

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
