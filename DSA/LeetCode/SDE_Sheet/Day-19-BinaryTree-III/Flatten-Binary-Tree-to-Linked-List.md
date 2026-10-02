# Flatten Binary Tree to Linked List

**LeetCode 114** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

### Problem
Flatten in-place to a linked list in preorder order.

### Approach (Morris-like — Reverse Preorder)

- Process nodes in **reverse preorder** (right → left → root)
- Maintain a `prev` pointer
- Set `node.right = prev`, `node.left = null`

```java
class Solution {
    TreeNode prev = null;

    public void flatten(TreeNode root) {
        if (root == null) return;
        flatten(root.right);
        flatten(root.left);
        root.right = prev;
        root.left = null;
        prev = root;
    }
}
```

**Alternative (Iterative):** At each node, insert left subtree between node and node.right.

**Complexity:** Time O(n) · Space O(h)

---
