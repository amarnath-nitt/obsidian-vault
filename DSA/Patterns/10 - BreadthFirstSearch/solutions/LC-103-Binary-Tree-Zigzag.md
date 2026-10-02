---
solved: false
difficulty: Medium
pattern: Breadth First Search
lc_number: 103
date_solved: 
tags:
  - dsa
  - breadth-first-search
  - medium
---
# Binary Tree Zigzag Level Order Traversal (LC 103)

**Difficulty**: Medium  
**Pattern**: Breadth First Search (BFS)  
**LeetCode**: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

## Problem Statement
Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

**Example:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

## Approach: BFS with Deque

### Intuition
Standard BFS with a queue. For the result list of each level, if `level % 2 == 0`, add normally. If `level % 2 == 1`, add to front (or reverse list).
Using `LinkedList` allows `addFirst` / `addLast`.

### Java Code
```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        boolean leftToRight = true;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            LinkedList<Integer> level = new LinkedList<>();
            
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                
                if (leftToRight) {
                    level.addLast(node.val);
                } else {
                    level.addFirst(node.val);
                }
                
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            
            result.add(level);
            leftToRight = !leftToRight;
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(w) max width

## Key Takeaways
- Simple modification of BFS level order
- `LinkedList` is better than `ArrayList` + `Collections.reverse` for O(1) front insertion
