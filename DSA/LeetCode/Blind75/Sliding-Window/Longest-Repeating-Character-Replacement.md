# Longest Repeating Character Replacement

**Difficulty:** Medium  
**Category:** Sliding Window  
**LeetCode Link:** [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

---

## Problem Statement

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

**Example 1:**
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

**Example 2:**
```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace one 'A' in the middle with 'B' → "AABBBBA", substring "BBBB" has length 4.
```

**Constraints:**
- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

---

## Intuition

We want the longest substring where we can make all characters the same by changing at most `k` characters. Key insight: In a valid window, `window_size - max_frequency <= k`.

---

## Approach 1: Brute Force (Naive Solution)

### Algorithm
1. Try all possible substrings
2. For each substring, find the most frequent character
3. Check if we can convert the rest with ≤ k changes
4. Track maximum valid length

### Java Code
```java
class Solution {
    public int characterReplacement(String s, int k) {
        int maxLength = 0;
        
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                // Count frequency in substring
                int[] freq = new int[26];
                int maxFreq = 0;
                
                for (int idx = i; idx <= j; idx++) {
                    freq[s.charAt(idx) - 'A']++;
                    maxFreq = Math.max(maxFreq, freq[s.charAt(idx) - 'A']);
                }
                
                int windowSize = j - i + 1;
                int replacements = windowSize - maxFreq;
                
                if (replacements <= k) {
                    maxLength = Math.max(maxLength, windowSize);
                }
            }
        }
        
        return maxLength;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n³) - Nested loops + frequency counting
- **Space Complexity:** O(1) - Fixed size frequency array

---

## Approach 2: Sliding Window (Optimized Solution)

### Algorithm
1. Use sliding window with `left` and `right` pointers
2. Track character frequencies in current window
3. Track max frequency seen in current window
4. If `window_size - max_frequency > k`, shrink window from left
5. Update maximum window size

### Java Code
```java
class Solution {
    public int characterReplacement(String s, int k) {
        int[] freq = new int[26];
        int maxFreq = 0;
        int maxLength = 0;
        int left = 0;
        
        for (int right = 0; right < s.length(); right++) {
            // Add right character to window
            freq[s.charAt(right) - 'A']++;
            maxFreq = Math.max(maxFreq, freq[s.charAt(right) - 'A']);
            
            // Check if window is valid
            int windowSize = right - left + 1;
            int replacements = windowSize - maxFreq;
            
            // Shrink window if invalid
            if (replacements > k) {
                freq[s.charAt(left) - 'A']--;
                left++;
            }
            
            // Update max length
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}
```

### Step-by-Step Example
For `s = "AABABBA", k = 1`:

```
right=0, 'A': freq={A:1}, maxFreq=1, window=1, replacements=0, valid
right=1, 'A': freq={A:2}, maxFreq=2, window=2, replacements=0, valid
right=2, 'B': freq={A:2,B:1}, maxFreq=2, window=3, replacements=1, valid
right=3, 'A': freq={A:3,B:1}, maxFreq=3, window=4, replacements=1, valid
right=4, 'B': freq={A:3,B:2}, maxFreq=3, window=5, replacements=2 > k
  → shrink: left=1, freq={A:2,B:2}, window=4, replacements=2 > k
  → shrink: left=2, freq={A:1,B:2}, window=3, replacements=1, valid
right=5, 'B': freq={A:1,B:3}, maxFreq=3, window=4, replacements=1, valid ✓
right=6, 'A': freq={A:2,B:3}, maxFreq=3, window=5, replacements=2 > k
  → shrink: left=3, freq={A:2,B:2}, window=4, replacements=2 > k
  → shrink: left=4, freq={A:1,B:2}, window=3

Max length = 4 (substring "BBBB" from index 2-5 after replacing one 'A')
```

### Complexity Analysis
- **Time Complexity:** O(n) - Single pass with two pointers
- **Space Complexity:** O(1) - Fixed size array (26 letters)

### Why This is Better
- ✅ Linear time complexity
- ✅ Sliding window maintains valid state
- ✅ No need to recount frequencies
- ✅ Optimal solution

---

## Key Insight

**Valid Window Condition:** `window_size - max_frequency_in_window <= k`

- `max_frequency` = count of most common character in window
- `window_size - max_frequency` = characters that need to be changed
- If this exceeds `k`, window is invalid

---

## Key Takeaways

1. **Pattern:** Sliding window with frequency tracking
2. **Validity condition:** Replacements needed = window size - max frequency
3. **Optimization:** Don't need to update maxFreq when shrinking (still works)
4. **Window expansion/contraction:** Expand right, shrink left when invalid

---

## Edge Cases

- All same character: `"AAAA", k=0` → `4`
- k = 0: `"ABCD", k=0` → `1`
- k >= length: `"ABCD", k=4` → `4`
- Single character: `"A", k=1` → `1`

---

## Related Problems
- [[Longest-Substring-Without-Repeating-Characters]] - Similar sliding window
- [[Minimum-Window-Substring]] - Advanced sliding window
- [[Max-Consecutive-Ones-III]] - Similar replacement concept

---

## Tags
#strings #sliding-window #hash-table #medium #blind75
