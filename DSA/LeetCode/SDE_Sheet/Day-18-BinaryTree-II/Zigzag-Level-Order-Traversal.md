# Zigzag Level Order Traversal

**LeetCode 103** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

### Approach

- Standard BFS level order
- Alternate direction with a boolean flag
- Use `LinkedList` to add to front or back based on direction

### Java Solution

```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        boolean leftToRight = true;

        while (!queue.isEmpty()) {
            Deque<Integer> level = new ArrayDeque<>();
            for (int size = queue.size(); size > 0; size--) {
                TreeNode node = queue.poll();
                if (leftToRight) level.addLast(node.val);
                else level.addFirst(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(new ArrayList<>(level));
            leftToRight = !leftToRight;
        }
        return result;
    }
}
```

---
