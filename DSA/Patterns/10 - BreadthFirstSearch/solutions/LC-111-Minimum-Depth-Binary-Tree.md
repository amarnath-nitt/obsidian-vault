---
solved: true
difficulty: Easy
pattern: Breadth First Search
lc_number: 111
date_solved: 
tags:
  - dsa
  - breadth-first-search
  - easy
---
# Minimum Depth of Binary Tree (LC 111)

**Difficulty**: Easy  
**Pattern**: Breadth First Search (preferred) / DFS  
**LeetCode**: https://leetcode.com/problems/minimum-depth-of-binary-tree/

## Problem Statement
Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: 2
```

## Approach 1: BFS (Optimal)

### Intuition
BFS visits nodes level by level. The first time we encounter a leaf node, that is the minimum depth. This is more efficient than DFS because we don't need to traverse the whole tree (e.g. if root.left is a leaf but root.right is very deep).

### Java Code
```java
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int depth = 1;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                
                // First leaf node encountered is the answer
                if (node.left == null && node.right == null) {
                    return depth;
                }
                
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            
            depth++;
        }
        
        return depth;
    }
}
```

### Complexity
- **Time**: O(n) - Worst case visits all nodes, but usually stops early
- **Space**: O(w) - Max width

## Approach 2: DFS

### Intuition
Similar to Max Depth, but handle skew cases. If a node has only one child, we must traverse that child (depth is not 1).

### Java Code
```java
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        
        if (root.left == null) return minDepth(root.right) + 1;
        if (root.right == null) return minDepth(root.left) + 1;
        
        return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
    }
}
```

## Key Takeaways
- BFS is generally "faster" for finding shortest path/min depth in trees/graphs
- DFS must visit all nodes to be sure (unless optimized bounds used)
- Careful with nodes having only one child (path must end at leaf)
