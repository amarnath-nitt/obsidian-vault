---
solved: false
difficulty: Hard
pattern: Matrix Traversal
lc_number: 305
date_solved: 
tags:
  - dsa
  - matrix-traversal
  - hard
---
# Number of Islands II

[Problem Link](https://leetcode.com/problems/number-of-islands-ii/)

## Problem Statement
You are given an empty 2D binary grid `grid` of size `m x n`. The grid represents a map where `0`'s represent water and `1`'s represent land. Initially, all the cells of `grid` are water cells (i.e., all the cells are `0`'s).
We may perform an add land operation which turns the water at position `(row, col)` into a land. You are given an array `positions` where `positions[i] = [ri, ci]` is the position `(ri, ci)` at which we should operate the `i`th operation.
Return an array of integers `answer` where `answer[i]` is the number of islands after turning the cell `(ri, ci)` into a land.

## Approach
Union-Find (Disjoint Set).
1.  Treat grid as 1D array of size `m * n`.
2.  Maintain `count` of islands.
3.  For each operation:
    - If already land, continue.
    - Set as land, `count++`.
    - Check 4 neighbors. If neighbor is land, `union(current, neighbor)`.
    - If union successful, `count--`.
    - Add `count` to result.

## Time and Space Complexity
- **Time Complexity:** O(K * alpha(M*N)), where K is number of operations.
- **Space Complexity:** O(M * N).

## Code
```java
class Solution {
    class UnionFind {
        int[] parent;
        int[] rank;
        int count;
        
        public UnionFind(int n) {
            parent = new int[n];
            rank = new int[n];
            Arrays.fill(parent, -1); // -1 indicates water
            count = 0;
        }
        
        public void setLand(int i) {
            if (parent[i] == -1) {
                parent[i] = i;
                count++;
            }
        }
        
        public boolean isLand(int i) {
            return parent[i] != -1;
        }
        
        public int find(int i) {
            if (parent[i] != i) parent[i] = find(parent[i]);
            return parent[i];
        }
        
        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) {
                if (rank[rootX] > rank[rootY]) {
                    parent[rootY] = rootX;
                } else if (rank[rootX] < rank[rootY]) {
                    parent[rootX] = rootY;
                } else {
                    parent[rootY] = rootX;
                    rank[rootX]++;
                }
                count--;
            }
        }
        
        public int getCount() {
            return count;
        }
    }
    
    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        List<Integer> result = new ArrayList<>();
        UnionFind uf = new UnionFind(m * n);
        int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        for (int[] pos : positions) {
            int r = pos[0];
            int c = pos[1];
            int idx = r * n + c;
            
            if (uf.isLand(idx)) {
                result.add(uf.getCount());
                continue;
            }
            
            uf.setLand(idx);
            
            for (int[] d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];
                int nidx = nr * n + nc;
                
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && uf.isLand(nidx)) {
                    uf.union(idx, nidx);
                }
            }
            result.add(uf.getCount());
        }
        return result;
    }
}
```
