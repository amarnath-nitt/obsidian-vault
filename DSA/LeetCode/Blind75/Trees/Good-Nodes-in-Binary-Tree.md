# Good Nodes in Binary Tree

**Difficulty:** Medium  
**Category:** Trees  
**LeetCode Link:** [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

---

## Problem Statement

Given a binary tree `root`, a node X in the tree is named **good** if in the path from root to X there are no nodes with a value greater than X.

Return the number of **good** nodes in the binary tree.

**Example:**
```
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```

**Constraints:**
- The number of nodes in the binary tree is in the range `[1, 10^5]`.
- Each node's value is between `[-10^4, 10^4]`.

---

## Intuition

A node is "good" if its value is >= all values on the path from root to that node. Track the maximum value seen so far on the path.

---

## Approach: DFS with Max Tracking

### Algorithm
1. Use DFS to traverse the tree
2. Track the maximum value seen on current path
3. If current node >= max, it's a good node
4. Update max for children

### Java Code
```java
class Solution {
    public int goodNodes(TreeNode root) {
        return dfs(root, root.val);
    }
    
    private int dfs(TreeNode node, int maxSoFar) {
        if (node == null) return 0;
        
        int count = 0;
        
        // Check if current node is good
        if (node.val >= maxSoFar) {
            count = 1;
            maxSoFar = node.val;  // Update max for children
        }
        
        // Count good nodes in subtrees
        count += dfs(node.left, maxSoFar);
        count += dfs(node.right, maxSoFar);
        
        return count;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Visit each node once
- **Space Complexity:** O(h) - Recursion stack, h = height

---

## Key Takeaways

1. **Pattern:** DFS with path state tracking
2. **Max tracking:** Pass maximum value down the tree
3. **Path-dependent:** Each path has its own maximum
4. **Root is always good:** No nodes before it

---

## Tags
#trees #dfs #recursion #medium #blind75
