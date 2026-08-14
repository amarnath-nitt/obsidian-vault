# Invert Binary Tree

**Difficulty:** Easy  
**Category:** Trees  
**LeetCode Link:** [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

---

## Problem Statement

Given the `root` of a binary tree, invert the tree, and return its root.

**Example:**
```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

---

## Approach: Recursive DFS

### Java Code
```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        
        // Swap children
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        
        // Recursively invert subtrees
        invertTree(root.left);
        invertTree(root.right);
        
        return root;
    }
}
```

### Complexity
- **Time:** O(n)
- **Space:** O(h) recursion

---

## Tags
#trees #dfs #recursion #easy #blind75
