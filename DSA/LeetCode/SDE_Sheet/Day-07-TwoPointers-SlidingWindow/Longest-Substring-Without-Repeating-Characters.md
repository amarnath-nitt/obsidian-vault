# Longest Substring Without Repeating Characters

**LeetCode 3** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

### Problem
Find the length of the longest substring without repeating characters.

### Approach (Sliding Window + HashMap)

- Track last seen index of each character
- When duplicate found, move `left` to `max(left, lastSeen[char] + 1)`

### Java Solution

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> lastSeen = new HashMap<>();
        int maxLen = 0, left = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (lastSeen.containsKey(c) && lastSeen.get(c) >= left) {
                left = lastSeen.get(c) + 1;
            }
            lastSeen.put(c, right);
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

**Complexity:** Time O(n) · Space O(min(n, alphabet))

---
