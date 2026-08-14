# Same Tree

**Difficulty:** Easy  
**Category:** Trees  
**LeetCode Link:** [Same Tree](https://leetcode.com/problems/same-tree/)

---

## Problem Statement

Given the roots of two binary trees `p` and `q`, check if they are the same.

---

## Approach: Recursive DFS

### Java Code
```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;
        
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```

### Complexity
- **Time:** O(n)
- **Space:** O(h)

---

## Tags
#trees #dfs #recursion #easy #blind75
