# Two Sum in BST

**LeetCode 653** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

### Problem
Find if there exist two nodes in BST that sum to target.

### Approach 1 — HashSet + DFS

```java
class Solution {
    Set<Integer> set = new HashSet<>();

    public boolean findTarget(TreeNode root, int k) {
        if (root == null) return false;
        if (set.contains(k - root.val)) return true;
        set.add(root.val);
        return findTarget(root.left, k) || findTarget(root.right, k);
    }
}
```

### Approach 2 — Inorder + Two Pointers

- Inorder traversal → sorted array → two pointer

**Complexity:** Time O(n) · Space O(n)

---
