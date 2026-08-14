# Day 20 — Binary Search Tree I

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** BST — Search, Insert, Delete, Validate
**Difficulty Mix:** Easy / Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Validate Binary Search Tree]] | 98 | Medium | ⬜ |
| 2 | [[#Search in BST]] | 700 | Easy | ⬜ |
| 3 | [[#Insert into BST]] | 701 | Medium | ⬜ |
| 4 | [[#Delete Node in BST]] | 450 | Medium | ⬜ |
| 5 | [[#Kth Smallest Element in BST]] | 230 | Medium | ⬜ |
| 6 | [[#Floor and Ceil in BST]] | — | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Validate Binary Search Tree | Inorder list, then check sorted order. O(n) space. | Recursive range validation. O(n), O(h). | Iterative inorder with previous value, or Morris for O(1) extra. |
| Search in BST | Treat as a binary tree and DFS all nodes. O(n). | Recursive BST search. O(h). | Iterative BST search. O(h), O(1). |
| Insert into BST | Rebuild tree with the new value. O(n). | Recursive insert using BST property. O(h). | Iterative insert with parent pointer. O(h), O(1). |
| Delete Node in BST | Inorder all values, remove, rebuild. O(n). | Recursive delete using successor/predecessor. O(h). | Same idea with careful pointer updates; O(h) average. |
| Kth Smallest Element in BST | Full inorder list then index k-1. O(n) space. | Iterative inorder and stop after k nodes. O(h+k). | Morris inorder for O(1) extra space. |
| Floor and Ceil in BST | Inorder list then binary search. O(n) space. | Traverse using BST property for floor and ceil separately. O(h). | One pass can update floor/ceil candidates together. O(h). |

---

## BST Properties

```
For every node N:
  - All values in N.left subtree < N.val
  - All values in N.right subtree > N.val
  - No duplicates (typically)

Inorder traversal of BST → sorted ascending order ✅
```

---

## Validate Binary Search Tree

**LeetCode 98** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/validate-binary-search-tree/)

### Approach (Range Validation)

- Pass `(min, max)` valid range for each node
- Root: `(-∞, +∞)`, left child: `(min, node.val)`, right child: `(node.val, max)`

### Java Solution

```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean validate(TreeNode node, long min, long max) {
        if (node == null) return true;
        if (node.val <= min || node.val >= max) return false;
        return validate(node.left, min, node.val)
            && validate(node.right, node.val, max);
    }
}
```

**Complexity:** Time O(n) · Space O(h)

> **Alternative:** Inorder traversal and check if sorted (prev < current).

---

## Search in BST

**LeetCode 700** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/search-in-a-binary-search-tree/)

### Java Solution

```java
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null || root.val == val) return root;
        return val < root.val ? searchBST(root.left, val) : searchBST(root.right, val);
    }
}
```

**Complexity:** Time O(h) · Space O(h) → O(log n) balanced

---

## Insert into BST

**LeetCode 701** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

### Java Solution

```java
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);
        if (val < root.val) root.left = insertIntoBST(root.left, val);
        else root.right = insertIntoBST(root.right, val);
        return root;
    }
}
```

**Complexity:** Time O(h) · Space O(h)

---

## Delete Node in BST

**LeetCode 450** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/delete-node-in-a-bst/)

### Three Cases

1. **Node is a leaf** → return null
2. **Node has one child** → return the child
3. **Node has two children** → replace with **inorder successor** (smallest in right subtree), then delete successor

### Java Solution

```java
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else {
            // Found the node to delete
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            // Two children: find inorder successor (min of right subtree)
            TreeNode successor = findMin(root.right);
            root.val = successor.val;
            root.right = deleteNode(root.right, successor.val);
        }
        return root;
    }

    private TreeNode findMin(TreeNode node) {
        while (node.left != null) node = node.left;
        return node;
    }
}
```

**Complexity:** Time O(h) · Space O(h)

---

## Kth Smallest Element in BST

**LeetCode 230** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

### Approach

- Inorder traversal gives sorted order
- Stop at the kth element

### Java Solution (Iterative Inorder)

```java
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode curr = root;
        int count = 0;

        while (curr != null || !stack.isEmpty()) {
            while (curr != null) { stack.push(curr); curr = curr.left; }
            curr = stack.pop();
            if (++count == k) return curr.val;
            curr = curr.right;
        }
        return -1;
    }
}
```

**Complexity:** Time O(h+k) · Space O(h)

---

## Floor and Ceil in BST

**Floor(key):** Largest value ≤ key
**Ceil(key):** Smallest value ≥ key

```java
int floor(TreeNode root, int key) {
    int floor = -1;
    while (root != null) {
        if (root.val == key) return key;
        if (root.val > key) root = root.left;  // too big, go left
        else { floor = root.val; root = root.right; } // might have closer answer
    }
    return floor;
}

int ceil(TreeNode root, int key) {
    int ceil = -1;
    while (root != null) {
        if (root.val == key) return key;
        if (root.val < key) root = root.right; // too small, go right
        else { ceil = root.val; root = root.left; } // might have closer answer
    }
    return ceil;
}
```

---

## BST Operations Summary

| Operation | Complexity (balanced) | Key Idea |
|-----------|----------------------|----------|
| Search | O(log n) | Compare and go left/right |
| Insert | O(log n) | Find insertion point at leaf |
| Delete | O(log n) | Handle 3 cases; use inorder successor |
| kth smallest | O(log n + k) | Inorder traversal |
| Floor/Ceil | O(log n) | Track best candidate while searching |
| LCA | O(log n) | If both < root → go left; both > root → go right |

#sde-sheet #bst #day20
