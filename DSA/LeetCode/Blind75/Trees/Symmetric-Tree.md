# Symmetric Tree

**Difficulty:** Easy  
**Category:** Trees  
**LeetCode Link:** [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

---

## Problem Statement

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

**Example 1:**
```
Input: root = [1,2,2,3,4,4,3]
Output: true
```

**Example 2:**
```
Input: root = [1,2,2,null,3,null,3]
Output: false
```

**Constraints:**
- The number of nodes in the tree is in the range `[1, 1000]`.
- `-100 <= Node.val <= 100`

---

## Intuition

A tree is symmetric if the left subtree is a mirror reflection of the right subtree. We need to compare nodes at corresponding positions.

---

## Approach 1: Recursive (Naive Solution)

### Algorithm
1. Create a helper function that compares two nodes
2. Check if left.left mirrors right.right
3. Check if left.right mirrors right.left
4. Values must match and structure must be symmetric

### Java Code
```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return isMirror(root.left, root.right);
    }
    
    private boolean isMirror(TreeNode left, TreeNode right) {
        // Both null - symmetric
        if (left == null && right == null) {
            return true;
        }
        
        // One null, one not - not symmetric
        if (left == null || right == null) {
            return false;
        }
        
        // Check value and recursively check subtrees
        return (left.val == right.val) &&
               isMirror(left.left, right.right) &&
               isMirror(left.right, right.left);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Visit each node once
- **Space Complexity:** O(h) - Recursion stack, h = height

---

## Approach 2: Iterative with Queue (Optimized Solution)

### Algorithm
1. Use a queue to store pairs of nodes to compare
2. Start with root.left and root.right
3. For each pair, check values and add children in mirror order
4. Continue until queue is empty

### Java Code
```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root.left);
        queue.offer(root.right);
        
        while (!queue.isEmpty()) {
            TreeNode left = queue.poll();
            TreeNode right = queue.poll();
            
            // Both null - continue
            if (left == null && right == null) {
                continue;
            }
            
            // One null or values don't match - not symmetric
            if (left == null || right == null || left.val != right.val) {
                return false;
            }
            
            // Add children in mirror order
            queue.offer(left.left);
            queue.offer(right.right);
            queue.offer(left.right);
            queue.offer(right.left);
        }
        
        return true;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Visit each node once
- **Space Complexity:** O(w) - Queue size, w = max width of tree

### Why This is Better
- ✅ Avoids recursion stack overflow for deep trees
- ✅ More explicit control flow
- ✅ Same time complexity but iterative

---

## Key Takeaways

1. **Pattern:** Mirror comparison requires checking opposite sides
2. **Recursion:** Natural fit for tree problems
3. **Iterative alternative:** Use queue for level-by-level comparison
4. **Base cases:** Handle null nodes carefully

---

## Edge Cases

- Single node: `[1]` → `true`
- Two nodes: `[1,2,2]` → `true`
- Asymmetric values: `[1,2,2,3,4,4,5]` → `false`
- Asymmetric structure: `[1,2,2,null,3,null,3]` → `false`

---

## Related Problems
- [[Same-Tree]] - Similar tree comparison
- [[Invert-Binary-Tree]] - Tree transformation
- [[Maximum-Depth-of-Binary-Tree]] - Tree traversal

---

## Tags
#trees #recursion #bfs #dfs #easy #blind75
