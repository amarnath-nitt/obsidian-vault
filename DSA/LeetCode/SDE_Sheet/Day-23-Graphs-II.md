# Day 23 — Graphs II (Bipartite, Topological Sort)

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Graph — Bipartite Check, Topo Sort, SCCs
**Difficulty Mix:** Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Bipartite Graph Check]] | 785 | Medium | ⬜ |
| 2 | [[#Topological Sort (Kahn's BFS)]] | — | Medium | ⬜ |
| 3 | [[#Course Schedule I]] | 207 | Medium | ⬜ |
| 4 | [[#Course Schedule II]] | 210 | Medium | ⬜ |
| 5 | [[#Find Eventual Safe States]] | 802 | Medium | ⬜ |
| 6 | [[#Alien Dictionary]] | 269 | Hard | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Bipartite Graph Check | Try all 2-color assignments. Exponential. | BFS/DFS coloring and reject same-color edges. O(V+E). | Same coloring across all components; DSU parity is an alternative. |
| Topological Sort | Repeatedly scan all vertices for zero indegree. O(V^2+E). | Kahn BFS with a queue. O(V+E). | DFS postorder topo is the other O(V+E) standard. |
| Course Schedule I | Try to build every possible course order. Exponential. | DFS cycle detection with states. O(V+E). | Kahn indegree count; if processed count < V, cycle exists. |
| Course Schedule II | Try permutations until one satisfies prerequisites. Exponential. | DFS postorder, reverse result. O(V+E). | Kahn BFS produces valid order directly. O(V+E). |
| Find Eventual Safe States | DFS every path repeatedly. O(V*(V+E)). | DFS coloring/memo safe and unsafe states. O(V+E). | Reverse graph + topo from terminal nodes. O(V+E). |
| Alien Dictionary | Try alphabet orders and validate. Exponential. | Build precedence graph from adjacent words, then topo sort. | Kahn topo with invalid-prefix handling and all unique chars. |

---

## Bipartite Graph Check

**LeetCode 785** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/is-graph-bipartite/)

### Problem
A graph is bipartite if we can color nodes with 2 colors such that no two adjacent nodes share the same color.

### Approach (BFS Coloring)

- Color nodes alternately
- If a neighbor has the same color → not bipartite

### Java Solution

```java
class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n]; // 0=uncolored, 1=red, -1=blue

        for (int i = 0; i < n; i++) {
            if (color[i] != 0) continue;
            Queue<Integer> queue = new LinkedList<>();
            queue.offer(i);
            color[i] = 1;
            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int neighbor : graph[node]) {
                    if (color[neighbor] == 0) {
                        color[neighbor] = -color[node];
                        queue.offer(neighbor);
                    } else if (color[neighbor] == color[node]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
```

**Complexity:** Time O(V+E) · Space O(V)

---

## Topological Sort (Kahn's BFS Algorithm)

**Problem:** Linear ordering of vertices in a DAG such that for every edge u→v, u comes before v.

### Approach (Kahn's — BFS with in-degree)

1. Compute **in-degree** of all nodes
2. Add all nodes with `in-degree == 0` to queue
3. Process queue: decrement neighbor's in-degree; if 0, add to queue
4. If total processed == n → valid topo sort; else cycle exists

### Java Solution

```java
List<Integer> topoSort(int n, List<List<Integer>> adj) {
    int[] inDegree = new int[n];
    for (int u = 0; u < n; u++)
        for (int v : adj.get(u)) inDegree[v]++;

    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < n; i++)
        if (inDegree[i] == 0) queue.offer(i);

    List<Integer> order = new ArrayList<>();
    while (!queue.isEmpty()) {
        int node = queue.poll();
        order.add(node);
        for (int neighbor : adj.get(node)) {
            if (--inDegree[neighbor] == 0) queue.offer(neighbor);
        }
    }
    return order.size() == n ? order : new ArrayList<>(); // empty if cycle
}
```

### DFS Topo Sort

```java
void dfsTopoSort(int node, boolean[] visited, Deque<Integer> stack, List<List<Integer>> adj) {
    visited[node] = true;
    for (int neighbor : adj.get(node))
        if (!visited[neighbor]) dfsTopoSort(neighbor, visited, stack, adj);
    stack.push(node); // push AFTER processing all neighbors
}
```

---

## Course Schedule I

**LeetCode 207** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/course-schedule/)

### Problem
Can you finish all courses given prerequisites? (Detect cycle in directed graph)

### Java Solution (Kahn's)

```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDegree = new int[numCourses];
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());

        for (int[] pre : prerequisites) {
            adj.get(pre[1]).add(pre[0]);
            inDegree[pre[0]]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++)
            if (inDegree[i] == 0) queue.offer(i);

        int count = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            count++;
            for (int next : adj.get(course))
                if (--inDegree[next] == 0) queue.offer(next);
        }
        return count == numCourses;
    }
}
```

**Complexity:** Time O(V+E) · Space O(V+E)

---

## Course Schedule II

**LeetCode 210** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/course-schedule-ii/)

### Problem
Return the order to take courses. Return empty if impossible.

### Java Solution (same as Kahn's — collect order)

```java
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDegree = new int[numCourses];
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());

        for (int[] pre : prerequisites) {
            adj.get(pre[1]).add(pre[0]);
            inDegree[pre[0]]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++)
            if (inDegree[i] == 0) queue.offer(i);

        int[] order = new int[numCourses];
        int idx = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            order[idx++] = course;
            for (int next : adj.get(course))
                if (--inDegree[next] == 0) queue.offer(next);
        }
        return idx == numCourses ? order : new int[]{};
    }
}
```

---

## Find Eventual Safe States

**LeetCode 802** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/find-eventual-safe-states/)

### Problem
A node is "safe" if every path from it leads to a terminal node (no cycle).

### Approach

- A node is safe if it's NOT in a cycle
- Reverse the graph and find nodes reachable from terminal nodes using Kahn's

```java
class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        List<List<Integer>> reverseGraph = new ArrayList<>();
        int[] inDegree = new int[n];
        for (int i = 0; i < n; i++) reverseGraph.add(new ArrayList<>());

        for (int u = 0; u < n; u++)
            for (int v : graph[u]) {
                reverseGraph.get(v).add(u);
                inDegree[u]++;
            }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++)
            if (inDegree[i] == 0) queue.offer(i);

        boolean[] safe = new boolean[n];
        while (!queue.isEmpty()) {
            int node = queue.poll();
            safe[node] = true;
            for (int prev : reverseGraph.get(node))
                if (--inDegree[prev] == 0) queue.offer(prev);
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) if (safe[i]) result.add(i);
        return result;
    }
}
```

---

## Alien Dictionary

**LeetCode 269** · Hard

### Problem
Given sorted list of words in alien language, find the alien alphabet order.

### Approach

1. Compare adjacent words char by char → find first difference → edge `c1 → c2`
2. Topological sort on character graph
3. If `word2` is prefix of `word1` → invalid ("abc" before "ab" is wrong)

```java
public String alienOrder(String[] words) {
    Map<Character, Set<Character>> adj = new HashMap<>();
    Map<Character, Integer> inDegree = new HashMap<>();
    for (String w : words) for (char c : w.toCharArray()) {
        adj.putIfAbsent(c, new HashSet<>());
        inDegree.putIfAbsent(c, 0);
    }

    for (int i = 0; i < words.length - 1; i++) {
        String w1 = words[i], w2 = words[i+1];
        if (w1.length() > w2.length() && w1.startsWith(w2)) return "";
        for (int j = 0; j < Math.min(w1.length(), w2.length()); j++) {
            if (w1.charAt(j) != w2.charAt(j)) {
                if (!adj.get(w1.charAt(j)).contains(w2.charAt(j))) {
                    adj.get(w1.charAt(j)).add(w2.charAt(j));
                    inDegree.merge(w2.charAt(j), 1, Integer::sum);
                }
                break;
            }
        }
    }

    Queue<Character> queue = new LinkedList<>();
    for (char c : inDegree.keySet()) if (inDegree.get(c) == 0) queue.offer(c);
    StringBuilder sb = new StringBuilder();
    while (!queue.isEmpty()) {
        char c = queue.poll();
        sb.append(c);
        for (char next : adj.get(c))
            if (inDegree.merge(next, -1, Integer::sum) == 0) queue.offer(next);
    }
    return sb.length() == inDegree.size() ? sb.toString() : "";
}
```

#sde-sheet #graphs #topological-sort #day23
