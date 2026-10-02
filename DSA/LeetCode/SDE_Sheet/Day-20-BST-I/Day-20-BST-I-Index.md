# Day 20 — Binary Search Tree I

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** BST — Search, Insert, Delete, Validate
**Difficulty Mix:** Easy / Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Validate Binary Search Tree](Validate-Binary-Search-Tree.md) | LeetCode 98 | Medium | [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)
- [ ] [Search in BST](Search-in-BST.md) | LeetCode 700 | Easy | [LeetCode](https://leetcode.com/problems/search-in-a-binary-search-tree/)
- [ ] [Insert into BST](Insert-into-BST.md) | LeetCode 701 | Medium | [LeetCode](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
- [ ] [Delete Node in BST](Delete-Node-in-BST.md) | LeetCode 450 | Medium | [LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/)
- [ ] [Kth Smallest Element in BST](Kth-Smallest-Element-in-BST.md) | LeetCode 230 | Medium | [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [ ] [Floor and Ceil in BST](Floor-and-Ceil-in-BST.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Floor+and+Ceil+in+BST)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Validate Binary Search Tree | Inorder list, then check sorted order. O(n) space. | Recursive range validation. O(n), O(h). | Iterative inorder with previous value, or Morris for O(1) extra. |
| Search in BST | Treat as a binary tree and DFS all nodes. O(n). | Recursive BST search. O(h). | Iterative BST search. O(h), O(1). |
| Insert into BST | Rebuild tree with the new value. O(n). | Recursive insert using BST property. O(h). | Iterative insert with parent pointer. O(h), O(1). |
| Delete Node in BST | Inorder all values, remove, rebuild. O(n). | Recursive delete using successor/predecessor. O(h). | Same idea with careful pointer updates; O(h) average. |
| Kth Smallest Element in BST | Full inorder list then index k-1. O(n) space. | Iterative inorder and stop after k nodes. O(h+k). | Morris inorder for O(1) extra space. |
| Floor and Ceil in BST | Inorder list then binary search. O(n) space. | Traverse using BST property for floor and ceil separately. O(h). | One pass can update floor/ceil candidates together. O(h). |

---

## BST Properties

```
For every node N:
  - All values in N.left subtree < N.val
  - All values in N.right subtree > N.val
  - No duplicates (typically)

Inorder traversal of BST → sorted ascending order [x]
```

---

## BST Operations Summary

| Operation | Complexity (balanced) | Key Idea |
|-----------|----------------------|----------|
| Search | O(log n) | Compare and go left/right |
| Insert | O(log n) | Find insertion point at leaf |
| Delete | O(log n) | Handle 3 cases; use inorder successor |
| kth smallest | O(log n + k) | Inorder traversal |
| Floor/Ceil | O(log n) | Track best candidate while searching |
| LCA | O(log n) | If both < root → go left; both > root → go right |

#sde-sheet #bst #day20
