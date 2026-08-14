# Subtree of Another Tree

**Difficulty:** Easy  
**Category:** Trees  
**LeetCode Link:** [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

---

## Problem Statement

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot`.

---

## Approach: Recursive Check

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

### Complexity
- **Time:** O(m × n)
- **Space:** O(h)

---

## Tags
#trees #dfs #recursion #easy #blind75
