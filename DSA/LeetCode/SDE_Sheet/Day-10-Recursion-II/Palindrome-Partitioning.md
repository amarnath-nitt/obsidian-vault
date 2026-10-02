# Palindrome Partitioning

**LeetCode 131** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/palindrome-partitioning/)

### Problem
Partition string `s` such that every substring of the partition is a palindrome.

### Approach (Backtracking)

- Try each prefix: if it's a palindrome, recurse on the suffix
- Add to result when entire string is consumed

### Java Solution

```java
class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(String s, int start, List<String> current, List<List<String>> result) {
        if (start == s.length()) {
            result.add(new ArrayList<>(current)); return;
        }
        for (int end = start + 1; end <= s.length(); end++) {
            String sub = s.substring(start, end);
            if (isPalindrome(sub)) {
                current.add(sub);
                backtrack(s, end, current, result);
                current.remove(current.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) if (s.charAt(l++) != s.charAt(r--)) return false;
        return true;
    }
}
```

---
