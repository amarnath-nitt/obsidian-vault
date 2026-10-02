# Binary Tree Maximum Path Sum

**Difficulty:** Hard
**Category:** Trees
**LeetCode Link:** [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

---

## Problem Statement

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge. A node can appear at most once. The path sum is the sum of node values in the path. Return the maximum path sum of any non-empty path.

**Example:**
```
Input: root = [-10,9,20,null,null,15,7]
Output: 42  (path: 15 → 20 → 7)
```

---

## Intuition

At each node, a path can either:
1. Pass through the node connecting left and right subtrees (this is a "complete" path — can't extend upward)
2. Extend upward through the node (only one side can be chosen)

So at each node we compute the best "gain" we can contribute upward (node + max of left/right), but also check if the full path through this node (left + node + right) is the global maximum.

---

## Approach: Post-order DFS with Global Max

### Algorithm
1. For each node, recursively get max gain from left and right subtrees
2. Ignore negative gains (take 0 instead — don't include that subtree)
3. Update global max with `node.val + leftGain + rightGain` (path through this node)
4. Return `node.val + max(leftGain, rightGain)` to parent (can only extend one side)

### Java Code
```java
class Solution {
    private int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        maxGain(root);
        return maxSum;
    }

    private int maxGain(TreeNode node) {
        if (node == null) return 0;

        // Ignore negative contributions
        int leftGain = Math.max(maxGain(node.left), 0);
        int rightGain = Math.max(maxGain(node.right), 0);

        // Path through current node (cannot extend upward)
        int pathSum = node.val + leftGain + rightGain;
        maxSum = Math.max(maxSum, pathSum);

        // Return max gain if extending upward (only one side)
        return node.val + Math.max(leftGain, rightGain);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) — visit every node once
- **Space Complexity:** O(h) — recursion stack

---

## Step-by-Step Example

For `[-10, 9, 20, null, null, 15, 7]`:
```
maxGain(15): leftGain=0, rightGain=0, pathSum=15, return 15
maxGain(7):  leftGain=0, rightGain=0, pathSum=7,  return 7
maxGain(20): leftGain=15, rightGain=7, pathSum=42 ← global max, return 35
maxGain(9):  leftGain=0, rightGain=0, pathSum=9,  return 9
maxGain(-10): leftGain=9, rightGain=35, pathSum=34, return 25
```

---

## Key Takeaways

1. **Two roles per node:** Contribute to global max (both sides) vs. extend upward (one side)
2. **Ignore negatives:** `Math.max(gain, 0)` — don't include subtrees that hurt
3. **Global variable:** Track max across all nodes with a class-level variable

---

## Tags
#trees #dfs #recursion #hard #blind75
