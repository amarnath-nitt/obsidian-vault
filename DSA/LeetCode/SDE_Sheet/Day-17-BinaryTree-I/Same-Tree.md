# Same Tree

**LeetCode 100** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/same-tree/)

### Java Solution

```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        return p.val == q.val
            && isSameTree(p.left, q.left)
            && isSameTree(p.right, q.right);
    }
}
```

---
