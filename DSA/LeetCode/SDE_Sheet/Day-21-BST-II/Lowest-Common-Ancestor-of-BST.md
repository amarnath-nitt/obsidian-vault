# Lowest Common Ancestor of BST

**LeetCode 235** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

### Approach (Use BST property!)

- If both p and q < root → LCA is in left subtree
- If both p and q > root → LCA is in right subtree
- Otherwise → root is the LCA (they diverge here)

### Java Solution

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        while (root != null) {
            if (p.val < root.val && q.val < root.val) root = root.left;
            else if (p.val > root.val && q.val > root.val) root = root.right;
            else return root;
        }
        return null;
    }
}
```

**Complexity:** Time O(h) · Space O(1)

---
