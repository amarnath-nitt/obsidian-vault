# Binary Tree Maximum Path Sum

**Difficulty:** Hard  
**Category:** Trees  
**LeetCode Link:** [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

---

## Problem Statement

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge. A node can only appear in the sequence **at most once**.

The **path sum** is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum path sum of any **non-empty** path.

---

## Approach: Post-order DFS

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
        
        // Max sum from left and right (ignore negative)
        int leftGain = Math.max(maxGain(node.left), 0);
        int rightGain = Math.max(maxGain(node.right), 0);
        
        // Path through current node
        int pathSum = node.val + leftGain + rightGain;
        maxSum = Math.max(maxSum, pathSum);
        
        // Return max gain if continuing path
        return node.val + Math.max(leftGain, rightGain);
    }
}
```

### Complexity
- **Time:** O(n)
- **Space:** O(h)

---

## Tags
#trees #dfs #recursion #hard #blind75
