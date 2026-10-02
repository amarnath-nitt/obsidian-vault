---
solved: false
difficulty: Medium
pattern: Binary Tree Traversal
lc_number: 102
date_solved: 
tags:
  - dsa
  - binary-tree-traversal
  - medium
---
# Binary Tree Level Order Traversal (LC 102)

**Difficulty**: Medium  
**Pattern**: Breadth-First Search / Binary Tree Traversal  
**LeetCode**: https://leetcode.com/problems/binary-tree-level-order-traversal/

## Problem Statement
Given the `root` of a binary tree, return the level order traversal of its nodes (i.e., from left to right, level by level).

**Example:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

## Approach 1: BFS with Queue

### Java Code
```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>();
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                currentLevel.add(node.val);
                
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            
            result.add(currentLevel);
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(n)

## Approach 2: DFS with Level Tracking

### Java Code
```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(root, 0, result);
        return result;
    }
    
    private void dfs(TreeNode node, int level, List<List<Integer>> result) {
        if (node == null) return;
        
        if (level == result.size()) {
            result.add(new ArrayList<>());
        }
        
        result.get(level).add(node.val);
        dfs(node.left, level + 1, result);
        dfs(node.right, level + 1, result);
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(h) - Recursion depth

## Key Takeaways
- BFS naturally processes level by level
- Track level size to separate levels
- DFS can also work with level parameter
- Foundation for many tree traversal problems
