# Clone Graph

**LeetCode 133** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/clone-graph/)

### Approach (BFS + HashMap)

- Map: `original node → cloned node`
- BFS: for each original node, clone neighbors

### Java Solution

```java
class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        Map<Node, Node> cloned = new HashMap<>();
        Queue<Node> queue = new LinkedList<>();
        queue.offer(node);
        cloned.put(node, new Node(node.val));

        while (!queue.isEmpty()) {
            Node curr = queue.poll();
            for (Node neighbor : curr.neighbors) {
                if (!cloned.containsKey(neighbor)) {
                    cloned.put(neighbor, new Node(neighbor.val));
                    queue.offer(neighbor);
                }
                cloned.get(curr).neighbors.add(cloned.get(neighbor));
            }
        }
        return cloned.get(node);
    }
}
```

**Complexity:** Time O(V+E) · Space O(V)

---
