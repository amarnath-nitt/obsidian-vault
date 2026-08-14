# Clone Graph

[Problem Link](https://leetcode.com/problems/clone-graph/)

## Problem Statement
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

## Approach
DFS with a HashMap to store visited nodes.
Map `originalNode -> clonedNode`.
1.  If node is null, return null.
2.  If node in map, return map value (cloned node).
3.  Create new clone node. Put in map.
4.  For each neighbor, recursively clone and add to clone's neighbors.

## Time and Space Complexity
- **Time Complexity:** O(V + E).
- **Space Complexity:** O(V).

## Code
```java
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

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
