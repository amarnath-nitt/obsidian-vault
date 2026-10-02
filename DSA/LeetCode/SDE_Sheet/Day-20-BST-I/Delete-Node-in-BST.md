# Delete Node in BST

**LeetCode 450** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/delete-node-in-a-bst/)

### Three Cases

1. **Node is a leaf** → return null
2. **Node has one child** → return the child
3. **Node has two children** → replace with **inorder successor** (smallest in right subtree), then delete successor

### Java Solution

```java
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else {
            // Found the node to delete
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            // Two children: find inorder successor (min of right subtree)
            TreeNode successor = findMin(root.right);
            root.val = successor.val;
            root.right = deleteNode(root.right, successor.val);
        }
        return root;
    }

    private TreeNode findMin(TreeNode node) {
        while (node.left != null) node = node.left;
        return node;
    }
}
```

**Complexity:** Time O(h) · Space O(h)

---
