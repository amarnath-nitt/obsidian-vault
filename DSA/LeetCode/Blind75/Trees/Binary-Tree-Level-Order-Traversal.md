# Binary Tree Level Order Traversal

**Difficulty:** Medium  
**Category:** Trees  
**LeetCode Link:** [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

---

## Problem Statement

Given the `root` of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

---

## Approach: BFS with Queue

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
                TreeNode node = queue.poll();
                level.add(node.val);
                
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            
            result.add(level);
        }
        
        return result;
    }
}
```

### Complexity
- **Time:** O(n)
- **Space:** O(w) where w = max width

---

## Tags
#trees #bfs #medium #blind75

---

## Visualization

- Embed: `![](../assets/binary-tree-level-order/step-1.svg)`
- Obsidian embed: `![[../assets/binary-tree-level-order/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="180">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <text x="20" y="28" fill="#222">Level-order BFS traversal (levels shown):</text>
    <g transform="translate(20,40)">
        <circle cx="80" cy="20" r="18" fill="#fff" stroke="#4b6cc1"/>
        <text x="80" y="24" text-anchor="middle">1</text>
        <circle cx="40" cy="70" r="18" fill="#fff" stroke="#4b6cc1"/>
        <text x="40" y="74" text-anchor="middle">2</text>
        <circle cx="120" cy="70" r="18" fill="#fff" stroke="#4b6cc1"/>
        <text x="120" y="74" text-anchor="middle">3</text>
    </g>
</svg>
