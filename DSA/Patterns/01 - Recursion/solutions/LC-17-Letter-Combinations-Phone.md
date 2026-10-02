---
solved: true
difficulty: Medium
pattern: Recursion
lc_number: 17
date_solved: 
tags:
  - dsa
  - recursion
  - medium
---
# Letter Combinations of a Phone Number (LC 17)

**Difficulty**: Medium  
**Pattern**: Recursion / Backtracking  
**LeetCode**: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## Problem Statement
Given digits from `2` to `9`, return all possible letter combinations they could represent on a phone keypad.

## Recursive Idea
At index `i`, choose one letter mapped from `digits.charAt(i)`, then recurse to index `i + 1`.

## Intuition: Combinatorial Generation

### The Key Insight
Each digit (2-9) maps to multiple letters:
```
2 → "abc" (3 letters)
3 → "def" (3 letters)
4 → "ghi" (3 letters)
5 → "jkl" (3 letters)
6 → "mno" (3 letters)
7 → "pqrs" (4 letters)
8 → "tuv" (3 letters)
9 → "wxyz" (4 letters)
```

We need **ALL combinations**: for each digit, pick one letter.

### Combinatorial Counting
For digits="234":
- Digit 2 has 3 choices
- Digit 3 has 3 choices
- Digit 4 has 3 choices
- Total combinations: 3 × 3 × 3 = **27 combinations**

Time complexity: O(4^n × n) where 4 is the max letters per digit.

### The Backtracking Approach
At each digit:
1. Get the letters it can map to
2. For each letter, add it to the current combination
3. Move to the next digit (recursively)
4. After exploring, remove the letter (backtrack)

### Visual Flow: digits="23"

```
Start at digit '2' (maps to "abc"):
├─ Choose 'a':
│  └─ Move to digit '3' (maps to "def"):
│     ├─ Choose 'd': Save "ad" ✓
│     ├─ Choose 'e': Save "ae" ✓
│     └─ Choose 'f': Save "af" ✓
├─ Choose 'b':
│  └─ Move to digit '3':
│     ├─ Choose 'd': Save "bd" ✓
│     ├─ Choose 'e': Save "be" ✓
│     └─ Choose 'f': Save "bf" ✓
└─ Choose 'c':
   └─ Move to digit '3':
      ├─ Choose 'd': Save "cd" ✓
      ├─ Choose 'e': Save "ce" ✓
      └─ Choose 'f': Save "cf" ✓

Result: 9 combinations = 3 × 3
```

### Iterative Alternative
Instead of recursion, build combinations level by level:
```
Start: [""]
Process '2' (letters "abc"):
  Expand: "" → "a", "b", "c"
Process '3' (letters "def"):
  Expand: "a" → "ad", "ae", "af"
           "b" → "bd", "be", "bf"
           "c" → "cd", "ce", "cf"
Result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```
The iterative BFS approach eliminates recursion stack overhead.

## Java Code
```java
class Solution {
    private static final String[] MAP = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) {
            return result;
        }
        backtrack(digits, 0, new StringBuilder(), result);
        return result;
    }

    private void backtrack(String digits, int index, StringBuilder path, List<String> result) {
        if (index == digits.length()) {
            result.add(path.toString());
            return;
        }

        String letters = MAP[digits.charAt(index) - '0'];
        for (char ch : letters.toCharArray()) {
            path.append(ch);
            backtrack(digits, index + 1, path, result);
            path.deleteCharAt(path.length() - 1);
        }
    }
}
```

## Alternative Optimal Solution: Iterative BFS
Build combinations level by level. Each digit expands the current list of prefixes.

```java
class Solution {
    private static final String[] MAP = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) {
            return result;
        }

        result.add("");
        for (char digit : digits.toCharArray()) {
            List<String> next = new ArrayList<>();
            for (String prefix : result) {
                for (char ch : MAP[digit - '0'].toCharArray()) {
                    next.add(prefix + ch);
                }
            }
            result = next;
        }
        return result;
    }
}
```

### Alternative Complexity
- **Time**: O(4^n * n)
- **Space**: O(4^n * n) for the output

## Complexity
- **Time**: O(4^n * n)
- **Space**: O(n) excluding output

## Key Takeaways
- One recursive level represents one digit.
- Backtracking removes the last choice before trying the next one.
