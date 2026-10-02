# Binary Tree Level Order Traversal

**Difficulty:** Medium
**Category:** Trees
**LeetCode Link:** [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

---

## Problem Statement

Given the `root` of a binary tree, return the level order traversal of its nodes' values (left to right, level by level).

**Example:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

---

## Intuition

Level order traversal processes nodes level by level — exactly what BFS does. The key trick is capturing the queue size at the start of each level to know how many nodes belong to that level.

---

## Approach: BFS with Queue

### Algorithm
1. Add root to queue
2. While queue is not empty:
   - Record current queue size = number of nodes at this level
   - Process exactly that many nodes, collecting their values
   - Add their children to the queue
   - Add the level's values to result

### Java Code
```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> level = new ArrayList<>();

            for (int i = 0; i < levelSize; i++) {
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

### Complexity Analysis
- **Time Complexity:** O(n) — every node visited once
- **Space Complexity:** O(w) — queue holds at most one full level, w = max width

---

## Step-by-Step Example

For `[3,9,20,null,null,15,7]`:
```
Queue: [3]         → level = [3],     add 9, 20
Queue: [9,20]      → level = [9,20],  add 15, 7
Queue: [15,7]      → level = [15,7]
Result: [[3],[9,20],[15,7]]
```

---

## Key Takeaways

1. **Pattern:** BFS with level-size snapshot
2. **Level boundary:** `int levelSize = queue.size()` before the inner loop
3. **Foundation:** Many tree problems (right side view, zigzag, etc.) build on this

---

## Tags
#trees #bfs #medium #blind75
