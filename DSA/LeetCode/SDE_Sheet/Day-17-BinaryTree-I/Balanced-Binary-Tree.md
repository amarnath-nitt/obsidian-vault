# Balanced Binary Tree

**LeetCode 110** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/balanced-binary-tree/)

### Problem
Is the binary tree height-balanced? (|leftHeight - rightHeight| ≤ 1 for every node)

### Approach

- Return -1 from height function to signal "unbalanced"
- If height difference > 1, propagate -1 upward

### Java Solution

```java
class Solution {
    public boolean isBalanced(TreeNode root) {
        return checkHeight(root) != -1;
    }

    private int checkHeight(TreeNode node) {
        if (node == null) return 0;
        int left = checkHeight(node.left);
        if (left == -1) return -1;
        int right = checkHeight(node.right);
        if (right == -1) return -1;
        if (Math.abs(left - right) > 1) return -1;
        return 1 + Math.max(left, right);
    }
}
```

**Complexity:** Time O(n) · Space O(h)

---
