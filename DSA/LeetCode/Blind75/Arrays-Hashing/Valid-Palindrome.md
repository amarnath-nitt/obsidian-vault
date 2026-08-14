# Valid Palindrome

**Difficulty:** Easy  
**Category:** Arrays & Hashing / Two Pointers  
**LeetCode Link:** [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

---

## Problem Statement

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Example 1:**
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

**Example 3:**
```
Input: s = " "
Output: true
Explanation: Empty string after removing non-alphanumeric is palindrome.
```

**Constraints:**
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

---

## Intuition

We need to check if the string reads the same forwards and backwards, ignoring case and non-alphanumeric characters.

---

## Approach 1: Build Filtered String (Naive Solution)

### Algorithm
1. Create a new string with only alphanumeric characters (lowercase)
2. Compare the string with its reverse

### Java Code
```java
class Solution {
    public boolean isPalindrome(String s) {
        // Build filtered string
        StringBuilder filtered = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                filtered.append(Character.toLowerCase(c));
            }
        }
        
        // Compare with reverse
        String str = filtered.toString();
        String reversed = filtered.reverse().toString();
        
        return str.equals(reversed);
    }
}
```

### Alternative Using Streams
```java
class Solution {
    public boolean isPalindrome(String s) {
        String filtered = s.toLowerCase()
                          .replaceAll("[^a-z0-9]", "");
        
        String reversed = new StringBuilder(filtered)
                          .reverse()
                          .toString();
        
        return filtered.equals(reversed);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Process string twice
- **Space Complexity:** O(n) - Store filtered string

### Drawbacks
- Uses extra space for filtered string
- Creates reversed string unnecessarily

---

## Approach 2: Two Pointers (Optimized Solution)

### Algorithm
1. Use two pointers: left (start) and right (end)
2. Skip non-alphanumeric characters from both ends
3. Compare characters (case-insensitive)
4. Move pointers inward
5. If all comparisons match, it's a palindrome

### Java Code
```java
class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            // Skip non-alphanumeric from left
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            
            // Skip non-alphanumeric from right
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            
            // Compare characters (case-insensitive)
            if (Character.toLowerCase(s.charAt(left)) != 
                Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            
            left++;
            right--;
        }
        
        return true;
    }
}
```

### Step-by-Step Example
For `s = "A man, a plan, a canal: Panama"`:

```
left=0, right=30: 'A' vs 'a' → match, move pointers
left=1, right=29: skip ' ', 'm' vs 'm' → match
left=2, right=28: 'a' vs 'a' → match
left=3, right=27: 'n' vs 'n' → match
...continues until pointers meet
```

### Complexity Analysis
- **Time Complexity:** O(n) - Single pass with two pointers
- **Space Complexity:** O(1) - Only using pointers

### Why This is Better
- ✅ O(1) space complexity
- ✅ Single pass through string
- ✅ No string building or reversal needed
- ✅ Early termination on mismatch

---

## Key Takeaways

1. **Pattern:** Two pointers from both ends is common for palindrome problems
2. **Space optimization:** In-place comparison vs building new string
3. **Character utilities:** Use `Character.isLetterOrDigit()` and `Character.toLowerCase()`
4. **Early exit:** Return false immediately on mismatch

---

## Common Mistakes

- Forgetting to handle uppercase/lowercase
- Not skipping non-alphanumeric characters properly
- Using `==` instead of comparing character values
- Not handling empty strings after filtering

---

## Edge Cases

- Empty string: `""` → `true`
- Only spaces: `"   "` → `true`
- Single character: `"a"` → `true`
- No alphanumeric: `".,!"` → `true`
- Mixed case: `"Aa"` → `true`

---

## Related Problems
- [[Palindrome-Linked-List]] - Palindrome in linked list
- [[Valid-Palindrome-II]] - Allow one deletion
- [[Longest-Palindromic-Substring]] - Find longest palindrome

---

## Tags
#strings #two-pointers #palindrome #easy #blind75
