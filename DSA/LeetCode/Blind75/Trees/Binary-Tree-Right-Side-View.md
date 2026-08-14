# Binary Tree Right Side View

**Difficulty:** Medium  
**Category:** Trees  
**LeetCode Link:** [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

---

## Problem Statement

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return the values of the nodes you can see ordered from top to bottom.

**Example 1:**
```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

**Example 2:**
```
Input: root = [1,null,3]
Output: [1,3]
```

**Constraints:**
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

---

## Intuition

From the right side, we see the rightmost node at each level. This is a level-order traversal problem where we need the last node of each level.

---

## Approach 1: BFS Level Order (Naive Solution)

### Algorithm
1. Use BFS to traverse level by level
2. For each level, track all nodes
3. Add the last node of each level to result

### Java Code
```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                
                // Add last node of this level
                if (i == levelSize - 1) {
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

### Complexity Analysis
- **Time Complexity:** O(n) - Visit all nodes
- **Space Complexity:** O(w) - Queue size, w = max width

---

## Approach 2: DFS (Optimized Solution)

### Algorithm
1. Use DFS, prioritizing right subtree first
2. Track current depth
3. Add node if it's the first time we see this depth

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
        
        // First time seeing this depth - add to result
        if (depth == result.size()) {
            result.add(node.val);
        }
        
        // Visit right first, then left
        dfs(node.right, depth + 1, result);
        dfs(node.left, depth + 1, result);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Visit all nodes
- **Space Complexity:** O(h) - Recursion stack, h = height

### Why This is Better
- ✅ More space efficient for balanced trees
- ✅ Elegant recursive solution
- ✅ Processes right side first naturally

---

## Key Takeaways

1. **Pattern:** Level-order traversal or DFS with depth tracking
2. **BFS:** Natural for level-based problems
3. **DFS optimization:** Visit right subtree first
4. **Depth tracking:** Key to knowing when we see a new level

---

## Tags
#trees #bfs #dfs #medium #blind75
