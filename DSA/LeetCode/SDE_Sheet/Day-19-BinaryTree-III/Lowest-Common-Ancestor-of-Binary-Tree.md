# Lowest Common Ancestor of Binary Tree

**LeetCode 236** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

### Problem
Find LCA of two nodes p and q.

### Approach

- If root is null → return null
- If root == p or root == q → return root
- Recurse left and right
- If both sides return non-null → current node is LCA
- Else return the non-null side

### Java Solution

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root; // found in both subtrees
        return (left != null) ? left : right;
    }
}
```

**Complexity:** Time O(n) · Space O(h)

---
