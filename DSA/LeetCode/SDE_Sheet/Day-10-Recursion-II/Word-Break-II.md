# Word Break II

**LeetCode 140** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/word-break-ii/)

### Problem
Return all possible sentences by inserting spaces into `s` using words from `wordDict`.

### Approach (Backtracking + Memoization)

- Try all prefixes of remaining string
- If prefix is in dictionary, recurse on suffix
- Memoize: `string → list of sentences` to avoid recomputation

### Java Solution

```java
class Solution {
    Map<String, List<String>> memo = new HashMap<>();

    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        return backtrack(s, dict);
    }

    private List<String> backtrack(String s, Set<String> dict) {
        if (memo.containsKey(s)) return memo.get(s);
        List<String> result = new ArrayList<>();
        if (s.isEmpty()) { result.add(""); return result; }

        for (int end = 1; end <= s.length(); end++) {
            String word = s.substring(0, end);
            if (dict.contains(word)) {
                List<String> rest = backtrack(s.substring(end), dict);
                for (String sentence : rest) {
                    result.add(word + (sentence.isEmpty() ? "" : " " + sentence));
                }
            }
        }
        memo.put(s, result);
        return result;
    }
}
```

---
