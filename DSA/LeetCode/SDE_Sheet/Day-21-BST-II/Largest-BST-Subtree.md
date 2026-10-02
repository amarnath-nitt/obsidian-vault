# Largest BST Subtree

**LeetCode 333** · Medium
**Problem:** Find the largest subtree that is a valid BST.

### Approach (Bottom-up DP)

Return `(size, min, max)` from each node:
- Check if left and right subtrees are valid BSTs
- If current node can be root of a BST: `left.max < node.val < right.min`
- Return total size; propagate as `-1` for invalid

```java
class Solution {
    int maxSize = 0;

    public int largestBSTSubtree(TreeNode root) {
        solve(root);
        return maxSize;
    }

    // Returns [size, min, max] — size=-1 if not BST
    private int[] solve(TreeNode node) {
        if (node == null) return new int[]{0, Integer.MAX_VALUE, Integer.MIN_VALUE};

        int[] left = solve(node.left);
        int[] right = solve(node.right);

        if (left[0] == -1 || right[0] == -1
                || node.val <= left[2] || node.val >= right[1]) {
            return new int[]{-1, 0, 0};
        }

        int size = left[0] + right[0] + 1;
        maxSize = Math.max(maxSize, size);
        return new int[]{size, Math.min(left[1], node.val), Math.max(right[2], node.val)};
    }
}
```

---
