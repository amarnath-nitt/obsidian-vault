# Day 23 — Graphs II (Bipartite, Topological Sort)

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Graph — Bipartite Check, Topo Sort, SCCs
**Difficulty Mix:** Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Bipartite Graph Check](Bipartite-Graph-Check.md) | LeetCode 785 | Medium | [LeetCode](https://leetcode.com/problems/is-graph-bipartite/)
- [ ] [Topological Sort (Kahn's BFS)](Topological-Sort-Kahn-s-BFS.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Topological+Sort+%28Kahn%27s+BFS%29)
- [ ] [Course Schedule I](Course-Schedule-I.md) | LeetCode 207 | Medium | [LeetCode](https://leetcode.com/problems/course-schedule/)
- [ ] [Course Schedule II](Course-Schedule-II.md) | LeetCode 210 | Medium | [LeetCode](https://leetcode.com/problems/course-schedule-ii/)
- [ ] [Find Eventual Safe States](Find-Eventual-Safe-States.md) | LeetCode 802 | Medium | [LeetCode](https://leetcode.com/problems/find-eventual-safe-states/)
- [ ] [Alien Dictionary](Alien-Dictionary.md) | LeetCode 269 | Hard | [LeetCode](https://leetcode.com/problems/alien-dictionary/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Bipartite Graph Check | Try all 2-color assignments. Exponential. | BFS/DFS coloring and reject same-color edges. O(V+E). | Same coloring across all components; DSU parity is an alternative. |
| Topological Sort | Repeatedly scan all vertices for zero indegree. O(V^2+E). | Kahn BFS with a queue. O(V+E). | DFS postorder topo is the other O(V+E) standard. |
| Course Schedule I | Try to build every possible course order. Exponential. | DFS cycle detection with states. O(V+E). | Kahn indegree count; if processed count < V, cycle exists. |
| Course Schedule II | Try permutations until one satisfies prerequisites. Exponential. | DFS postorder, reverse result. O(V+E). | Kahn BFS produces valid order directly. O(V+E). |
| Find Eventual Safe States | DFS every path repeatedly. O(V*(V+E)). | DFS coloring/memo safe and unsafe states. O(V+E). | Reverse graph + topo from terminal nodes. O(V+E). |
| Alien Dictionary | Try alphabet orders and validate. Exponential. | Build precedence graph from adjacent words, then topo sort. | Kahn topo with invalid-prefix handling and all unique chars. |

---
