# Clone Graph

**Difficulty:** Medium  
**Category:** Graphs  
**LeetCode Link:** [Clone Graph](https://leetcode.com/problems/clone-graph/)

---

## Approach: DFS with HashMap

### Java Code
```java
class Solution {
    private Map<Node, Node> visited = new HashMap<>();
    
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        
        if (visited.containsKey(node)) {
            return visited.get(node);
        }
        
        Node clone = new Node(node.val);
        visited.put(node, clone);
        
        for (Node neighbor : node.neighbors) {
            clone.neighbors.add(cloneGraph(neighbor));
        }
        
        return clone;
    }
}
```

### Complexity
- **Time:** O(N + E)
- **Space:** O(N)

---

## Tags
#graphs #dfs #hash-table #medium #blind75
