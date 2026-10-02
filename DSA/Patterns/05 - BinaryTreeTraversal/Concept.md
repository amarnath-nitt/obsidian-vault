# Binary Tree Traversal — Concept

## What Is It?

Binary Tree Traversal is the process of visiting every node in a binary tree exactly once, in a specific order. The three classic orders — **Inorder, Preorder, Postorder** — plus **Level Order (BFS)** form the foundation of all tree problems.

---

## When to Use

> **Trigger keywords:** "binary tree", "traverse", "visit all nodes", "tree order", "level by level"

| Trigger | Example |
|---------|---------|
| Need nodes in **sorted order** (BST) | Inorder traversal |
| Need to **serialize/rebuild** the tree | Preorder + Inorder |
| Need **bottom-up** computation | Postorder (height, delete) |
| Need **level-by-level** processing | Level order (BFS) |

---

## Variants

### 1. Inorder (Left → Root → Right)
```java
void inorder(TreeNode root) {
    if (root == null) return;
    inorder(root.left);
    process(root.val);   // ← visit
    inorder(root.right);
}
```
**Use case:** BST → sorted order

### 2. Preorder (Root → Left → Right)
```java
void preorder(TreeNode root) {
    if (root == null) return;
    process(root.val);   // ← visit
    preorder(root.left);
    preorder(root.right);
}
```
**Use case:** Clone tree, serialize

### 3. Postorder (Left → Right → Root)
```java
void postorder(TreeNode root) {
    if (root == null) return;
    postorder(root.left);
    postorder(root.right);
    process(root.val);   // ← visit
}
```
**Use case:** Delete tree, compute height

### 4. Level Order (BFS)
```java
Queue<TreeNode> queue = new LinkedList<>();
queue.offer(root);
while (!queue.isEmpty()) {
    int size = queue.size();
    for (int i = 0; i < size; i++) {
        TreeNode node = queue.poll();
        process(node.val);
        if (node.left != null) queue.offer(node.left);
        if (node.right != null) queue.offer(node.right);
    }
}
```

---

## Visual Walkthrough

```
        1
       / \
      2   3
     / \
    4   5

Inorder:   4 → 2 → 5 → 1 → 3  (Left, Root, Right)
Preorder:  1 → 2 → 4 → 5 → 3  (Root, Left, Right)
Postorder: 4 → 5 → 2 → 3 → 1  (Left, Right, Root)
Level:     1 → 2,3 → 4,5       (Level by level)
```

---

## Time/Space Complexity

| Traversal | Time | Space |
|-----------|------|-------|
| All DFS variants | O(n) | O(h) stack — h = height |
| BFS (Level Order) | O(n) | O(w) queue — w = max width |
| Iterative with stack | O(n) | O(h) |

---

## Common Mistakes

1. **Forgetting null check** → Always check `if (root == null) return` first
2. **Confusing traversal orders** → Remember: Pre="Root first", In="Root middle", Post="Root last"
3. **Not tracking level size in BFS** → Must capture `queue.size()` before inner loop

---

## Related Patterns

- [[10 - BreadthFirstSearch/Concept|BFS]] — Level order traversal extended to graphs
- [[11 - DepthFirstSearch/Concept|DFS]] — Inorder/Preorder/Postorder are DFS variants
- [[01 - Recursion/Concept|Recursion]] — Tree traversals are natural recursive problems

---

#binary-tree #traversal #dsa #concept
