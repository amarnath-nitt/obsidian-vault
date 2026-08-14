# Word Ladder

**Difficulty:** Hard  
**Category:** Graphs  
**LeetCode Link:** [Word Ladder](https://leetcode.com/problems/word-ladder/)

---

## Problem Statement

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words where:
- The first word is `beginWord`
- The last word is `endWord`
- Each adjacent pair differs by exactly one letter
- Every word in the sequence is in `wordList`

Return the **length** of the shortest transformation sequence, or `0` if no such sequence exists.

**Example:**
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog"
```

**Constraints:**
- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 5000`
- All words have the same length and contain only lowercase letters.

---

## Intuition

This is a shortest path problem in an unweighted graph. Use BFS to find the shortest transformation sequence.

---

## Approach: BFS

### Algorithm
1. Use BFS starting from beginWord
2. For each word, try changing each character
3. If transformed word is in wordList, add to queue
4. Track visited words to avoid cycles
5. Return level when endWord is found

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
                String word = queue.poll();
                char[] chars = word.toCharArray();
                
                // Try changing each character
                for (int j = 0; j < chars.length; j++) {
                    char original = chars[j];
                    
                    // Try all 26 letters
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == original) continue;
                        
                        chars[j] = c;
                        String newWord = new String(chars);
                        
                        if (newWord.equals(endWord)) {
                            return level + 1;
                        }
                        
                        if (wordSet.contains(newWord)) {
                            queue.offer(newWord);
                            wordSet.remove(newWord);  // Mark as visited
                        }
                    }
                    
                    chars[j] = original;  // Restore
                }
            }
            
            level++;
        }
        
        return 0;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(M² × N) where M = word length, N = wordList size
- **Space Complexity:** O(N) - Queue and set

---

## Tags
#graphs #bfs #shortest-path #hard #blind75
