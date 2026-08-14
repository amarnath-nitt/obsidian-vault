# Palindrome Partitioning (LC 131)

**Difficulty**: Medium  
**Pattern**: Backtracking  
**LeetCode**: https://leetcode.com/problems/palindrome-partitioning/

## Problem Statement
Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

**Example:**
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

## Approach: Backtracking

### Intuition
Try to cut `s` at every possible position `i`.
If `s[0...i]` is a palindrome, recurse on `s[i+1...]`.
If it's not a palindrome, prune this branch.
Base case: when start index reaches end of string, add current partition to results.

### Java Code
```java
class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), s, 0);
        return result;
    }
    
    private void backtrack(List<List<String>> result, List<String> current, String s, int start) {
        if (start == s.length()) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                current.add(s.substring(start, end + 1));
                backtrack(result, current, s, end + 1);
                current.remove(current.size() - 1);
            }
        }
    }
    
    private boolean isPalindrome(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) return false;
        }
        return true;
    }
}
```

### Complexity
- **Time**: O(N * 2^N)
- **Space**: O(N)

## Key Takeaways
- "Partitioning" is a classic backtracking pattern
- Helper `isPalindrome` checks validity of choice
