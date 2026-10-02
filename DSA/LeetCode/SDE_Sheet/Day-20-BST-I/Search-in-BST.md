# Search in BST

**LeetCode 700** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/search-in-a-binary-search-tree/)

### Java Solution

```java
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null || root.val == val) return root;
        return val < root.val ? searchBST(root.left, val) : searchBST(root.right, val);
    }
}
```

**Complexity:** Time O(h) · Space O(h) → O(log n) balanced

---
