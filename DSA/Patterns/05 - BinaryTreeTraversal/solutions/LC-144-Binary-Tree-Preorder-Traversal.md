---
solved: false
difficulty: Easy
pattern: Binary Tree Traversal
lc_number: 144
date_solved: 
tags:
  - dsa
  - binary-tree-traversal
  - easy
---
# Binary Tree Preorder Traversal (LC 144)

**Difficulty**: Easy  
**Pattern**: Binary Tree Traversal  
**LeetCode**: https://leetcode.com/problems/binary-tree-preorder-traversal/

## Problem Statement
Given the `root` of a binary tree, return the preorder traversal of its nodes' values.
Preorder: Root -> Left -> Right.

**Example:**
```
Input: root = [1,null,2,3]
Output: [1,2,3]
```

## Approach 1: Recursive

### Java Code
```java
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        dfs(root, result);
        return result;
    }
    
    private void dfs(TreeNode node, List<Integer> result) {
        if (node == null) return;
        
        result.add(node.val);    // Root
        dfs(node.left, result);  // Left
        dfs(node.right, result); // Right
    }
}
```

## Approach 2: Iterative (Stack)

### Intuition
Push root. While stack not empty: pop node, process it, then push RIGHT child, then LEFT child (so left is popped first).

### Java Code
```java
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            result.add(node.val);
            
            // Push right first so left is processed first (LIFO)
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
        }
        
        return result;
    }
}
```

## Key Takeaways
- Preorder useful for cloning graphs/trees
- Stack order is opposite of visit order (Push Right, Push Left -> Pop Left, Pop Right)
- Simpler iterative logic than Inorder/Postorder
