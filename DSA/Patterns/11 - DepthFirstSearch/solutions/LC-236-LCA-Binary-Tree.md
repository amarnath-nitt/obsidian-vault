---
solved: false
difficulty: Medium
pattern: Depth First Search
lc_number: 236
date_solved: 
tags:
  - dsa
  - depth-first-search
  - medium
---
# Lowest Common Ancestor of a Binary Tree (LC 236)

**Difficulty**: Medium  
**Pattern**: Depth First Search  
**LeetCode**: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

## Problem Statement
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

**Example:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
```

## Approach: Recursive DFS

### Intuition
Traverse the tree.
1. If current node is `p` or `q` or `null`, return current node.
2. Recurse left and right.
3. If both left and right return non-null, then current node is the LCA (because p and q are in different subtrees).
4. If only one returns non-null, pass that up (LCA is in that subtree).

### Java Code
```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) {
            return root;
        }
        
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        
        if (left != null && right != null) {
            return root;
        }
        
        return left != null ? left : right;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(h)

## Key Takeaways
- Classic recursion problem
- Works for Binary Tree (not just BST)
- Base case handles finding p or q directly
