---
solved: false
difficulty: Medium
pattern: Breadth First Search
lc_number: 199
date_solved: 
tags:
  - dsa
  - breadth-first-search
  - medium
---
# Binary Tree Right Side View (LC 199)

**Difficulty**: Medium  
**Pattern**: Breadth First Search (BFS) / DFS  
**LeetCode**: https://leetcode.com/problems/binary-tree-right-side-view/

## Problem Statement
Given the `root` of a binary tree, imagine standing on the **right side** of it, return the values of the nodes you can see ordered from top to bottom.

**Example:**
```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

## Approach 1: BFS

### Intuition
Level order traversal. The last element of each level is visible from the right.

### Java Code
```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                // If it's the last node in the current level, add to result
                if (i == size - 1) {
                    result.add(node.val);
                }
                
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
        
        return result;
    }
}
```

## Approach 2: DFS (Reverse Preorder)

### Intuition
Visit Root -> Right -> Left.
If we visit Right before Left, we see the rightmost element of a level first.
Keep track of depth. If `depth == result.size()`, it means this is the first time we visit this depth, so it must be the rightmost node visible so far.

### Java Code
```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        dfs(root, 0, result);
        return result;
    }
    
    private void dfs(TreeNode node, int depth, List<Integer> result) {
        if (node == null) return;
        
        if (depth == result.size()) {
            result.add(node.val);
        }
        
        dfs(node.right, depth + 1, result); // Visit Right first
        dfs(node.left, depth + 1, result);
    }
}
```

## Key Takeaways
- BFS is intuitive for level-based logic
- DFS (Right-first) is a clever optimization to avoid queue overhead
