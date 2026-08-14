# Path Sum (LC 112)

**Difficulty**: Easy  
**Pattern**: Depth First Search  
**LeetCode**: https://leetcode.com/problems/path-sum/

## Problem Statement
Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.

**Example:**
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: 5 -> 4 -> 11 -> 2 = 22
```

## Approach 1: Recursive DFS

### Intuition
Subtract current node's value from targetSum. If we reach a leaf node and remaining targetSum == 0, we found a path.

### Java Code
```java
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return false;
        }
        
        // Check if it's a leaf node
        if (root.left == null && root.right == null) {
            return targetSum - root.val == 0;
        }
        
        // Recurse
        return hasPathSum(root.left, targetSum - root.val) || 
               hasPathSum(root.right, targetSum - root.val);
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(h)

## Approach 2: Iterative DFS (Stack)

### Java Code
```java
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        
        Stack<TreeNode> nodeStack = new Stack<>();
        Stack<Integer> sumStack = new Stack<>();
        
        nodeStack.push(root);
        sumStack.push(targetSum - root.val);
        
        while (!nodeStack.isEmpty()) {
            TreeNode node = nodeStack.pop();
            int currSum = sumStack.pop();
            
            if (node.left == null && node.right == null && currSum == 0) {
                return true;
            }
            
            if (node.right != null) {
                nodeStack.push(node.right);
                sumStack.push(currSum - node.right.val);
            }
            if (node.left != null) {
                nodeStack.push(node.left);
                sumStack.push(currSum - node.left.val);
            }
        }
        
        return false;
    }
}
```

## Key Takeaways
- "Root-to-leaf" means checking validity only at leaf nodes
- Recursion simplifies passing state (remaining sum) down
- Short-circuit evaluation (`||`) stops search early if path found
