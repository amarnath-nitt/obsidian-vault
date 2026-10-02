# Serialize and Deserialize Binary Tree

**Difficulty:** Hard
**Category:** Trees
**LeetCode Link:** [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

---

## Problem Statement

Design an algorithm to serialize a binary tree to a string and deserialize that string back to the original tree structure.

**Example:**
```
Input: root = [1,2,3,null,null,4,5]
Serialized: "1,2,null,null,3,4,null,null,5,null,null,"
Output: [1,2,3,null,null,4,5]
```

---

## Intuition

Use preorder traversal (root → left → right). Record `"null"` for missing nodes so the structure is unambiguous. During deserialization, consume tokens from a queue in the same preorder sequence to reconstruct the tree.

---

## Approach: Preorder DFS with Null Markers

### Algorithm

**Serialize:**
1. Preorder DFS — append `node.val + ","` or `"null,"` for null nodes

**Deserialize:**
1. Split string into tokens, put in a queue
2. Preorder DFS — poll from queue; if `"null"` return null, else create node and recurse for left then right

### Java Code
```java
public class Codec {

    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        serializeHelper(root, sb);
        return sb.toString();
    }

    private void serializeHelper(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append("null,");
            return;
        }
        sb.append(node.val).append(",");
        serializeHelper(node.left, sb);
        serializeHelper(node.right, sb);
    }

    public TreeNode deserialize(String data) {
        Queue<String> queue = new LinkedList<>(Arrays.asList(data.split(",")));
        return deserializeHelper(queue);
    }

    private TreeNode deserializeHelper(Queue<String> queue) {
        String val = queue.poll();
        if (val.equals("null")) return null;

        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = deserializeHelper(queue);
        node.right = deserializeHelper(queue);
        return node;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) — every node visited once in both operations
- **Space Complexity:** O(n) — string + queue storage

---

## Key Takeaways

1. **Preorder + null markers** = unambiguous serialization (no need for two traversals)
2. **Queue for deserialization:** Naturally consumes tokens in preorder sequence
3. **Delimiter:** Use `","` to separate values; handle `"null"` for missing nodes

---

## Tags
#trees #design #serialization #hard #blind75
