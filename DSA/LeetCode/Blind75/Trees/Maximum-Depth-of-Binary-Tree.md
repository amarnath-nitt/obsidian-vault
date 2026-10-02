# Maximum Depth of Binary Tree

**Difficulty:** Easy
**Category:** Trees
**LeetCode Link:** [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

---

## Problem Statement

Given the `root` of a binary tree, return its maximum depth — the number of nodes along the longest path from root to the farthest leaf.

**Example:**
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

---

## Intuition

The depth of a tree is 1 + the maximum depth of its two subtrees. This is a classic post-order recursion — compute children's depths first, then combine.

---

## Approach 1: Recursive DFS (Post-order)

### Algorithm
1. Base case: null node has depth 0
2. Recursively get depth of left subtree
3. Recursively get depth of right subtree
4. Return `1 + max(left, right)`

### Java Code
```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;

        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);

        return Math.max(leftDepth, rightDepth) + 1;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) — visit every node
- **Space Complexity:** O(h) — recursion stack

---

## Approach 2: Iterative BFS (Level Order)

### Algorithm
1. Use a queue for level-order traversal
2. Count the number of levels processed

### Java Code
```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int depth = 0;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            depth++;

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }

        return depth;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(w) — max width of tree

---

## Key Takeaways

1. **Pattern:** Post-order DFS — combine results from children
2. **Base case:** null = depth 0
3. **BFS alternative:** Count levels directly

---

## Tags
#trees #dfs #bfs #recursion #easy #blind75
