# Binary Tree Right Side View

**LeetCode 199** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/binary-tree-right-side-view/)

### Approach
BFS level order — collect the **last** node at each level.

### Java Solution

```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (i == size - 1) result.add(node.val); // last of level
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
        return result;
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---
