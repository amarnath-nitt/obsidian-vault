# Word Ladder II

[Problem Link](https://leetcode.com/problems/word-ladder-ii/)

## Problem Statement
A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:
- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`.
Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *all the shortest transformation sequences* from `beginWord` to `endWord`, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words `[beginWord, s1, s2, ..., sk]`.

## Approach
1.  **BFS**: Use Breadth-First Search to find the shortest distance from `beginWord` to every other word. Also, build a graph (adjacency list) where edges go from a word to its neighbors that are one step closer to the `beginWord`. This is effectively building the parents map for backtracking.
    - Store `minDistance` for each word.
    - If, during BFS, we reach a word that has already been visited at the *same* distance, it means there's another shortest path to it; add the parent.
2.  **DFS (Backtracking)**: Once the graph/parents map is built, use DFS starting from `endWord` to trace back to `beginWord` using the parents map to reconstruct all paths.

## Time and Space Complexity
- **Time Complexity:** O(N * L^2 + P), where N is number of words, L is word length, P is number of paths.
- **Space Complexity:** O(N * L) for storing the graph/parents.

## Code
```java
class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        List<List<String>> result = new ArrayList<>();
        if (!wordSet.contains(endWord)) return result;
        
        // BFS to build graph/parents
        // Map<Word, List<Parents>>
        Map<String, List<String>> parents = new HashMap<>();
        Map<String, Integer> distance = new HashMap<>();
        
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        distance.put(beginWord, 0);
        
        boolean found = false;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            Set<String> currentLevelVisited = new HashSet<>();
            
            for (int i = 0; i < size; i++) {
                String curr = queue.poll();
                if (curr.equals(endWord)) found = true;
                
                // Try changing each char
                char[] chars = curr.toCharArray();
                for (int j = 0; j < chars.length; j++) {
                    char original = chars[j];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == original) continue;
                        chars[j] = c;
                        String next = new String(chars);
                        
                        if (wordSet.contains(next)) {
                            if (!distance.containsKey(next)) {
                                // First time seeing 'next'
                                distance.put(next, distance.get(curr) + 1);
                                queue.offer(next);
                                parents.computeIfAbsent(next, k -> new ArrayList<>()).add(curr);
                            } else if (distance.get(next) == distance.get(curr) + 1) {
                                // Another shortest path to 'next'
                                parents.computeIfAbsent(next, k -> new ArrayList<>()).add(curr);
                            }
                        }
                    }
                    chars[j] = original;
                }
            }
            if (found) break; // Found shortest path, stop BFS
        }
        
        // DFS to reconstruct paths
        if (found) {
            List<String> path = new ArrayList<>();
            path.add(endWord);
            dfs(endWord, beginWord, parents, path, result);
        }
        
        return result;
    }
    
    private void dfs(String curr, String target, Map<String, List<String>> parents, List<String> path, List<List<String>> result) {
        if (curr.equals(target)) {
            List<String> validPath = new ArrayList<>(path);
            Collections.reverse(validPath);
            result.add(validPath);
            return;
        }
        
        if (!parents.containsKey(curr)) return;
        
        for (String parent : parents.get(curr)) {
            path.add(parent);
            dfs(parent, target, parents, path, result);
            path.remove(path.size() - 1);
        }
    }
}
```
