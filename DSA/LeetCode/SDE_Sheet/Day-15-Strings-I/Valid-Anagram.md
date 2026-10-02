# Valid Anagram

**LeetCode 242** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/valid-anagram/)

### Approach

- Use frequency array of size 26
- Increment for `s`, decrement for `t`
- Check all zeros

### Java Solution

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
            freq[t.charAt(i) - 'a']--;
        }
        for (int f : freq) if (f != 0) return false;
        return true;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
