# Serialize and Deserialize Binary Tree

[Problem Link](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.

## Approach
Preorder Traversal (DFS).
- **Serialize**: Visit root. Append val + delimiter. If null, append "#" + delimiter. Recurse left, recurse right.
- **Deserialize**: Split string by delimiter. Use a Queue.
    - Poll first value. If "#", return null.
    - Create node.
    - Node.left = recurse.
    - Node.right = recurse.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```java
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        serializeHelper(root, sb);
        return sb.toString();
    }
    
    private void serializeHelper(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append("X").append(",");
            return;
        }
        sb.append(node.val).append(",");
        serializeHelper(node.left, sb);
        serializeHelper(node.right, sb);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Queue<String> queue = new LinkedList<>(Arrays.asList(data.split(",")));
        return deserializeHelper(queue);
    }
    
    private TreeNode deserializeHelper(Queue<String> queue) {
        String val = queue.poll();
        if ("X".equals(val)) {
            return null;
        }
        
        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = deserializeHelper(queue);
        node.right = deserializeHelper(queue);
        return node;
    }
}
```
