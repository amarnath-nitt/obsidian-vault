# Serialize and Deserialize Binary Tree

**LeetCode 297** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

### Approach (Preorder with null markers)

- Serialize: preorder DFS, write "null" for null nodes
- Deserialize: parse the sequence, rebuild using same preorder logic

### Java Solution

```java
public class Codec {
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        serDfs(root, sb);
        return sb.toString();
    }

    private void serDfs(TreeNode node, StringBuilder sb) {
        if (node == null) { sb.append("null,"); return; }
        sb.append(node.val).append(",");
        serDfs(node.left, sb);
        serDfs(node.right, sb);
    }

    public TreeNode deserialize(String data) {
        Queue<String> queue = new LinkedList<>(Arrays.asList(data.split(",")));
        return desDfs(queue);
    }

    private TreeNode desDfs(Queue<String> queue) {
        String val = queue.poll();
        if (val.equals("null")) return null;
        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = desDfs(queue);
        node.right = desDfs(queue);
        return node;
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---
