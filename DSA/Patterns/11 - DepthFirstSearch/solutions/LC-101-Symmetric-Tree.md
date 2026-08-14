# Symmetric Tree

[Problem Link](https://leetcode.com/problems/symmetric-tree/)

## Problem Statement
Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Approach
Recursion (DFS).
Create a helper function `isMirror(node1, node2)`.
1.  If both null, true.
2.  If one null, false.
3.  If values different, false.
4.  Return `isMirror(node1.left, node2.right) && isMirror(node1.right, node2.left)`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return isMirror(root.left, root.right);
    }
    
    private boolean isMirror(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return true;
        if (t1 == null || t2 == null) return false;
        if (t1.val != t2.val) return false;
        
        return isMirror(t1.left, t2.right) && isMirror(t1.right, t2.left);
    }
}
```
