# Day 17 — Binary Tree I

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Binary Tree — Traversals, Height, Diameter
**Difficulty Mix:** Easy / Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Binary Tree Traversals (In/Pre/Post)]] | 94/144/145 | Easy | ⬜ |
| 2 | [[#Level Order Traversal (BFS)]] | 102 | Medium | ⬜ |
| 3 | [[#Maximum Depth of Binary Tree]] | 104 | Easy | ⬜ |
| 4 | [[#Diameter of Binary Tree]] | 543 | Easy | ⬜ |
| 5 | [[#Balanced Binary Tree]] | 110 | Easy | ⬜ |
| 6 | [[#Same Tree]] | 100 | Easy | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Binary Tree Traversals | Recursive DFS. O(n) time, O(h) stack. | Iterative stack traversal. O(n), O(h). | Morris traversal for inorder/preorder when O(1) space is required. |
| Level Order Traversal | Compute height, then print each level. O(n*h). | Queue BFS. O(n). | Queue BFS with fixed level size for clean level grouping. O(n). |
| Maximum Depth of Binary Tree | Level-order count levels. O(n). | Recursive height. O(n), O(h). | Iterative DFS/BFS avoids recursion-depth issues. O(n). |
| Diameter of Binary Tree | Compute height separately for every node. O(n^2). | One DFS returns height and updates diameter. O(n). | Same bottom-up DFS with global/holder max. |
| Balanced Binary Tree | Check height at every node repeatedly. O(n^2). | Bottom-up height computation. O(n). | Return -1 on imbalance for early exit. O(n). |
| Same Tree | Serialize both trees and compare. O(n) space. | Recursive node-by-node comparison. O(n). | Iterative stack/queue comparison avoids recursion overflow. |

---

## Binary Tree Traversals (In/Pre/Post)

### Recursive

```java
// Inorder: Left → Root → Right
void inorder(TreeNode root, List<Integer> result) {
    if (root == null) return;
    inorder(root.left, result);
    result.add(root.val);
    inorder(root.right, result);
}

// Preorder: Root → Left → Right
void preorder(TreeNode root, List<Integer> result) {
    if (root == null) return;
    result.add(root.val);
    preorder(root.left, result);
    preorder(root.right, result);
}

// Postorder: Left → Right → Root
void postorder(TreeNode root, List<Integer> result) {
    if (root == null) return;
    postorder(root.left, result);
    postorder(root.right, result);
    result.add(root.val);
}
```

### Iterative Inorder (with Stack)

```java
public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    Deque<TreeNode> stack = new ArrayDeque<>();
    TreeNode curr = root;

    while (curr != null || !stack.isEmpty()) {
        while (curr != null) { stack.push(curr); curr = curr.left; }
        curr = stack.pop();
        result.add(curr.val);
        curr = curr.right;
    }
    return result;
}
```

### Iterative Postorder (Two Stacks)

```java
public List<Integer> postorderTraversal(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    if (root == null) return result;
    Deque<TreeNode> s1 = new ArrayDeque<>(), s2 = new ArrayDeque<>();
    s1.push(root);
    while (!s1.isEmpty()) {
        TreeNode node = s1.pop();
        s2.push(node);
        if (node.left != null) s1.push(node.left);
        if (node.right != null) s1.push(node.right);
    }
    while (!s2.isEmpty()) result.add(s2.pop().val);
    return result;
}
```

---

## Level Order Traversal (BFS)

**LeetCode 102** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/binary-tree-level-order-traversal/)

### Java Solution

```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            for (int size = queue.size(); size > 0; size--) {
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

**Complexity:** Time O(n) · Space O(n)

---

## Maximum Depth of Binary Tree

**LeetCode 104** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

### Java Solution

```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
```

**Complexity:** Time O(n) · Space O(h) where h = height

---

## Diameter of Binary Tree

**LeetCode 543** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/diameter-of-binary-tree/)

### Problem
Find the longest path between any two nodes (doesn't need to pass through root).

### Approach

- Diameter through a node = `leftHeight + rightHeight`
- Update global max during DFS

### Java Solution

```java
class Solution {
    int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        height(root);
        return maxDiameter;
    }

    private int height(TreeNode node) {
        if (node == null) return 0;
        int left = height(node.left);
        int right = height(node.right);
        maxDiameter = Math.max(maxDiameter, left + right);
        return 1 + Math.max(left, right);
    }
}
```

**Complexity:** Time O(n) · Space O(h)

---

## Balanced Binary Tree

**LeetCode 110** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/balanced-binary-tree/)

### Problem
Is the binary tree height-balanced? (|leftHeight - rightHeight| ≤ 1 for every node)

### Approach

- Return -1 from height function to signal "unbalanced"
- If height difference > 1, propagate -1 upward

### Java Solution

```java
class Solution {
    public boolean isBalanced(TreeNode root) {
        return checkHeight(root) != -1;
    }

    private int checkHeight(TreeNode node) {
        if (node == null) return 0;
        int left = checkHeight(node.left);
        if (left == -1) return -1;
        int right = checkHeight(node.right);
        if (right == -1) return -1;
        if (Math.abs(left - right) > 1) return -1;
        return 1 + Math.max(left, right);
    }
}
```

**Complexity:** Time O(n) · Space O(h)

---

## Same Tree

**LeetCode 100** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/same-tree/)

### Java Solution

```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        return p.val == q.val
            && isSameTree(p.left, q.left)
            && isSameTree(p.right, q.right);
    }
}
```

---

## Tree Traversal Cheatsheet

| Traversal | Order | Key Use |
|-----------|-------|---------|
| Inorder | L→Root→R | BST sorted order |
| Preorder | Root→L→R | Copy tree, serialize |
| Postorder | L→R→Root | Delete tree, evaluate expression tree |
| Level order | BFS | Level-by-level, shortest path in tree |

---

## Binary Tree Problem-Solving Framework

```
Most tree problems = DFS that returns something useful

Template:
  solve(node):
    if node == null: return baseCase
    leftResult = solve(node.left)
    rightResult = solve(node.right)
    // combine leftResult, rightResult, node.val
    return something

What to return:
  - height / depth
  - (isValid, minVal, maxVal)
  - count / sum
  - -1 for invalid flag
```

#sde-sheet #binary-tree #day17
