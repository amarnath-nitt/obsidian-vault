# Binary Tree Maximum Path Sum

**LeetCode 124** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

### Problem
Find the max sum path between any two nodes.

### Approach

- For each node: max contribution going up = `node.val + max(leftGain, rightGain, 0)`
- Path through node = `node.val + leftGain + rightGain` (can go both sides)
- Update global max with path through current node

### Java Solution

```java
class Solution {
    int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        gainFrom(root);
        return maxSum;
    }

    private int gainFrom(TreeNode node) {
        if (node == null) return 0;
        int leftGain = Math.max(gainFrom(node.left), 0);
        int rightGain = Math.max(gainFrom(node.right), 0);
        maxSum = Math.max(maxSum, node.val + leftGain + rightGain);
        return node.val + Math.max(leftGain, rightGain); // can only go one way up
    }
}
```

**Complexity:** Time O(n) · Space O(h)

---
