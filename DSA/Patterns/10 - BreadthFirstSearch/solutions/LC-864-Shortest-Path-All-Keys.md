---
solved: false
difficulty: Hard
pattern: Breadth First Search
lc_number: 864
date_solved: 
tags:
  - dsa
  - breadth-first-search
  - hard
---
# Shortest Path to Get All Keys

[Problem Link](https://leetcode.com/problems/shortest-path-to-get-all-keys/)

## Problem Statement
You are given an `m x n` grid `grid` where:
- `'.'` is an empty cell.
- `'#'` is a wall.
- `'@'` is the starting point.
- Lowercase letters represent keys.
- Uppercase letters represent locks.

You start at the starting point and want to collect all keys. You cannot walk through walls. You cannot walk through a lock unless you have the corresponding key.
Return the path of the shortest path to all keys. If it is impossible, return `-1`.

## Approach
BFS. The state in BFS needs to include `(x, y, keys_collected)`.
`keys_collected` can be represented by a bitmask since there are at most 6 keys (a-f).
1.  Find start position and total number of keys.
2.  BFS Queue stores `int[] {x, y, bitmask}`.
3.  `visited[x][y][bitmask]` keeps track of visited states.
4.  Explore 4 directions.
    - If next cell is wall, skip.
    - If next cell is lock (A-F), check if we have key (bitmask & (1 << (char - 'A'))).
    - If next cell is key (a-f), update bitmask (bitmask | (1 << (char - 'a'))).
    - If next cell is empty or start, just move.
5.  If bitmask has all bits set (all keys collected), return steps.

## Time and Space Complexity
- **Time Complexity:** O(M * N * 2^K), where K is number of keys (max 6). 2^K states for each cell.
- **Space Complexity:** O(M * N * 2^K) for visited array.

## Code
```java
class Solution {
    public int shortestPathAllKeys(String[] grid) {
        int m = grid.length;
        int n = grid[0].length();
        int allKeys = 0;
        int startX = -1, startY = -1;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = grid[i].charAt(j);
                if (c == '@') {
                    startX = i;
                    startY = j;
                } else if (c >= 'a' && c <= 'f') {
                    allKeys |= (1 << (c - 'a'));
                }
            }
        }
        
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{startX, startY, 0});
        boolean[][][] visited = new boolean[m][n][1 << 6];
        visited[startX][startY][0] = true;
        
        int steps = 0;
        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int k = 0; k < size; k++) {
                int[] curr = queue.poll();
                int x = curr[0];
                int y = curr[1];
                int mask = curr[2];
                
                if (mask == allKeys) return steps;
                
                for (int[] d : dirs) {
                    int nx = x + d[0];
                    int ny = y + d[1];
                    
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                        char c = grid[nx].charAt(ny);
                        
                        if (c == '#') continue;
                        
                        int newMask = mask;
                        
                        if (c >= 'a' && c <= 'f') { // Key
                            newMask |= (1 << (c - 'a'));
                        } else if (c >= 'A' && c <= 'F') { // Lock
                            if ((mask >> (c - 'A') & 1) == 0) {
                                continue; // No key for this lock
                            }
                        }
                        
                        if (!visited[nx][ny][newMask]) {
                            visited[nx][ny][newMask] = true;
                            queue.offer(new int[]{nx, ny, newMask});
                        }
                    }
                }
            }
            steps++;
        }
        
        return -1;
    }
}
```
