# Same Tree

**Difficulty:** Easy
**Category:** Trees
**LeetCode Link:** [Same Tree](https://leetcode.com/problems/same-tree/)

---

## Problem Statement

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example:**
```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

---

## Intuition

Two trees are the same if their roots have equal values AND their left subtrees are the same AND their right subtrees are the same. This is a natural recursive definition.

---

## Approach: Recursive DFS

### Algorithm
1. If both nodes are null → same (base case)
2. If one is null and the other isn't → not same
3. If values differ → not same
4. Recursively check left and right subtrees

### Java Code
```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;

        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) — visit every node in both trees
- **Space Complexity:** O(h) — recursion stack

---

## Step-by-Step Example

For `p = [1,2,3]`, `q = [1,2,3]`:
```
isSameTree(1, 1): values match
  isSameTree(2, 2): values match
    isSameTree(null, null): true
    isSameTree(null, null): true
  → true
  isSameTree(3, 3): values match
    isSameTree(null, null): true
    isSameTree(null, null): true
  → true
→ true
```

---

## Key Takeaways

1. **Pattern:** Simultaneous DFS on two trees
2. **Three null checks:** Both null, one null, neither null
3. **Short-circuit:** Return false early on mismatch

---

## Tags
#trees #dfs #recursion #easy #blind75
