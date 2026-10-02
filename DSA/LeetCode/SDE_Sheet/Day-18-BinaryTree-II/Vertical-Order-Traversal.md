# Vertical Order Traversal

**LeetCode 987** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)

### Problem
Return vertical order traversal. Nodes at same position sorted by value.

### Approach

- Assign `(col, row)` to each node
- Sort by: col → row → value
- Group by column

### Java Solution

```java
class Solution {
    List<int[]> nodes = new ArrayList<>(); // [col, row, val]

    public List<List<Integer>> verticalTraversal(TreeNode root) {
        dfs(root, 0, 0);
        nodes.sort((a, b) -> a[0] != b[0] ? a[0] - b[0] :
                             a[1] != b[1] ? a[1] - b[1] : a[2] - b[2]);

        List<List<Integer>> result = new ArrayList<>();
        int prevCol = Integer.MIN_VALUE;

        for (int[] node : nodes) {
            if (node[0] != prevCol) {
                result.add(new ArrayList<>());
                prevCol = node[0];
            }
            result.get(result.size() - 1).add(node[2]);
        }
        return result;
    }

    private void dfs(TreeNode node, int col, int row) {
        if (node == null) return;
        nodes.add(new int[]{col, row, node.val});
        dfs(node.left, col - 1, row + 1);
        dfs(node.right, col + 1, row + 1);
    }
}
```

**Complexity:** Time O(n log n) · Space O(n)

---
