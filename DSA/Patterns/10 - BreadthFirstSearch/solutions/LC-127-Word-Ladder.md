# Word Ladder (LC 127)

**Difficulty**: Hard  
**Pattern**: Breadth-First Search  
**LeetCode**: https://leetcode.com/problems/word-ladder/

## Problem Statement
A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:
- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`.
Return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or 0 if no such sequence exists.

**Example:**
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
```

## Approach: BFS

### Intuition
Model this as a shortest path problem in an unweighted graph.
Nodes are words. Edges connect words differing by one letter.
BFS yields the shortest path.
Optimization: To find neighbors, instead of iterating over `wordList` (O(N*L)), iterate over current word's chars and try all 26 replacements (O(L*26)). Check if in `wordSet`.

### Java Code
```java
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        if (!wordSet.contains(endWord)) return 0;
        
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        
        int level = 1;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String curr = queue.poll();
                if (curr.equals(endWord)) return level;
                
                char[] chars = curr.toCharArray();
                for (int j = 0; j < chars.length; j++) {
                    char original = chars[j];
                    
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == original) continue;
                        chars[j] = c;
                        String next = new String(chars);
                        
                        if (wordSet.contains(next)) {
                            queue.offer(next);
                            wordSet.remove(next); // Mark as visited
                        }
                    }
                    chars[j] = original; // Restore
                }
            }
            level++;
        }
        
        return 0;
    }
}
```

### Complexity
- **Time**: O(M^2 * N), where M is length of word, N is number of words.
- **Space**: O(M * N) used by queue and set

## Key Takeaways
- BFS for shortest path in unweighted graph (state transitions)
- Optimize neighbor finding by transforming characters instead of comparing against list
