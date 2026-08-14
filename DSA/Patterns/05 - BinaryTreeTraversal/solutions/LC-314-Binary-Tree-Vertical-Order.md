# Binary Tree Vertical Order Traversal

[Problem Link](https://leetcode.com/problems/binary-tree-vertical-order-traversal/)

## Problem Statement
Given the `root` of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

## Approach
BFS with Column Index.
1.  Use a Queue storing pairs `(Node, Column)`.
2.  Use a Map `Column -> List<Values>` to store nodes at each column.
3.  Track `minCol` and `maxCol` to iterate result in order.
4.  BFS ensures top-to-bottom, left-to-right order naturally.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```java
class Solution {
    class Pair {
        TreeNode node;
        int col;
        Pair(TreeNode node, int col) {
            this.node = node;
            this.col = col;
        }
    }
    
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        
        Map<Integer, List<Integer>> map = new HashMap<>();
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(root, 0));
        
        int minCol = 0;
        int maxCol = 0;
        
        while (!queue.isEmpty()) {
            Pair curr = queue.poll();
            map.computeIfAbsent(curr.col, k -> new ArrayList<>()).add(curr.node.val);
            
            minCol = Math.min(minCol, curr.col);
            maxCol = Math.max(maxCol, curr.col);
            
            if (curr.node.left != null) {
                queue.offer(new Pair(curr.node.left, curr.col - 1));
            }
            if (curr.node.right != null) {
                queue.offer(new Pair(curr.node.right, curr.col + 1));
            }
        }
        
        for (int i = minCol; i <= maxCol; i++) {
            result.add(map.get(i));
        }
        
        return result;
    }
}
```
