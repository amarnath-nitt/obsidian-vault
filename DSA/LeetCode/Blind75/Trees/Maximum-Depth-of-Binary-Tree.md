# Maximum Depth of Binary Tree

**Difficulty:** Easy  
**Category:** Trees  
**LeetCode Link:** [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

---

## Problem Statement

Given the `root` of a binary tree, return its maximum depth.

---

## Approach: Recursive DFS

### Java Code
```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
```

### Complexity
- **Time:** O(n)
- **Space:** O(h)

---

## Tags
#trees #dfs #recursion #easy #blind75
