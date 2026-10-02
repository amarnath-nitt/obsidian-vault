# Clone Graph

**Difficulty:** Medium
**Category:** Graphs
**LeetCode Link:** [Clone Graph](https://leetcode.com/problems/clone-graph/)

---

## Problem Statement

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node contains a value and a list of neighbors.

**Example:**
```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
```

---

## Intuition

The challenge is handling cycles — without tracking visited nodes, we'd loop forever. Use a HashMap to map each original node to its clone. When we encounter a node already in the map, return the existing clone instead of creating a new one.

---

## Approach: DFS with HashMap

### Algorithm
1. If node is null, return null
2. If node already cloned (in map), return its clone
3. Create a new clone node, add to map
4. Recursively clone all neighbors and add to clone's neighbor list

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

### Complexity Analysis
- **Time Complexity:** O(N + E) — visit every node and edge once
- **Space Complexity:** O(N) — HashMap stores all clones

---

## Approach 2: BFS with HashMap

### Java Code
```java
class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;

        Map<Node, Node> map = new HashMap<>();
        Queue<Node> queue = new LinkedList<>();

        map.put(node, new Node(node.val));
        queue.offer(node);

        while (!queue.isEmpty()) {
            Node curr = queue.poll();

            for (Node neighbor : curr.neighbors) {
                if (!map.containsKey(neighbor)) {
                    map.put(neighbor, new Node(neighbor.val));
                    queue.offer(neighbor);
                }
                map.get(curr).neighbors.add(map.get(neighbor));
            }
        }

        return map.get(node);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(N + E)
- **Space Complexity:** O(N)

---

## Key Takeaways

1. **Pattern:** HashMap as visited set + clone registry
2. **Cycle handling:** Check map before creating new clone
3. **DFS vs BFS:** Both work; DFS is more concise

---

## Tags
#graphs #dfs #bfs #hash-table #medium #blind75
