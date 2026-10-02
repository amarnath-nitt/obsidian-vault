# Shortest Path - Practice Notes

## Pattern Overview
Finding the shortest path in graphs using algorithms like Dijkstra's, Bellman-Ford, and Floyd-Warshall.

## Key Concepts
- **Dijkstra's**: For weighted graphs with non-negative weights
- **Bellman-Ford**: Handles negative weights
- **BFS**: For unweighted graphs
- **Time Complexity**: O((V + E) log V) for Dijkstra's

## Template Code

### Dijkstra's Algorithm
```java
public int[] dijkstra(int n, int[][] edges, int start) {
    List<int[]>[] graph = new ArrayList[n];
    for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
    
    for (int[] edge : edges) {
        graph[edge[0]].add(new int[]{edge[1], edge[2]});
    }
    
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[start] = 0;
    
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
    pq.offer(new int[]{start, 0});
    
    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int node = curr[0], d = curr[1];
        
        if (d > dist[node]) continue;
        
        for (int[] edge : graph[node]) {
            int neighbor = edge[0], weight = edge[1];
            int newDist = dist[node] + weight;
            if (newDist < dist[neighbor]) {
                dist[neighbor] = newDist;
                pq.offer(new int[]{neighbor, newDist});
            }
        }
    }
    return dist;
}
```

### BFS for Unweighted Graph
```java
public int shortestPath(int start, int end, int n, int[][] edges) {
    List<Integer>[] graph = new ArrayList[n];
    for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
    for (int[] edge : edges) {
        graph[edge[0]].add(edge[1]);
    }
    
    Queue<Integer> queue = new LinkedList<>();
    boolean[] visited = new boolean[n];
    queue.offer(start);
    visited[start] = true;
    int distance = 0;
    
    while (!queue.isEmpty()) {
        int size = queue.size();
        for (int i = 0; i < size; i++) {
            int node = queue.poll();
            if (node == end) return distance;
            for (int neighbor : graph[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.offer(neighbor);
                }
            }
        }
        distance++;
    }
    return -1;
}
```

## Practice Problems

### Medium
- [ ] [Network Delay Time](https://leetcode.com/problems/network-delay-time/) (LC 743) → [Solution](solutions/LC-743-Network-Delay-Time.md)
- [ ] [Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) (LC 1514) → [Solution](solutions/LC-1514-Path-Maximum-Probability.md)
- [ ] [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) (LC 210) → [Solution](solutions/LC-210-Course-Schedule-II.md)
- [ ] [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) (LC 787) → [Solution](solutions/LC-787-Cheapest-Flights-Within-K-Stops.md)
- [ ] [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) (LC 1091) → [Solution](solutions/LC-1091-Shortest-Path-in-Binary-Matrix.md)

### Hard
- [ ] [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) (LC 847) → [Solution](solutions/LC-847-Shortest-Path-Visiting-All-Nodes.md)
- [ ] [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) (LC 778) → [Solution](solutions/LC-778-Swim-in-Rising-Water.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gJpZczEW)
