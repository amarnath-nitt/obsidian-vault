# Invert Binary Tree

**Difficulty:** Easy
**Category:** Trees
**LeetCode Link:** [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

---

## Problem Statement

Given the `root` of a binary tree, invert the tree, and return its root.

**Example:**
```
Input:  [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

---

## Intuition

To invert a binary tree, every node's left and right children must be swapped. This is naturally recursive — swap children at the current node, then recursively invert both subtrees.

---

## Approach 1: Recursive DFS

### Algorithm
1. Base case: if node is null, return null
2. Swap left and right children
3. Recursively invert left subtree
4. Recursively invert right subtree
5. Return root

### Java Code
```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        invertTree(root.left);
        invertTree(root.right);

        return root;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) — every node visited once
- **Space Complexity:** O(h) — recursion stack, h = height

---

## Approach 2: Iterative BFS

### Algorithm
1. Use a queue, start with root
2. For each node, swap its children
3. Add non-null children to queue

### Java Code
```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();

            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;

            if (node.left != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }

        return root;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(w) — queue size, w = max width

---

## Key Takeaways

1. **Pattern:** Pre-order DFS — process node before children
2. **Recursive trust:** Assume recursive call correctly inverts subtree
3. **BFS alternative:** Iterative approach avoids stack overflow on deep trees

---

## Tags
#trees #dfs #bfs #recursion #easy #blind75
