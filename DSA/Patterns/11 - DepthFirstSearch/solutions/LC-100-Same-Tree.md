---
solved: true
difficulty: Easy
pattern: Depth First Search
lc_number: 100
date_solved: 
tags:
  - dsa
  - depth-first-search
  - easy
---
# Same Tree

[Problem Link](https://leetcode.com/problems/same-tree/)

## Problem Statement
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Approach
Recursion (DFS).
1.  If both nodes are null, return true.
2.  If one is null and other is not, return false.
3.  If values are different, return false.
4.  Recursively check left and right subtrees.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
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
