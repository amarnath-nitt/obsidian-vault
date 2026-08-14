# Binary Tree Inorder Traversal (LC 94)

**Difficulty**: Easy  
**Pattern**: Binary Tree Traversal  
**LeetCode**: https://leetcode.com/problems/binary-tree-inorder-traversal/

## Problem Statement
Given the `root` of a binary tree, return the inorder traversal of its nodes' values.
Inorder: Left -> Root -> Right.

**Example:**
```
Input: root = [1,null,2,3]
Output: [1,3,2]
```

## Approach 1: Recursive

### Java Code
```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        dfs(root, result);
        return result;
    }
    
    private void dfs(TreeNode node, List<Integer> result) {
        if (node == null) return;
        
        dfs(node.left, result);  // Left
        result.add(node.val);    // Root
        dfs(node.right, result); // Right
    }
}
```

## Approach 2: Iterative (Stack)

### Intuition
Simulate recursion stack. Go as left as possible, pushing nodes. When null reached, pop, process (add to result), then go right.

### Java Code
```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        
        while (curr != null || !stack.isEmpty()) {
            // Reach the left most Node of the curr Node
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            // Current must be NULL at this point
            curr = stack.pop();
            result.add(curr.val); // Add the node
            curr = curr.right;    // Visit the right subtree
        }
        
        return result;
    }
}
```

## Key Takeaways
- Inorder property: for BST, yields sorted values
- Iterative approach goes "Left, Pop, Right"
- Essential foundation for BST problems
