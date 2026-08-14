# Alien Dictionary

**Difficulty:** Hard (Premium)  
**Category:** Graphs  
**LeetCode Link:** [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

---

## Problem Statement

There is a new alien language that uses the English alphabet. However, the order among letters is unknown to you.

You are given a list of strings `words` from the dictionary, where `words` are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return `""`. If there are multiple solutions, return any of them.

**Example:**
```
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

**Constraints:**
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of only lowercase English letters.

---

## Intuition

This is a topological sort problem. Compare adjacent words to find character ordering, build a directed graph, then perform topological sort.

---

## Approach: Topological Sort (Kahn's Algorithm)

### Algorithm
1. Build graph by comparing adjacent words
2. Find first differing character → add edge
3. Calculate in-degrees
4. Perform topological sort using BFS
5. If result length < unique chars, there's a cycle

### Java Code
```java
class Solution {
    public String alienOrder(String[] words) {
        Map<Character, Set<Character>> graph = new HashMap<>();
        Map<Character, Integer> inDegree = new HashMap<>();
        
        // Initialize graph
        for (String word : words) {
            for (char c : word.toCharArray()) {
                graph.putIfAbsent(c, new HashSet<>());
                inDegree.putIfAbsent(c, 0);
            }
        }
        
        // Build graph
        for (int i = 0; i < words.length - 1; i++) {
            String word1 = words[i];
            String word2 = words[i + 1];
            
            // Check for invalid case
            if (word1.length() > word2.length() && word1.startsWith(word2)) {
                return "";
            }
            
            // Find first different character
            for (int j = 0; j < Math.min(word1.length(), word2.length()); j++) {
                char c1 = word1.charAt(j);
                char c2 = word2.charAt(j);
                if (c1 != c2) {
                    if (!graph.get(c1).contains(c2)) {
                        graph.get(c1).add(c2);
                        inDegree.put(c2, inDegree.get(c2) + 1);
                    }
                    break;
                }
            }
        }
        
        // Topological sort
        Queue<Character> queue = new LinkedList<>();
        for (char c : inDegree.keySet()) {
            if (inDegree.get(c) == 0) {
                queue.offer(c);
            }
        }
        
        StringBuilder result = new StringBuilder();
        while (!queue.isEmpty()) {
            char c = queue.poll();
            result.append(c);
            
            for (char next : graph.get(c)) {
                inDegree.put(next, inDegree.get(next) - 1);
                if (inDegree.get(next) == 0) {
                    queue.offer(next);
                }
            }
        }
        
        return result.length() == inDegree.size() ? result.toString() : "";
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(C) where C = total characters in all words
- **Space Complexity:** O(1) - At most 26 characters

---

## Tags
#graphs #topological-sort #bfs #hard #blind75
