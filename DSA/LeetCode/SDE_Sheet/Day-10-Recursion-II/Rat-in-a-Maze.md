# Rat in a Maze

**Problem:** Rat starts at (0,0), find all paths to (n-1,n-1). Can move in all 4 directions.

### Approach

- DFS/backtracking: try all 4 directions
- Mark cell as visited while exploring, unmark when backtracking

### Java Solution

```java
public class RatMaze {
    static List<String> findPath(int[][] maze, int n) {
        List<String> paths = new ArrayList<>();
        boolean[][] visited = new boolean[n][n];
        if (maze[0][0] == 1) dfs(maze, visited, 0, 0, n, "", paths);
        return paths;
    }

    static int[] dr = {1, 0, 0, -1};
    static int[] dc = {0, -1, 1, 0};
    static char[] dir = {'D', 'L', 'R', 'U'};

    static void dfs(int[][] maze, boolean[][] visited,
                    int r, int c, int n, String path, List<String> paths) {
        if (r == n-1 && c == n-1) { paths.add(path); return; }

        visited[r][c] = true;
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n
                    && maze[nr][nc] == 1 && !visited[nr][nc]) {
                dfs(maze, visited, nr, nc, n, path + dir[d], paths);
            }
        }
        visited[r][c] = false; // backtrack
    }
}
```

---
