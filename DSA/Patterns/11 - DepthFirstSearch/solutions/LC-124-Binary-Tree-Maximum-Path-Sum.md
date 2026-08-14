# Binary Tree Maximum Path Sum (LC 124)

**Difficulty**: Hard  
**Pattern**: Depth First Search  
**LeetCode**: https://leetcode.com/problems/binary-tree-maximum-path-sum/

## Problem Statement
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum is the sum of the node's values in the path.
Given the `root` of a binary tree, return the maximum path sum of any non-empty path.

**Example:**
```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

## Approach: Recursive DFS

### Intuition
For any node, the maximum path passing through it (as the highest node in the path) is:
`Node.val + max(0, LeftGain) + max(0, RightGain)`
However, for the return value to its parent, it can only extend strictly downwards (either left or right), so it returns:
`Node.val + max(0, max(LeftGain, RightGain))`
We update a global maximum at each node.

### Java Code
```java
class Solution {
    int maxPathSum = Integer.MIN_VALUE;
    
    public int maxPathSum(TreeNode root) {
        postOrder(root);
        return maxPathSum;
    }
    
    private int postOrder(TreeNode node) {
        if (node == null) return 0;
        
        // Computed gain from subtrees (ignore negative sums)
        int leftGain = Math.max(postOrder(node.left), 0);
        int rightGain = Math.max(postOrder(node.right), 0);
        
        // Path through current node (potential global max)
        int currentPathSum = node.val + leftGain + rightGain;
        maxPathSum = Math.max(maxPathSum, currentPathSum);
        
        // Return max gain for parent
        return node.val + Math.max(leftGain, rightGain);
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(h)

## Key Takeaways
- Global variable (or array ref) tracks the max path sum
- Return value differs from what we update in global variable (Path vs Branch)
- `max(..., 0)` is critical to ignore negative path contributions
