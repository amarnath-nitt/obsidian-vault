# Valid Anagram

**Difficulty:** Easy  
**Category:** Arrays & Hashing  
**LeetCode Link:** [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

---

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**
```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:**
```
Input: s = "rat", t = "car"
Output: false
```

**Constraints:**
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

---

## Intuition

Two strings are anagrams if they contain the exact same characters with the same frequencies. We need to verify that both strings have identical character counts.

---

## Approach 1: Sorting (Naive Solution)

### Algorithm
1. If lengths differ, they can't be anagrams
2. Sort both strings
3. Compare sorted strings for equality

### Java Code
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        // Different lengths can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Convert to char arrays and sort
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        
        Arrays.sort(sChars);
        Arrays.sort(tChars);
        
        // Compare sorted arrays
        return Arrays.equals(sChars, tChars);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n log n) - Dominated by sorting
- **Space Complexity:** O(n) - Char arrays for both strings

### Drawbacks
- Sorting is overkill for this problem
- Not optimal time complexity

---

## Approach 2: Hash Map (Optimized Solution)

### Algorithm
1. If lengths differ, return false
2. Use a HashMap to count character frequencies in first string
3. Decrement counts for characters in second string
4. If any count becomes negative or doesn't exist, return false
5. If all counts reach zero, strings are anagrams

### Java Code
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        // Different lengths can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Count character frequencies
        Map<Character, Integer> charCount = new HashMap<>();
        
        // Add counts from s
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        
        // Subtract counts from t
        for (char c : t.toCharArray()) {
            if (!charCount.containsKey(c)) {
                return false;
            }
            charCount.put(c, charCount.get(c) - 1);
            if (charCount.get(c) < 0) {
                return false;
            }
        }
        
        return true;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Two passes through strings
- **Space Complexity:** O(1) - At most 26 lowercase letters

---

## Approach 3: Frequency Array (Most Optimized)

### Algorithm
1. Since we only have lowercase letters (26 characters), use an array
2. Increment count for each character in `s`
3. Decrement count for each character in `t`
4. Check if all counts are zero

### Java Code
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        // Different lengths can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Frequency array for 26 lowercase letters
        int[] count = new int[26];
        
        // Count characters in both strings
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        
        // Check if all counts are zero
        for (int c : count) {
            if (c != 0) {
                return false;
            }
        }
        
        return true;
    }
}
```

### Alternative Single-Pass Version
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] count = new int[26];
        
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        
        for (int c : count) {
            if (c != 0) return false;
        }
        
        return true;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Linear pass through strings
- **Space Complexity:** O(1) - Fixed size array of 26

### Why This is Better
- ✅ Linear time complexity
- ✅ Constant space (26 is fixed)
- ✅ Faster than HashMap (array access vs hash function)
- ✅ Simple and clean

---

## Key Takeaways

1. **Pattern:** Character frequency counting is common for string problems
2. **Optimization:** When character set is limited, use array instead of HashMap
3. **Array indexing:** `char - 'a'` gives index 0-25 for lowercase letters
4. **Early exit:** Check length first to avoid unnecessary work

---

## Follow-up

**Q: What if the inputs contain Unicode characters?**  
**A:** Use HashMap instead of array since Unicode has many more characters.

```java
// Unicode-safe version
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) return false;
    
    Map<Character, Integer> map = new HashMap<>();
    for (char c : s.toCharArray()) {
        map.put(c, map.getOrDefault(c, 0) + 1);
    }
    
    for (char c : t.toCharArray()) {
        if (!map.containsKey(c) || map.get(c) == 0) return false;
        map.put(c, map.get(c) - 1);
    }
    
    return true;
}
```

---

## Related Problems
- [[Group-Anagrams]] - Group strings that are anagrams
- [[Find-All-Anagrams]] - Find anagram substrings
- [[Permutation-in-String]] - Similar frequency matching

---

## Tags
#strings #hashing #sorting #frequency-count #easy #blind75
