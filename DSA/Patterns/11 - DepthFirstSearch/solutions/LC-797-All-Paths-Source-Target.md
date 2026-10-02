---
solved: false
difficulty: Medium
pattern: Depth First Search
lc_number: 797
date_solved: 
tags:
  - dsa
  - depth-first-search
  - medium
---
# All Paths From Source to Target

[Problem Link](https://leetcode.com/problems/all-paths-from-source-to-target/)

## Problem Statement
Given a directed acyclic graph (DAG) of `n` nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1` and return them in any order.
The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node `i` (i.e., there is a directed edge from node `i` to node `graph[i][j]`).

## Approach
DFS Backtracking.
1.  Start at node 0.
2.  Add node to current path.
3.  If node is `n-1`, add path to results.
4.  Directly iterate through neighbors and recurse.
5.  Backtrack: remove node from path.

## Time and Space Complexity
- **Time Complexity:** O(2^N * N). (Number of paths can be exponential).
- **Space Complexity:** O(N) stack space.

## Code
```java
class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        path.add(0);
        dfs(graph, 0, path, result);
        return result;
    }
    
    private void dfs(int[][] graph, int node, List<Integer> path, List<List<Integer>> result) {
        if (node == graph.length - 1) {
            result.add(new ArrayList<>(path));
            return;
        }
        
        for (int neighbor : graph[node]) {
            path.add(neighbor);
            dfs(graph, neighbor, path, result);
            path.remove(path.size() - 1);
        }
    }
}
```
