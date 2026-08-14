# Day 21 — Binary Search Tree II

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** BST — LCA, Two Sum, Merge, Convert
**Difficulty Mix:** Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Lowest Common Ancestor of BST]] | 235 | Medium | ⬜ |
| 2 | [[#Two Sum in BST]] | 653 | Easy | ⬜ |
| 3 | [[#Recover BST (Two Nodes Swapped)]] | 99 | Hard | ⬜ |
| 4 | [[#Largest BST Subtree]] | 333 | Medium | ⬜ |
| 5 | [[#Merge Two BSTs]] | — | Hard | ⬜ |
| 6 | [[#Convert Sorted Array to BST]] | 108 | Easy | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Lowest Common Ancestor of BST | Use generic binary-tree LCA. O(n). | Store root-to-node paths and compare. O(h) space. | Use BST property to move left/right iteratively. O(h), O(1). |
| Two Sum in BST | Compare every pair of nodes. O(n^2). | DFS with HashSet of complements. O(n) space. | Two BST iterators like two pointers on inorder. O(n), O(h). |
| Recover BST | Inorder list, sort/copy values, find swapped nodes. O(n) space. | Inorder traversal detects two violations. O(h) stack. | Morris inorder detects violations in O(1) extra space. |
| Largest BST Subtree | Validate every subtree separately. O(n^2). | Bottom-up return min, max, size, and validity. O(n). | Same postorder DP with early invalid propagation. |
| Merge Two BSTs | Inorder both trees, concatenate, sort. O((m+n) log(m+n)). | Merge two sorted inorder arrays. O(m+n) space. | Two stack-based inorder iterators merge on the fly. O(h1+h2) extra. |
| Convert Sorted Array to BST | Insert values one by one; can become skewed. O(n^2). | Recursively choose middle as root. O(n). | Same range-based recursion without slicing arrays. O(n), O(log n) stack. |

---

## Lowest Common Ancestor of BST

**LeetCode 235** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

### Approach (Use BST property!)

- If both p and q < root → LCA is in left subtree
- If both p and q > root → LCA is in right subtree
- Otherwise → root is the LCA (they diverge here)

### Java Solution

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        while (root != null) {
            if (p.val < root.val && q.val < root.val) root = root.left;
            else if (p.val > root.val && q.val > root.val) root = root.right;
            else return root;
        }
        return null;
    }
}
```

**Complexity:** Time O(h) · Space O(1)

---

## Two Sum in BST

**LeetCode 653** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

### Problem
Find if there exist two nodes in BST that sum to target.

### Approach 1 — HashSet + DFS

```java
class Solution {
    Set<Integer> set = new HashSet<>();

    public boolean findTarget(TreeNode root, int k) {
        if (root == null) return false;
        if (set.contains(k - root.val)) return true;
        set.add(root.val);
        return findTarget(root.left, k) || findTarget(root.right, k);
    }
}
```

### Approach 2 — Inorder + Two Pointers

- Inorder traversal → sorted array → two pointer

**Complexity:** Time O(n) · Space O(n)

---

## Recover BST (Two Nodes Swapped)

**LeetCode 99** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/recover-binary-search-tree/)

### Problem
Two nodes of BST are swapped. Fix the BST without changing structure.

### Approach (Inorder traversal — find violation)

- Inorder of BST should be sorted
- **First violation**: `prev > curr` → first swapped node = `prev`
- **Second violation**: `prev > curr` again → second swapped node = `curr`
- Swap their values

### Java Solution

```java
class Solution {
    TreeNode first = null, second = null, prev = null;

    public void recoverTree(TreeNode root) {
        inorder(root);
        int tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }

    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        if (prev != null && prev.val > node.val) {
            if (first == null) first = prev;
            second = node;
        }
        prev = node;
        inorder(node.right);
    }
}
```

**Complexity:** Time O(n) · Space O(h)

---

## Largest BST Subtree

**LeetCode 333** · Medium
**Problem:** Find the largest subtree that is a valid BST.

### Approach (Bottom-up DP)

Return `(size, min, max)` from each node:
- Check if left and right subtrees are valid BSTs
- If current node can be root of a BST: `left.max < node.val < right.min`
- Return total size; propagate as `-1` for invalid

```java
class Solution {
    int maxSize = 0;

    public int largestBSTSubtree(TreeNode root) {
        solve(root);
        return maxSize;
    }

    // Returns [size, min, max] — size=-1 if not BST
    private int[] solve(TreeNode node) {
        if (node == null) return new int[]{0, Integer.MAX_VALUE, Integer.MIN_VALUE};

        int[] left = solve(node.left);
        int[] right = solve(node.right);

        if (left[0] == -1 || right[0] == -1
                || node.val <= left[2] || node.val >= right[1]) {
            return new int[]{-1, 0, 0};
        }

        int size = left[0] + right[0] + 1;
        maxSize = Math.max(maxSize, size);
        return new int[]{size, Math.min(left[1], node.val), Math.max(right[2], node.val)};
    }
}
```

---

## Merge Two BSTs

**Problem:** Merge two BSTs into one balanced BST.

### Approach

1. Inorder traversal of both BSTs → two sorted arrays
2. Merge two sorted arrays → one sorted array
3. Convert sorted array to balanced BST

```java
List<Integer> inorder(TreeNode root) { /* standard inorder */ }

List<Integer> merge(List<Integer> a, List<Integer> b) {
    /* standard merge of two sorted lists */
}

TreeNode sortedToBST(List<Integer> list, int l, int r) {
    if (l > r) return null;
    int mid = (l + r) / 2;
    TreeNode root = new TreeNode(list.get(mid));
    root.left = sortedToBST(list, l, mid - 1);
    root.right = sortedToBST(list, mid + 1, r);
    return root;
}
```

**Complexity:** Time O(m+n) · Space O(m+n)

---

## Convert Sorted Array to BST

**LeetCode 108** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

### Approach

- Middle element → root (ensures balance)
- Recursively do the same for left and right halves

### Java Solution

```java
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return build(nums, 0, nums.length - 1);
    }

    private TreeNode build(int[] nums, int l, int r) {
        if (l > r) return null;
        int mid = l + (r - l) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = build(nums, l, mid - 1);
        node.right = build(nums, mid + 1, r);
        return node;
    }
}
```

**Complexity:** Time O(n) · Space O(log n)

---

## BST vs Binary Tree Problem Strategy

| If problem says... | Use |
|---|---|
| "BST" | BST property: left < root < right |
| "LCA" in BST | Compare values with root (O(log n)) |
| "Inorder" | Automatically sorted in BST |
| "Two nodes swapped" | Find inversions in inorder |
| "Convert to balanced BST" | Inorder → middle as root |

#sde-sheet #bst #day21
