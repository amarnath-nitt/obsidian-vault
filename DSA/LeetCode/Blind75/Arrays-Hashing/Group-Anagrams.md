# Group Anagrams

**Difficulty:** Medium  
**Category:** Arrays & Hashing  
**LeetCode Link:** [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

---

## Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**
```
Input: strs = ["a"]
Output: [["a"]]
```

**Constraints:**
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

## Intuition

Anagrams have the same characters with the same frequencies. We need a way to identify which strings are anagrams of each other and group them together.

---

## Approach 1: Sort Each String (Naive Solution)

### Algorithm
1. For each string, sort its characters to create a "signature"
2. Use this sorted string as a key in a HashMap
3. Group all strings with the same sorted signature together

### Java Code
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Map: sorted string -> list of original strings
        Map<String, List<String>> map = new HashMap<>();
        
        for (String str : strs) {
            // Sort the string to create signature
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            
            // Add to corresponding group
            if (!map.containsKey(sorted)) {
                map.put(sorted, new ArrayList<>());
            }
            map.get(sorted).add(str);
        }
        
        // Return all groups
        return new ArrayList<>(map.values());
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n * k log k) where n = number of strings, k = max length of string
  - Sorting each string takes O(k log k)
  - We do this for n strings
- **Space Complexity:** O(n * k) - Storing all strings in the map

### Drawbacks
- Sorting is expensive for long strings
- Can we avoid sorting?

---

## Approach 2: Character Count as Key (Optimized Solution)

### Algorithm
1. For each string, create a character frequency signature
2. Use this frequency signature as the HashMap key
3. Group strings with identical frequency signatures

### Java Code
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Map: character count signature -> list of strings
        Map<String, List<String>> map = new HashMap<>();
        
        for (String str : strs) {
            // Create character count array
            int[] count = new int[26];
            for (char c : str.toCharArray()) {
                count[c - 'a']++;
            }
            
            // Convert count array to string key
            // Format: "1#0#0#1#..." where # separates counts
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                sb.append(count[i]);
                sb.append('#');
            }
            String key = sb.toString();
            
            // Add to corresponding group
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(str);
        }
        
        return new ArrayList<>(map.values());
    }
}
```

### Alternative Using Arrays.toString()
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        
        for (String str : strs) {
            int[] count = new int[26];
            for (char c : str.toCharArray()) {
                count[c - 'a']++;
            }
            
            // Use Arrays.toString() as key
            String key = Arrays.toString(count);
            
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }
        
        return new ArrayList<>(map.values());
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n * k) where n = number of strings, k = max length
  - Creating frequency count takes O(k) per string
  - We do this for n strings
- **Space Complexity:** O(n * k) - Storing all strings

### Why This is Better
- ✅ Linear time per string (no sorting)
- ✅ Faster for longer strings
- ✅ Still uses hashing for O(1) grouping
- ✅ More efficient than O(k log k) sorting

---

## Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sorting | O(n * k log k) | O(n * k) | Simple but slower |
| Frequency Count | O(n * k) | O(n * k) | Optimal time |

---

## Key Takeaways

1. **Pattern:** Use character frequency as a unique identifier for anagrams
2. **HashMap grouping:** Map signature → list of items is a common pattern
3. **Key design:** The key must uniquely identify anagram groups
4. **Delimiter importance:** Use '#' to separate counts (e.g., "12#1" vs "1#21")
5. **computeIfAbsent:** Clean way to initialize map entries in Java

---

## Edge Cases

- Empty string: `[""]` → `[[""]]`
- Single character: `["a"]` → `[["a"]]`
- All same: `["a","a","a"]` → `[["a","a","a"]]`
- No anagrams: `["abc","def","ghi"]` → `[["abc"],["def"],["ghi"]]`

---

## Related Problems
- [[Valid-Anagram]] - Check if two strings are anagrams
- [[Find-All-Anagrams]] - Find anagram substrings
- [[Group-Shifted-Strings]] - Similar grouping problem

---

## Tags
#strings #hashing #sorting #frequency-count #medium #blind75
