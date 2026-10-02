---
solved: false
difficulty: Medium
pattern: Depth First Search
lc_number: 98
date_solved: 
tags:
  - dsa
  - depth-first-search
  - medium
---
# Validate Binary Search Tree

[Problem Link](https://leetcode.com/problems/validate-binary-search-tree/)

## Problem Statement
Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

## Approach
Recursion with range constraints `(min, max)`.
1.  Call helper `isValid(root, null, null)`.
2.  If node is null, true.
3.  If node value <= min or >= max, false.
4.  Recurse left with `(min, node.val)`.
5.  Recurse right with `(node.val, max)`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValid(root, null, null);
    }
    
    private boolean isValid(TreeNode node, Integer min, Integer max) {
        if (node == null) return true;
        
        if ((min != null && node.val <= min) || (max != null && node.val >= max)) {
            return false;
        }
        
        return isValid(node.left, min, node.val) && isValid(node.right, node.val, max);
    }
}
```
