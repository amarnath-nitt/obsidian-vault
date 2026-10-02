# Count and Say

**LeetCode 38** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/count-and-say/)

### Problem
RLE sequence: 1 → "1", 11 → "21", 21 → "1211", ...

### Approach

- Start from "1", build each level by counting consecutive chars

### Java Solution

```java
class Solution {
    public String countAndSay(int n) {
        String result = "1";
        for (int i = 1; i < n; i++) {
            StringBuilder next = new StringBuilder();
            int j = 0;
            while (j < result.length()) {
                char c = result.charAt(j);
                int count = 0;
                while (j < result.length() && result.charAt(j) == c) {
                    j++; count++;
                }
                next.append(count).append(c);
            }
            result = next.toString();
        }
        return result;
    }
}
```

**Complexity:** Time O(n × max_length) · Space O(max_length)

---
