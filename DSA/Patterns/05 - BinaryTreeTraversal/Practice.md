# Binary Tree Traversal - Practice Notes

## Pattern Overview
Different ways to traverse binary trees: Preorder, Inorder, Postorder, and Level Order.

## Key Concepts
- **Preorder**: Root → Left → Right
- **Inorder**: Left → Root → Right
- **Postorder**: Left → Right → Root
- **Level Order**: Level by level (BFS)

## Template Code

### Preorder (Recursive)
```java
public void preorder(TreeNode root, List<Integer> result) {
    if (root == null) return;
    result.add(root.val);
    preorder(root.left, result);
    preorder(root.right, result);
}
```

### Inorder (Iterative)
```java
public List<Integer> inorder(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    Stack<TreeNode> stack = new Stack<>();
    TreeNode curr = root;
    
    while (curr != null || !stack.isEmpty()) {
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
        curr = stack.pop();
        result.add(curr.val);
        curr = curr.right;
    }
    return result;
}
```

### Level Order
```java
public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) return result;
    
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    
    while (!queue.isEmpty()) {
        int size = queue.size();
        List<Integer> level = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            TreeNode node = queue.poll();
            level.add(node.val);
            if (node.left != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }
        result.add(level);
    }
    return result;
}
```

## Practice Problems

### Easy
- [ ] [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) (LC 144) → [Solution](solutions/LC-144-Binary-Tree-Preorder-Traversal.md)
- [ ] [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) (LC 94) → [Solution](solutions/LC-94-Binary-Tree-Inorder-Traversal.md)
- [ ] [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) (LC 145) → [Solution](solutions/LC-145-Binary-Tree-Postorder-Traversal.md)
- [ ] [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) (LC 104) → [Solution](../DepthFirstSearch/solutions/LC-104-Maximum-Depth-Binary-Tree.md)

### Medium
- [ ] [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (LC 102) → [Solution](solutions/LC-102-Binary-Tree-Level-Order.md)
- [ ] [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) (LC 103) → [Solution](../BreadthFirstSearch/solutions/LC-103-Binary-Tree-Zigzag.md)
- [ ] [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) (LC 199) → [Solution](../BreadthFirstSearch/solutions/LC-199-Binary-Tree-Right-Side.md)
- [ ] [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) (LC 230) → [Solution](../DepthFirstSearch/solutions/LC-230-Kth-Smallest-Element-BST.md)

### Hard
- [ ] [Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) (LC 314) → [Solution](solutions/LC-314-Binary-Tree-Vertical-Order.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gWpgwvGc)
