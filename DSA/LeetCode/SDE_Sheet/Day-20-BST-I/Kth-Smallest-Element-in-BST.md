# Kth Smallest Element in BST

**LeetCode 230** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

### Approach

- Inorder traversal gives sorted order
- Stop at the kth element

### Java Solution (Iterative Inorder)

```java
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode curr = root;
        int count = 0;

        while (curr != null || !stack.isEmpty()) {
            while (curr != null) { stack.push(curr); curr = curr.left; }
            curr = stack.pop();
            if (++count == k) return curr.val;
            curr = curr.right;
        }
        return -1;
    }
}
```

**Complexity:** Time O(h+k) · Space O(h)

---
