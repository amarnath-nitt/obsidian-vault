# Longest Palindrome (LC 409)

**Difficulty**: Easy  
**Pattern**: Greedy  
**LeetCode**: https://leetcode.com/problems/longest-palindrome/

## Problem Statement
Given a string `s` which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

**Example:**
```
Input: s = "abccccdd"
Output: 7
Explanation: "dccaccd"
```

## Approach: Pair Counting

### Intuition
For palindrome, we need pairs.
Count char frequencies.
Add `count / 2 * 2` to answer.
If we have any odd count left, we can put one character in the middle.

### Java Code
```java
class Solution {
    public int longestPalindrome(String s) {
        int[] count = new int[128];
        for (char c : s.toCharArray()) count[c]++;
        
        int length = 0;
        boolean hasOdd = false;
        
        for (int c : count) {
            length += (c / 2) * 2;
            if (c % 2 == 1) hasOdd = true;
        }
        
        return hasOdd ? length + 1 : length;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- Simple greedy collection of pairs
