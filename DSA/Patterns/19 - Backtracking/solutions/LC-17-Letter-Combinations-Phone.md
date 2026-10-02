---
solved: false
difficulty: Medium
pattern: Backtracking
lc_number: 17
date_solved: 
tags:
  - dsa
  - backtracking
  - medium
---
# Letter Combinations of a Phone Number (LC 17)

**Difficulty**: Medium  
**Pattern**: Backtracking  
**LeetCode**: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## Problem Statement
Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
Mapping is standard telephone buttons (2=abc, 3=def...).

**Example:**
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

## Approach: Backtracking

### Intuition
For each digit, iterate through its corresponding letters.
Recursively proceed to the next digit.
Base case: if path length == digits length, add to result.

### Java Code
```java
class Solution {
    private static final String[] KEYS = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };
    
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;
        
        backtrack(digits, 0, new StringBuilder(), result);
        return result;
    }
    
    private void backtrack(String digits, int index, StringBuilder current, List<String> result) {
        if (index == digits.length()) {
            result.add(current.toString());
            return;
        }
        
        int digit = digits.charAt(index) - '0';
        String letters = KEYS[digit];
        
        for (char c : letters.toCharArray()) {
            current.append(c);
            backtrack(digits, index + 1, current, result);
            current.deleteCharAt(current.length() - 1); // Backtrack
        }
    }
}
```

### Complexity
- **Time**: O(4^N * N), where N is number of digits. 4 is max letters per digit.
- **Space**: O(N) stack depth

## Key Takeaways
- Classic Backtracking template
- Use StringBuilder for efficiency
