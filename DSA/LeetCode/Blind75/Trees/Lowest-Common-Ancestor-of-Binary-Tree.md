# Lowest Common Ancestor of Binary Tree

**Difficulty:** Medium  
**Category:** Trees  
**LeetCode Link:** [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

---

## Problem Statement

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

The lowest common ancestor is defined as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).

**Example:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

**Constraints:**
- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the tree.

---

## Intuition

The LCA is the deepest node that has both p and q in its subtrees (or is one of them). Use recursion to search both subtrees.

---

## Approach: Recursive DFS

### Algorithm
1. If current node is null or matches p or q, return it
2. Recursively search left and right subtrees
3. If both subtrees return non-null, current node is LCA
4. Otherwise, return the non-null subtree result

### Java Code
```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // Base case: null or found one of the nodes
        if (root == null || root == p || root == q) {
            return root;
        }
        
        // Search in left and right subtrees
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        
        // If both subtrees return non-null, root is LCA
        if (left != null && right != null) {
            return root;
        }
        
        // Otherwise, return the non-null side
        return left != null ? left : right;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - May visit all nodes
- **Space Complexity:** O(h) - Recursion stack, h = height

---

## Key Takeaways

1. **Pattern:** Post-order DFS (process children first)
2. **Three cases:** Both in left, both in right, or split
3. **Early return:** If node matches p or q
4. **Elegant recursion:** Solution naturally bubbles up

---

## Tags
#trees #dfs #recursion #lca #medium #blind75
