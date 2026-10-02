# Day 21 — Binary Search Tree II

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** BST — LCA, Two Sum, Merge, Convert
**Difficulty Mix:** Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Lowest Common Ancestor of BST](Lowest-Common-Ancestor-of-BST.md) | LeetCode 235 | Medium | [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [ ] [Two Sum in BST](Two-Sum-in-BST.md) | LeetCode 653 | Easy | [LeetCode](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
- [ ] [Recover BST (Two Nodes Swapped)](Recover-BST-Two-Nodes-Swapped.md) | LeetCode 99 | Hard | [LeetCode](https://leetcode.com/problems/recover-binary-search-tree/)
- [ ] [Largest BST Subtree](Largest-BST-Subtree.md) | LeetCode 333 | Medium | [LeetCode](https://leetcode.com/problems/largest-bst-subtree/)
- [ ] [Merge Two BSTs](Merge-Two-BSTs.md) | LeetCode — | Hard | [LeetCode search](https://leetcode.com/problemset/?search=Merge+Two+BSTs)
- [ ] [Convert Sorted Array to BST](Convert-Sorted-Array-to-BST.md) | LeetCode 108 | Easy | [LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Lowest Common Ancestor of BST | Use generic binary-tree LCA. O(n). | Store root-to-node paths and compare. O(h) space. | Use BST property to move left/right iteratively. O(h), O(1). |
| Two Sum in BST | Compare every pair of nodes. O(n^2). | DFS with HashSet of complements. O(n) space. | Two BST iterators like two pointers on inorder. O(n), O(h). |
| Recover BST | Inorder list, sort/copy values, find swapped nodes. O(n) space. | Inorder traversal detects two violations. O(h) stack. | Morris inorder detects violations in O(1) extra space. |
| Largest BST Subtree | Validate every subtree separately. O(n^2). | Bottom-up return min, max, size, and validity. O(n). | Same postorder DP with early invalid propagation. |
| Merge Two BSTs | Inorder both trees, concatenate, sort. O((m+n) log(m+n)). | Merge two sorted inorder arrays. O(m+n) space. | Two stack-based inorder iterators merge on the fly. O(h1+h2) extra. |
| Convert Sorted Array to BST | Insert values one by one; can become skewed. O(n^2). | Recursively choose middle as root. O(n). | Same range-based recursion without slicing arrays. O(n), O(log n) stack. |

---

## BST vs Binary Tree Problem Strategy

| If problem says... | Use |
|---|---|
| "BST" | BST property: left < root < right |
| "LCA" in BST | Compare values with root (O(log n)) |
| "Inorder" | Automatically sorted in BST |
| "Two nodes swapped" | Find inversions in inorder |
| "Convert to balanced BST" | Inorder → middle as root |

#sde-sheet #bst #day21
