# Day 17 — Binary Tree I

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Binary Tree — Traversals, Height, Diameter
**Difficulty Mix:** Easy / Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Binary Tree Traversals (In/Pre/Post)](Binary-Tree-Traversals-In-Pre-Post.md) | LeetCode 94/144/145 | Easy | [LeetCode 1](https://leetcode.com/problems/binary-tree-inorder-traversal/), [LeetCode 2](https://leetcode.com/problems/binary-tree-preorder-traversal/), [LeetCode 3](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- [ ] [Level Order Traversal (BFS)](Level-Order-Traversal-BFS.md) | LeetCode 102 | Medium | [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [ ] [Maximum Depth of Binary Tree](Maximum-Depth-of-Binary-Tree.md) | LeetCode 104 | Easy | [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [ ] [Diameter of Binary Tree](Diameter-of-Binary-Tree.md) | LeetCode 543 | Easy | [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/)
- [ ] [Balanced Binary Tree](Balanced-Binary-Tree.md) | LeetCode 110 | Easy | [LeetCode](https://leetcode.com/problems/balanced-binary-tree/)
- [ ] [Same Tree](Same-Tree.md) | LeetCode 100 | Easy | [LeetCode](https://leetcode.com/problems/same-tree/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Binary Tree Traversals | Recursive DFS. O(n) time, O(h) stack. | Iterative stack traversal. O(n), O(h). | Morris traversal for inorder/preorder when O(1) space is required. |
| Level Order Traversal | Compute height, then print each level. O(n*h). | Queue BFS. O(n). | Queue BFS with fixed level size for clean level grouping. O(n). |
| Maximum Depth of Binary Tree | Level-order count levels. O(n). | Recursive height. O(n), O(h). | Iterative DFS/BFS avoids recursion-depth issues. O(n). |
| Diameter of Binary Tree | Compute height separately for every node. O(n^2). | One DFS returns height and updates diameter. O(n). | Same bottom-up DFS with global/holder max. |
| Balanced Binary Tree | Check height at every node repeatedly. O(n^2). | Bottom-up height computation. O(n). | Return -1 on imbalance for early exit. O(n). |
| Same Tree | Serialize both trees and compare. O(n) space. | Recursive node-by-node comparison. O(n). | Iterative stack/queue comparison avoids recursion overflow. |

---

## Tree Traversal Cheatsheet

| Traversal | Order | Key Use |
|-----------|-------|---------|
| Inorder | L→Root→R | BST sorted order |
| Preorder | Root→L→R | Copy tree, serialize |
| Postorder | L→R→Root | Delete tree, evaluate expression tree |
| Level order | BFS | Level-by-level, shortest path in tree |

---

## Binary Tree Problem-Solving Framework

```
Most tree problems = DFS that returns something useful

Template:
  solve(node):
    if node == null: return baseCase
    leftResult = solve(node.left)
    rightResult = solve(node.right)
    // combine leftResult, rightResult, node.val
    return something

What to return:
  - height / depth
  - (isValid, minVal, maxVal)
  - count / sum
  - -1 for invalid flag
```

#sde-sheet #binary-tree #day17
