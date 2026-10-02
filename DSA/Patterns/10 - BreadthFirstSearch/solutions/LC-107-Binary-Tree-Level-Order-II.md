---
solved: true
difficulty: Medium
pattern: Breadth First Search
lc_number: 107
date_solved: 
tags:
  - dsa
  - breadth-first-search
  - medium
---
# Binary Tree Level Order Traversal II (LC 107)

**Difficulty**: Medium  
**Pattern**: Breadth-First Search  
**LeetCode**: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

## Problem Statement
Given the `root` of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

**Example:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
```

## Approach: BFS + Reverse

### Intuition
Same as Standard Level Order, but append each level to the *front* of the result list (or reverse the result list at the end).
LinkedList allows O(1) insertion at head.

### Java Code
```java
class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        LinkedList<List<Integer>> result = new LinkedList<>(); // Use LinkedList for addFirst
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
            result.addFirst(level); // Add to front
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(N)

## Key Takeaways
- `LinkedList.addFirst()` for O(1) prepend
- Alternatively `Collections.reverse(ArrayList)`
