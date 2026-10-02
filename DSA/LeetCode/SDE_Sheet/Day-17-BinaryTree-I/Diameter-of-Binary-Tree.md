# Diameter of Binary Tree

**LeetCode 543** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/diameter-of-binary-tree/)

### Problem
Find the longest path between any two nodes (doesn't need to pass through root).

### Approach

- Diameter through a node = `leftHeight + rightHeight`
- Update global max during DFS

### Java Solution

```java
class Solution {
    int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        height(root);
        return maxDiameter;
    }

    private int height(TreeNode node) {
        if (node == null) return 0;
        int left = height(node.left);
        int right = height(node.right);
        maxDiameter = Math.max(maxDiameter, left + right);
        return 1 + Math.max(left, right);
    }
}
```

**Complexity:** Time O(n) · Space O(h)

---
