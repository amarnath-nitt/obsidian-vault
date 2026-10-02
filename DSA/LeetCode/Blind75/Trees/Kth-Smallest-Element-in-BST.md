# Kth Smallest Element in a BST

**Difficulty:** Medium
**Category:** Trees
**LeetCode Link:** [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

---

## Problem Statement

Given the `root` of a binary search tree and an integer `k`, return the `kth` smallest value (1-indexed) among all node values.

**Example:**
```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

---

## Intuition

Inorder traversal of a BST visits nodes in ascending sorted order (left → root → right). So the kth node visited in inorder traversal is the kth smallest element.

---

## Approach 1: Recursive Inorder

### Algorithm
1. Traverse left subtree
2. Increment counter; if counter == k, record result
3. Traverse right subtree

### Java Code
```java
class Solution {
    private int count = 0;
    private int result = 0;

    public int kthSmallest(TreeNode root, int k) {
        inorder(root, k);
        return result;
    }

    private void inorder(TreeNode node, int k) {
        if (node == null) return;

        inorder(node.left, k);

        count++;
        if (count == k) {
            result = node.val;
            return;
        }

        inorder(node.right, k);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(H + k) — H = height to reach leftmost, then k steps
- **Space Complexity:** O(h) — recursion stack

---

## Approach 2: Iterative Inorder (Optimal for follow-up)

### Algorithm
Use an explicit stack to simulate inorder traversal, stopping as soon as we reach the kth element.

### Java Code
```java
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;

        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }

            curr = stack.pop();
            k--;
            if (k == 0) return curr.val;

            curr = curr.right;
        }

        return -1;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(H + k)
- **Space Complexity:** O(H) — stack depth

### Why Iterative is Better for Follow-up
If the BST is frequently modified (insert/delete) and we need to find kth smallest often, the iterative approach can be stopped early without completing the full traversal.

---

## Key Takeaways

1. **Pattern:** Inorder traversal of BST = sorted order
2. **Early stop:** No need to traverse the entire tree
3. **Iterative:** Better for streaming/frequent queries

---

## Tags
#trees #bst #inorder #medium #blind75
