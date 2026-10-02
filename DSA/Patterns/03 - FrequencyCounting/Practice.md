# Frequency Counting - Practice Notes

## Pattern Overview
Uses HashMap or array to count frequencies of elements for efficient lookups and comparisons.

## Key Concepts
- **HashMap**: For unlimited range of values
- **Array**: For limited range (0-255, 'a'-'z')
- **Time Complexity**: O(n)

## Template Code

### Using HashMap
```java
Map<Character, Integer> freq = new HashMap<>();
for (char c : s.toCharArray()) {
    freq.put(c, freq.getOrDefault(c, 0) + 1);
}
```

### Using Array
```java
int[] freq = new int[26];
for (char c : s.toCharArray()) {
    freq[c - 'a']++;
}
```

## Practice Problems

### Easy
- [x] [Valid Anagram](https://leetcode.com/problems/valid-anagram/) (LC 242) → [Solution](solutions/LC-242-Valid-Anagram.md)
- [x] [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) (LC 387) → [Solution](solutions/LC-387-First-Unique-Character.md)
- [x] [Ransom Note](https://leetcode.com/problems/ransom-note/) (LC 383) → [Solution](solutions/LC-383-Ransom-Note.md)
- [x] [Majority Element](https://leetcode.com/problems/majority-element/) (LC 169) → [Solution](solutions/LC-169-Majority-Element.md)
- [x] [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (LC 217) → [Solution](solutions/LC-217-Contains-Duplicate.md)

### Medium
- [x] [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (LC 347) → [Solution](solutions/LC-347-Top-K-Frequent-Elements.md)
- [x] [Group Anagrams](https://leetcode.com/problems/group-anagrams/) (LC 49) → [Solution](solutions/LC-49-Group-Anagrams.md)
- [x] [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) (LC 438) → [Solution](../06 - SlidingWindow/solutions/LC-438-Find-All-Anagrams.md)
- [x] [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (LC 560) → [Solution](../02 - PrefixSum/solutions/LC-560-Subarray-Sum-Equals-K.md)
- [x] [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) (LC 128) → [Solution](solutions/LC-128-Longest-Consecutive-Sequence.md)

### Hard
- [x] [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) (LC 41) → [Solution](solutions/LC-41-First-Missing-Positive.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gXzrFVg3)
