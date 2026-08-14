# Binary Tree Postorder Traversal (LC 145)

**Difficulty**: Easy  
**Pattern**: Binary Tree Traversal  
**LeetCode**: https://leetcode.com/problems/binary-tree-postorder-traversal/

## Problem Statement
Given the `root` of a binary tree, return the postorder traversal of its nodes' values.

**Example:**
```
Input: root = [1,null,2,3]
Output: [3,2,1]
```

## Approach 1: Recursive

### Intuition
Standard DFS: `dfs(left)`, `dfs(right)`, `visit(root)`.

### Java Code (Recursive)
```java
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        dfs(root, result);
        return result;
    }
    
    private void dfs(TreeNode node, List<Integer> result) {
        if (node == null) return;
        dfs(node.left, result);
        dfs(node.right, result);
        result.add(node.val);
    }
}
```

## Approach 2: Iterative

### Intuition
Iterative Postorder is tricky (Left-Right-Root).
Reverse Preorder (Root-Right-Left) is easier to implement, then reverse result.
Or use 2 stacks. OR keep track of last visited node to distinguish returning from Left vs returning from Right.
Here is the "Reverse Preorder" trick which is concise:
Traverse Root -> Right -> Left.
Add to front of LinkedList (or reverse ArrayList at end).
Result: Left -> Right -> Root.

### Java Code (Iterative)
```java
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        LinkedList<Integer> result = new LinkedList<>();
        if (root == null) return result;
        
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        
        while (!stack.isEmpty()) {
            TreeNode curr = stack.pop();
            result.addFirst(curr.val); // Add to front (Reverse step)
            
            // Push Left then Right, so we process Right then Left
            if (curr.left != null) stack.push(curr.left);
            if (curr.right != null) stack.push(curr.right);
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(N)

## Key Takeaways
- Recursive is trivial
- Iterative can be done via "Reverse Root-Right-Left"
