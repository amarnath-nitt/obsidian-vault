# Day 19 — Binary Tree III

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Binary Tree — Paths, LCA, Max Path Sum
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Binary Tree Maximum Path Sum](Binary-Tree-Maximum-Path-Sum.md) | LeetCode 124 | Hard | [LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [ ] [Lowest Common Ancestor of Binary Tree](Lowest-Common-Ancestor-of-Binary-Tree.md) | LeetCode 236 | Medium | [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [ ] [Construct Tree from Preorder and Inorder](Construct-Tree-from-Preorder-and-Inorder.md) | LeetCode 105 | Medium | [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- [ ] [Serialize and Deserialize Binary Tree](Serialize-and-Deserialize-Binary-Tree.md) | LeetCode 297 | Hard | [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- [ ] [Flatten Binary Tree to Linked List](Flatten-Binary-Tree-to-Linked-List.md) | LeetCode 114 | Medium | [LeetCode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
- [ ] [Root to Node Path](Root-to-Node-Path.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Root+to+Node+Path)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Binary Tree Maximum Path Sum | Consider paths between many node pairs. O(n^2) or worse. | DFS returns max gain from each node. O(n). | Same DFS updates global best with left+node+right. |
| Lowest Common Ancestor of Binary Tree | Build root-to-node paths and compare. O(n) space. | Recursive search returns matching child/root. O(n). | Same one-pass recursion with O(h) stack. |
| Construct Tree from Preorder and Inorder | Recursively scan inorder to find root. O(n^2). | HashMap value to inorder index. O(n). | Pass index ranges, avoid array copies. O(n). |
| Serialize and Deserialize Binary Tree | Level-order with many null markers. O(n). | Preorder with null markers. O(n). | StringBuilder/queue parser to avoid costly string operations. |
| Flatten Binary Tree to Linked List | Store preorder nodes in a list, then relink. O(n) space. | Reverse preorder recursion with prev pointer. O(h) stack. | Morris-like rewiring using rightmost node of left subtree. O(1) extra. |
| Root to Node Path | Generate all root-to-leaf paths, then search. | DFS backtracking with early return. O(n). | Same, stopping as soon as target is found. |

---

## Tree Path Problems Summary

| Problem | Approach |
|---------|----------|
| Max path sum | DFS, return max gain, update global at each node |
| LCA | DFS, return non-null; if both sides non-null → LCA |
| Path to node | DFS with backtracking |
| All root-to-leaf paths | DFS, collect path, add when leaf |

#sde-sheet #binary-tree #day19
