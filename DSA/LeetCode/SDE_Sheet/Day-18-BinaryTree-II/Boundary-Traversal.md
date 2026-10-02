# Boundary Traversal

**Problem:** Print the boundary of a binary tree (anti-clockwise): left boundary + leaves + right boundary (reversed).

### Approach

1. **Left boundary**: root → left subtree top → before last leaf (going down left)
2. **All leaves**: in-order DFS to collect all leaf nodes
3. **Right boundary**: (right subtree → root) reversed, excluding last leaf

```java
public List<Integer> boundaryOfBinaryTree(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    if (root == null) return result;
    if (!isLeaf(root)) result.add(root.val);

    // Left boundary (top-down, not including leaf)
    TreeNode node = root.left;
    while (node != null) {
        if (!isLeaf(node)) result.add(node.val);
        node = (node.left != null) ? node.left : node.right;
    }

    // All leaves
    addLeaves(root, result);

    // Right boundary (bottom-up, not including leaf)
    Deque<Integer> stack = new ArrayDeque<>();
    node = root.right;
    while (node != null) {
        if (!isLeaf(node)) stack.push(node.val);
        node = (node.right != null) ? node.right : node.left;
    }
    while (!stack.isEmpty()) result.add(stack.pop());
    return result;
}

boolean isLeaf(TreeNode node) { return node.left == null && node.right == null; }
void addLeaves(TreeNode node, List<Integer> result) {
    if (node == null) return;
    if (isLeaf(node)) { result.add(node.val); return; }
    addLeaves(node.left, result);
    addLeaves(node.right, result);
}
```

---
