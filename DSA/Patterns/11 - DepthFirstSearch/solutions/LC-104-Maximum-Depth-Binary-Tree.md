# Maximum Depth of Binary Tree (LC 104)

**Difficulty**: Easy  
**Pattern**: Depth First Search  
**LeetCode**: https://leetcode.com/problems/maximum-depth-of-binary-tree/

## Problem Statement
Given the `root` of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example:**
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

## Approach 1: Recursive DFS

### Intuition
Max depth = 1 + max(depth of left subtree, depth of right subtree). Base case: null node has depth 0.

### Java Code
```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
```

### Complexity
- **Time**: O(n) - Visit every node once
- **Space**: O(h) - Height of tree (recursion stack), worst case O(n)

## Approach 2: Iterative DFS (Stack)

### Java Code
```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        
        Stack<Pair<TreeNode, Integer>> stack = new Stack<>();
        stack.push(new Pair<>(root, 1));
        
        int maxDepth = 0;
        
        while (!stack.isEmpty()) {
            Pair<TreeNode, Integer> current = stack.pop();
            TreeNode node = current.getKey();
            int depth = current.getValue();
            
            maxDepth = Math.max(maxDepth, depth);
            
            if (node.left != null) {
                stack.push(new Pair<>(node.left, depth + 1));
            }
            if (node.right != null) {
                stack.push(new Pair<>(node.right, depth + 1));
            }
        }
        
        return maxDepth;
    }
}
```

## Approach 3: BFS (Level Order)

### Java Code
```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int depth = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            depth++;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
        
        return depth;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(w) - Max width of tree (queue size)

## Key Takeaways
- Recursive DFS is most elegant for depth problems
- Base case is crucial (root == null)
- Can also be solved with BFS by counting levels
