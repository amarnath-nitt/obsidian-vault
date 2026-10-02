# Minimum Window Substring

**LeetCode 76** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/minimum-window-substring/)

### Problem
Find the minimum window in `s` that contains all characters of `t`.

### Approach (Sliding Window + Frequency Map)

1. Count all characters in `t` → `need` map
2. Expand `right` until window contains all required chars
3. Once valid, shrink `left` to minimize
4. Track minimum window

### Java Solution

```java
class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> need = new HashMap<>();
        for (char c : t.toCharArray()) need.merge(c, 1, Integer::sum);

        int left = 0, matched = 0, minLen = Integer.MAX_VALUE, minStart = 0;
        Map<Character, Integer> window = new HashMap<>();

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            window.merge(c, 1, Integer::sum);
            if (need.containsKey(c) && window.get(c).equals(need.get(c))) matched++;

            while (matched == need.size()) {
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minStart = left;
                }
                char lc = s.charAt(left);
                window.merge(lc, -1, Integer::sum);
                if (need.containsKey(lc) && window.get(lc) < need.get(lc)) matched--;
                left++;
            }
        }
        return minLen == Integer.MAX_VALUE ? "" : s.substring(minStart, minStart + minLen);
    }
}
```

**Complexity:** Time O(|s| + |t|) · Space O(|t|)

---
