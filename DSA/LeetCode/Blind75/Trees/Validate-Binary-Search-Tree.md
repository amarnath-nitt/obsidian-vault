# Validate Binary Search Tree

**Difficulty:** Medium
**Category:** Trees
**LeetCode Link:** [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

---

## Problem Statement

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST). A valid BST requires every node's value to be strictly greater than all values in its left subtree and strictly less than all values in its right subtree.

**Example:**
```
Input: root = [5,1,4,null,null,3,6]
Output: false  (4 is in right subtree of 5 but 4 < 5)
```

---

## Intuition

A common mistake is only comparing a node with its direct children. But BST validity is a global constraint — every node must lie within a valid range inherited from its ancestors. Pass `min` and `max` bounds down the recursion.

---

## Approach 1: Recursive with Range (Optimized)

### Algorithm
1. Each node must satisfy `min < node.val < max`
2. When going left, update max = current node's value
3. When going right, update min = current node's value
4. Start with min = null, max = null (no bounds)

### Java Code
```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return validate(root, null, null);
    }

    private boolean validate(TreeNode node, Integer min, Integer max) {
        if (node == null) return true;

        if (min != null && node.val <= min) return false;
        if (max != null && node.val >= max) return false;

        return validate(node.left, min, node.val) &&
               validate(node.right, node.val, max);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) — visit every node
- **Space Complexity:** O(h) — recursion stack

---

## Approach 2: Inorder Traversal

### Algorithm
Inorder traversal of a valid BST produces a strictly increasing sequence. Track the previous value and verify each node is greater.

### Java Code
```java
class Solution {
    private Integer prev = null;

    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;

        if (!isValidBST(root.left)) return false;

        if (prev != null && root.val <= prev) return false;
        prev = root.val;

        return isValidBST(root.right);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## Key Takeaways

1. **Common mistake:** Only checking parent-child relationship — wrong for nodes deeper in the tree
2. **Range propagation:** Pass inherited bounds down the tree
3. **Inorder alternative:** Valid BST ↔ strictly increasing inorder sequence

---

## Tags
#trees #dfs #bst #medium #blind75
