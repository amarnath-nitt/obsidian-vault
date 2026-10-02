# Recover BST (Two Nodes Swapped)

**LeetCode 99** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/recover-binary-search-tree/)

### Problem
Two nodes of BST are swapped. Fix the BST without changing structure.

### Approach (Inorder traversal — find violation)

- Inorder of BST should be sorted
- **First violation**: `prev > curr` → first swapped node = `prev`
- **Second violation**: `prev > curr` again → second swapped node = `curr`
- Swap their values

### Java Solution

```java
class Solution {
    TreeNode first = null, second = null, prev = null;

    public void recoverTree(TreeNode root) {
        inorder(root);
        int tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }

    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        if (prev != null && prev.val > node.val) {
            if (first == null) first = prev;
            second = node;
        }
        prev = node;
        inorder(node.right);
    }
}
```

**Complexity:** Time O(n) · Space O(h)

---
