# Insert into BST

**LeetCode 701** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

### Java Solution

```java
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);
        if (val < root.val) root.left = insertIntoBST(root.left, val);
        else root.right = insertIntoBST(root.right, val);
        return root;
    }
}
```

**Complexity:** Time O(h) · Space O(h)

---
