# Valid Anagram (LC 242)

**Difficulty**: Easy  
**Pattern**: Frequency Counting  
**LeetCode**: https://leetcode.com/problems/valid-anagram/

## Existing Solution
This problem is solved in Blind75: → [Solution](../../../LeetCode/Blind75/Arrays-Hashing/Valid-Anagram.md)

## Problem Statement
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

**Example 1:**
```
Input: s = "anagram", t = "nagaram"
Output: true
```

## Approach 1: Sorting

### Java Code
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        
        Arrays.sort(sArr);
        Arrays.sort(tArr);
        
        return Arrays.equals(sArr, tArr);
    }
}
```

### Complexity
- **Time**: O(n log n)
- **Space**: O(1)

## Approach 2: Frequency Counting (Optimized)

### Java Code
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] count = new int[26];
        
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        
        for (int c : count) {
            if (c != 0) return false;
        }
        
        return true;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(1)

## Key Takeaways
- Frequency array optimal for lowercase English letters
- Can use HashMap for Unicode characters
- Sorting works but slower than frequency counting
