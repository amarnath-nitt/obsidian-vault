# Validate Binary Search Tree

**LeetCode 98** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/validate-binary-search-tree/)

### Approach (Range Validation)

- Pass `(min, max)` valid range for each node
- Root: `(-∞, +∞)`, left child: `(min, node.val)`, right child: `(node.val, max)`

### Java Solution

```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean validate(TreeNode node, long min, long max) {
        if (node == null) return true;
        if (node.val <= min || node.val >= max) return false;
        return validate(node.left, min, node.val)
            && validate(node.right, node.val, max);
    }
}
```

**Complexity:** Time O(n) · Space O(h)

> **Alternative:** Inorder traversal and check if sorted (prev < current).

---
