---
solved: false
difficulty: Easy
pattern: Matrix Traversal
lc_number: 733
date_solved: 
tags:
  - dsa
  - matrix-traversal
  - easy
---
# Flood Fill (LC 733)

**Difficulty**: Easy  
**Pattern**: Matrix Traversal / BFS / DFS  
**LeetCode**: https://leetcode.com/problems/flood-fill/

## Problem Statement
An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image.

You are also given three integers `sr`, `sc`, and `color`. You should perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.

**Example:**
```
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
```

## Approach 1: DFS (Recursive)

### Intuition
Start at the source pixel. Change its color. Recursively visit 4-directionally connected pixels if they have the same original color.

### Java Code
```java
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int originalColor = image[sr][sc];
        if (originalColor != color) {
            dfs(image, sr, sc, originalColor, color);
        }
        return image;
    }
    
    private void dfs(int[][] image, int r, int c, int originalColor, int newColor) {
        if (r < 0 || r >= image.length || c < 0 || c >= image[0].length || image[r][c] != originalColor) {
            return;
        }
        
        image[r][c] = newColor;
        
        dfs(image, r+1, c, originalColor, newColor);
        dfs(image, r-1, c, originalColor, newColor);
        dfs(image, r, c+1, originalColor, newColor);
        dfs(image, r, c-1, originalColor, newColor);
    }
}
```

### Complexity
- **Time**: O(m × n)
- **Space**: O(m × n) - Stack

## Approach 2: BFS (Iterative)

### Java Code
```java
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int originalColor = image[sr][sc];
        if (originalColor == color) return image;
        
        int m = image.length;
        int n = image[0].length;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{sr, sc});
        image[sr][sc] = color;
        
        int[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];
            
            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && image[nr][nc] == originalColor) {
                    image[nr][nc] = color;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
        
        return image;
    }
}
```

## Key Takeaways
- Basic graph traversal (DFS/BFS) on grid
- Check `originalColor != color` to avoid infinite loop
- Change color in-place to mark visited
