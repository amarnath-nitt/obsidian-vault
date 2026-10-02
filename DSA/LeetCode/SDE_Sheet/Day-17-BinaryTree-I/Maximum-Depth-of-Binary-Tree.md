# Maximum Depth of Binary Tree

**LeetCode 104** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

### Java Solution

```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
```

**Complexity:** Time O(n) · Space O(h) where h = height

---
