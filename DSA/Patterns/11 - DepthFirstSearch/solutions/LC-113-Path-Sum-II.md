---
solved: false
difficulty: Medium
pattern: Depth First Search
lc_number: 113
date_solved: 
tags:
  - dsa
  - depth-first-search
  - medium
---
# Path Sum II

[Problem Link](https://leetcode.com/problems/path-sum-ii/)

## Problem Statement
Given the `root` of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of the node values in the path equals `targetSum`. Each path should be returned as a list of the node values, not node references.

## Approach
DFS with backtracking.
1.  Traverse the tree.
2.  Add current node value to `currentPath` and subtract from `targetSum`.
3.  If leaf node and `targetSum == 0`, add `currentPath` copy to results.
4.  Recurse left and right.
5.  Backtrack: remove last element from `currentPath`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```java
class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> currentPath = new ArrayList<>();
        dfs(root, targetSum, currentPath, result);
        return result;
    }
    
    private void dfs(TreeNode node, int target, List<Integer> currentPath, List<List<Integer>> result) {
        if (node == null) return;
        
        currentPath.add(node.val);
        
        if (node.left == null && node.right == null && node.val == target) {
            result.add(new ArrayList<>(currentPath));
        } else {
            dfs(node.left, target - node.val, currentPath, result);
            dfs(node.right, target - node.val, currentPath, result);
        }
        
        // Backtrack
        currentPath.remove(currentPath.size() - 1);
    }
}
```
