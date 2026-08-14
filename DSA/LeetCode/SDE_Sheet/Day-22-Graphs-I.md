# Day 22 — Graphs I (BFS / DFS)

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Graph Fundamentals — BFS, DFS, Connected Components
**Difficulty Mix:** Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Number of Islands]] | 200 | Medium | ⬜ |
| 2 | [[#Clone Graph]] | 133 | Medium | ⬜ |
| 3 | [[#Flood Fill]] | 733 | Easy | ⬜ |
| 4 | [[#Detect Cycle in Undirected Graph]] | — | Medium | ⬜ |
| 5 | [[#Detect Cycle in Directed Graph]] | — | Medium | ⬜ |
| 6 | [[#Surrounded Regions]] | 130 | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Number of Islands | For each land cell, search its component repeatedly. O((m*n)^2). | DFS/BFS with visited marking. O(m*n). | In-place marking or DSU for repeated/dynamic connectivity. |
| Clone Graph | Clone nodes, then search cloned neighbors repeatedly. O(V*E). | DFS/BFS with original-to-clone map. O(V+E). | Iterative BFS map avoids recursion-depth issues. O(V+E). |
| Flood Fill | Repeatedly scan the image for connected color changes. | DFS/BFS from source only. O(m*n). | Same with early return when new color equals old color. |
| Detect Cycle in Undirected Graph | Remove/check edges or try all paths. Costly. | DFS/BFS with parent tracking. O(V+E). | DSU detects an edge connecting an existing component. O(E alpha(V)). |
| Detect Cycle in Directed Graph | Start DFS from every node without memo. O(V*(V+E)). | DFS with recursion-stack/color states. O(V+E). | Kahn topological sort; leftover nodes imply cycle. O(V+E). |
| Surrounded Regions | For each O, search whether it reaches boundary. O((m*n)^2). | Mark boundary-connected O cells with DFS/BFS. O(m*n). | Union-Find with dummy boundary node. O(m*n alpha(m*n)). |

---

## Graph Representations

```java
// Adjacency List (most common)
List<List<Integer>> adj = new ArrayList<>();
for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
adj.get(u).add(v);
adj.get(v).add(u); // undirected

// BFS Template
void bfs(int start, List<List<Integer>> adj, boolean[] visited) {
    Queue<Integer> queue = new LinkedList<>();
    queue.offer(start);
    visited[start] = true;
    while (!queue.isEmpty()) {
        int node = queue.poll();
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                queue.offer(neighbor);
            }
        }
    }
}

// DFS Template
void dfs(int node, List<List<Integer>> adj, boolean[] visited) {
    visited[node] = true;
    for (int neighbor : adj.get(node)) {
        if (!visited[neighbor]) dfs(neighbor, adj, visited);
    }
}
```

---

## Number of Islands

**LeetCode 200** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/number-of-islands/)

### Approach

- DFS/BFS from each unvisited '1' cell
- Mark all connected '1's as visited
- Count the number of DFS/BFS calls

### Java Solution (DFS)

```java
class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length, n = grid[0].length, count = 0;

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
        return count;
    }

    private void dfs(char[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] != '1')
            return;
        grid[i][j] = '0'; // mark visited
        dfs(grid, i+1, j); dfs(grid, i-1, j);
        dfs(grid, i, j+1); dfs(grid, i, j-1);
    }
}
```

**Complexity:** Time O(m×n) · Space O(m×n) stack

---

## Clone Graph

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

## Flood Fill

**LeetCode 733** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/flood-fill/)

### Java Solution

```java
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color) return image;
        dfs(image, sr, sc, image[sr][sc], color);
        return image;
    }

    private void dfs(int[][] image, int r, int c, int oldColor, int newColor) {
        if (r < 0 || r >= image.length || c < 0 || c >= image[0].length
                || image[r][c] != oldColor) return;
        image[r][c] = newColor;
        dfs(image, r+1, c, oldColor, newColor);
        dfs(image, r-1, c, oldColor, newColor);
        dfs(image, r, c+1, oldColor, newColor);
        dfs(image, r, c-1, oldColor, newColor);
    }
}
```

---

## Detect Cycle in Undirected Graph

### Approach (BFS / DFS with parent tracking)

- In undirected graph: cycle exists if we visit a visited node that is **not the parent**

```java
boolean hasCycleUndirected(int n, List<List<Integer>> adj) {
    boolean[] visited = new boolean[n];
    for (int i = 0; i < n; i++)
        if (!visited[i] && dfs(i, -1, adj, visited)) return true;
    return false;
}

boolean dfs(int node, int parent, List<List<Integer>> adj, boolean[] visited) {
    visited[node] = true;
    for (int neighbor : adj.get(node)) {
        if (!visited[neighbor]) {
            if (dfs(neighbor, node, adj, visited)) return true;
        } else if (neighbor != parent) return true; // back edge = cycle
    }
    return false;
}
```

---

## Detect Cycle in Directed Graph

### Approach (DFS with 3-color / recursion stack)

- `visited[v]` = false → unvisited
- `inStack[v]` = true → in current DFS path
- Back edge (neighbor is in stack) → cycle!

```java
boolean hasCycleDirected(int n, List<List<Integer>> adj) {
    boolean[] visited = new boolean[n], inStack = new boolean[n];
    for (int i = 0; i < n; i++)
        if (!visited[i] && dfs(i, adj, visited, inStack)) return true;
    return false;
}

boolean dfs(int node, List<List<Integer>> adj, boolean[] visited, boolean[] inStack) {
    visited[node] = inStack[node] = true;
    for (int neighbor : adj.get(node)) {
        if (!visited[neighbor] && dfs(neighbor, adj, visited, inStack)) return true;
        if (inStack[neighbor]) return true; // cycle
    }
    inStack[node] = false;
    return false;
}
```

---

## Surrounded Regions

**LeetCode 130** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/surrounded-regions/)

### Approach

- 'O's connected to the boundary cannot be flipped
- DFS from all boundary 'O's → mark as safe
- Flip remaining 'O' → 'X', restore safe marks → 'O'

```java
class Solution {
    public void solve(char[][] board) {
        int m = board.length, n = board[0].length;
        // Mark boundary-connected O's as safe
        for (int i = 0; i < m; i++) {
            dfs(board, i, 0); dfs(board, i, n-1);
        }
        for (int j = 0; j < n; j++) {
            dfs(board, 0, j); dfs(board, m-1, j);
        }
        // Flip
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                if (board[i][j] == '#') board[i][j] = 'O';
            }
    }

    void dfs(char[][] board, int r, int c) {
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != 'O') return;
        board[r][c] = '#'; // safe marker
        dfs(board, r+1, c); dfs(board, r-1, c);
        dfs(board, r, c+1); dfs(board, r, c-1);
    }
}
```

---

## BFS vs DFS Decision Guide

| Use BFS when... | Use DFS when... |
|---|---|
| Shortest path (unweighted) | Cycle detection |
| Level-order traversal | Topological sort |
| Multi-source spreading | Connected components |
| Finding nearest neighbor | Finding all paths |

#sde-sheet #graphs #bfs #dfs #day22
