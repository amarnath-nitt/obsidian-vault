# Subtree of Another Tree

**Difficulty:** Easy
**Category:** Trees
**LeetCode Link:** [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

---

## Problem Statement

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values as `subRoot`.

**Example:**
```
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

---

## Intuition

At every node in `root`, check if the subtree rooted there is identical to `subRoot`. This reuses the "Same Tree" logic. We traverse every node of `root` and run a full tree comparison at each.

---

## Approach: Recursive DFS + isSameTree

### Algorithm
1. If `root` is null → false (subRoot not found)
2. If `isSameTree(root, subRoot)` → true
3. Otherwise, recursively check left and right subtrees of root

### Java Code
```java
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;
        if (isSameTree(root, subRoot)) return true;

        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;

        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(m × n) — for each of m nodes in root, compare up to n nodes of subRoot
- **Space Complexity:** O(h) — recursion stack, h = height of root

---

## Key Takeaways

1. **Pattern:** Compose two recursive functions — traversal + comparison
2. **Reuse:** isSameTree is a standalone helper
3. **Short-circuit:** `||` stops as soon as subtree is found

---

## Tags
#trees #dfs #recursion #easy #blind75
