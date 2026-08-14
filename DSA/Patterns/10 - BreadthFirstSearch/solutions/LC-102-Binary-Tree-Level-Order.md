# Binary Tree Level Order Traversal (LC 102)

**Difficulty**: Medium  
**Pattern**: Breadth-First Search  
**LeetCode**: https://leetcode.com/problems/binary-tree-level-order-traversal/

## Problem Statement
Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

**Example:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

## Approach: BFS with Queue

### Intuition
Standard BFS. Use a queue.
Process nodes level by level by capturing queue size at start of each level iteration.

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
            List<Integer> level = new ArrayList<>();
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode curr = queue.poll();
                level.add(curr.val);
                
                if (curr.left != null) queue.offer(curr.left);
                if (curr.right != null) queue.offer(curr.right);
            }
            result.add(level);
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(N) (width of tree)

## Key Takeaways
- Queue allows FIFO processing
- `levelSize` capture is the standard trick to distinguish levels
