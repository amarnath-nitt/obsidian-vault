# Validate Binary Search Tree

**Difficulty:** Medium  
**Category:** Trees  
**LeetCode Link:** [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

---

## Problem Statement

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

---

## Approach: Recursive with Range

### Java Code
```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return validate(root, null, null);
    }
    
    private boolean validate(TreeNode node, Integer min, Integer max) {
        if (node == null) return true;
        
        if ((min != null && node.val <= min) || (max != null && node.val >= max)) {
            return false;
        }
        
        return validate(node.left, min, node.val) && 
               validate(node.right, node.val, max);
    }
}
```

### Complexity
- **Time:** O(n)
- **Space:** O(h)

---

## Tags
#trees #dfs #bst #medium #blind75
