# First Unique Character in a String (LC 387)

**Difficulty**: Easy  
**Pattern**: Frequency Counting  
**LeetCode**: https://leetcode.com/problems/first-unique-character-in-a-string/

## Problem Statement
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

**Example:**
```
Input: s = "leetcode"
Output: 0
```

## Approach: Frequency Array / Map

### Intuition
1. Count frequency of all characters.
2. Iterate string again. Return first char with count 1.
Using array `int[26]` is faster than HashMap for lowercase English letters.

### Java Code
```java
class Solution {
    public int firstUniqChar(String s) {
        int[] freq = new int[26];
        
        // Count frequencies
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }
        
        // Find first unique
        for (int i = 0; i < s.length(); i++) {
            if (freq[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }
        
        return -1;
    }
}
```

### Complexity
- **Time**: O(N) (Two passes)
- **Space**: O(1) (26 chars)

## Key Takeaways
- Two-pass strategy: Count then Verify
- Array `int[26]` optimal for char counts
