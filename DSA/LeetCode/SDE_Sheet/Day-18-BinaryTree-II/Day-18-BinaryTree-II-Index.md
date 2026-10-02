# Day 18 — Binary Tree II

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Binary Tree — Views, Boundary, Vertical Order
**Difficulty Mix:** Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Binary Tree Right Side View](Binary-Tree-Right-Side-View.md) | LeetCode 199 | Medium | [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/)
- [ ] [Bottom View of Binary Tree](Bottom-View-of-Binary-Tree.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Bottom+View+of+Binary+Tree)
- [ ] [Top View of Binary Tree](Top-View-of-Binary-Tree.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Top+View+of+Binary+Tree)
- [ ] [Vertical Order Traversal](Vertical-Order-Traversal.md) | LeetCode 987 | Hard | [LeetCode](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)
- [ ] [Boundary Traversal](Boundary-Traversal.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Boundary+Traversal)
- [ ] [Zigzag Level Order Traversal](Zigzag-Level-Order-Traversal.md) | LeetCode 103 | Medium | [LeetCode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Binary Tree Right Side View | Store full level order and take last node per level. O(n). | BFS and record last node of each level. | DFS right-first, add first node seen at each depth. O(n). |
| Bottom View of Binary Tree | Build every vertical list, then take deepest node. | BFS with horizontal distance and overwrite map entry. | TreeMap/min-max horizontal distance for ordered output. O(n log n) or O(n). |
| Top View of Binary Tree | Build every vertical list, then take first node. | BFS with horizontal distance and keep first entry only. | Track min/max horizontal distance to output without sorting where possible. |
| Vertical Order Traversal | Collect nodes, rows, columns, then sort. O(n log n). | BFS with nested maps/priority queues. | DFS/BFS collect triples and sort by column,row,value. O(n log n). |
| Boundary Traversal | Traverse all nodes and filter boundary afterward. | Separate left boundary, leaves, and reversed right boundary. | One clean pass per boundary part, avoiding duplicates. O(n). |
| Zigzag Level Order Traversal | BFS levels, then reverse alternate levels. O(n). | Deque insert front/back depending on level. | Fill an array by index direction per level. O(n). |

---

## Key Insight for View Problems

```
View Type        → What to extract from BFS/DFS
──────────────────────────────────────────────────
Right Side View  → Last node at each level
Left Side View   → First node at each level
Top View         → First node at each HD (BFS order)
Bottom View      → Last node at each HD (BFS order)
Vertical Order   → Sort by (col, row, val)
```

#sde-sheet #binary-tree #day18
