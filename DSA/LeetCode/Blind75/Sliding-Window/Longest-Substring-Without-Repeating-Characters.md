# Longest Substring Without Repeating Characters

**Difficulty:** Medium  
**Category:** Sliding Window  
**LeetCode Link:** [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with length 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with length 3.
```

**Constraints:**
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

---

## Intuition

We need to find the longest window (substring) where all characters are unique. When we encounter a duplicate, we need to shrink the window from the left.

---

## Approach 1: Brute Force (Naive Solution)

### Algorithm
1. Generate all possible substrings
2. Check each substring for duplicate characters
3. Track the maximum length

### Java Code
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                if (allUnique(s, i, j)) {
                    maxLength = Math.max(maxLength, j - i);
                }
            }
        }
        
        return maxLength;
    }
    
    private boolean allUnique(String s, int start, int end) {
        Set<Character> set = new HashSet<>();
        for (int i = start; i < end; i++) {
            if (set.contains(s.charAt(i))) {
                return false;
            }
            set.add(s.charAt(i));
        }
        return true;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n³) - O(n²) substrings × O(n) uniqueness check
- **Space Complexity:** O(min(n, m)) where m = charset size

---

## Approach 2: Sliding Window with HashSet (Optimized Solution)

### Algorithm
1. Use two pointers: `left` and `right` for the window
2. Use a HashSet to track characters in current window
3. Expand window by moving `right`
4. If duplicate found, shrink window from `left` until duplicate removed
5. Track maximum window size

### Java Code
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int maxLength = 0;
        int left = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            
            // Shrink window until no duplicate
            while (set.contains(c)) {
                set.remove(s.charAt(left));
                left++;
            }
            
            // Add current character
            set.add(c);
            
            // Update max length
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Each character visited at most twice
- **Space Complexity:** O(min(n, m)) - HashSet size

---

## Approach 3: Sliding Window with HashMap (Most Optimized)

### Algorithm
1. Use HashMap to store character → last seen index
2. When duplicate found, jump `left` directly to position after last occurrence
3. No need to remove characters one by one

### Java Code
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int maxLength = 0;
        int left = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            
            // If character seen before and in current window
            if (map.containsKey(c) && map.get(c) >= left) {
                left = map.get(c) + 1;
            }
            
            // Update last seen index
            map.put(c, right);
            
            // Update max length
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}
```

### Step-by-Step Example
For `s = "abcabcbb"`:

```
right=0, c='a': map={a:0}, left=0, len=1
right=1, c='b': map={a:0,b:1}, left=0, len=2
right=2, c='c': map={a:0,b:1,c:2}, left=0, len=3
right=3, c='a': 'a' at 0 >= left(0), left=1, map={a:3,b:1,c:2}, len=3
right=4, c='b': 'b' at 1 >= left(1), left=2, map={a:3,b:4,c:2}, len=3
right=5, c='c': 'c' at 2 >= left(2), left=3, map={a:3,b:4,c:5}, len=3
right=6, c='b': 'b' at 4 >= left(3), left=5, map={a:3,b:6,c:5}, len=2
right=7, c='b': 'b' at 6 >= left(5), left=7, map={a:3,b:7,c:5}, len=1

Max length = 3
```

### Complexity Analysis
- **Time Complexity:** O(n) - Single pass
- **Space Complexity:** O(min(n, m)) - HashMap size

### Why This is Better
- ✅ Single pass through string
- ✅ Direct jump instead of incremental shrinking
- ✅ Fewer operations per character
- ✅ Optimal solution

---

## Key Takeaways

1. **Pattern:** Sliding window for substring problems
2. **Window expansion:** Move right pointer to explore
3. **Window contraction:** Move left pointer to maintain validity
4. **HashMap optimization:** Store indices to enable direct jumps
5. **Condition check:** Ensure last occurrence is in current window

---

## Edge Cases

- Empty string: `""` → `0`
- Single character: `"a"` → `1`
- All unique: `"abcdef"` → `6`
- All same: `"aaaa"` → `1`
- Spaces and symbols: `" "` → `1`

---

## Related Problems
- [[Longest-Repeating-Character-Replacement]] - Similar sliding window
- [[Minimum-Window-Substring]] - Advanced sliding window
- [[Permutation-in-String]] - Sliding window with frequency

---

## Tags
#strings #sliding-window #hash-table #medium #blind75

---

## Visualization

- Embed: `![](../assets/longest-substring/step-1.svg)`
- Obsidian embed: `![[../assets/longest-substring/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="140">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <rect x="8" y="8" width="744" height="124" fill="#ffffff" stroke="#e3e8ef" rx="8"/>
    <text x="20" y="32" fill="#222">Window example (s = "abcabcbb")</text>
    <g transform="translate(20,50)">
        <rect x="0" y="0" width="48" height="48" fill="#fff" stroke="#3a7bd5"/>
        <text x="24" y="32" text-anchor="middle">a</text>
        <rect x="58" y="0" width="48" height="48" fill="#fff" stroke="#3a7bd5"/>
        <text x="82" y="32" text-anchor="middle">b</text>
        <rect x="116" y="0" width="48" height="48" fill="#fff" stroke="#3a7bd5"/>
        <text x="140" y="32" text-anchor="middle">c</text>
        <rect x="174" y="0" width="48" height="48" fill="#fff" stroke="#3a7bd5"/>
        <text x="198" y="32" text-anchor="middle">a</text>
    </g>
</svg>
