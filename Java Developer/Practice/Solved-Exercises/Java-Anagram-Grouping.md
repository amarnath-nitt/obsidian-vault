# Anagram Grouping (LC 49)

**Concept tested**: Grouping by normalized keys using Streams.

## Problem
Given an array of strings, group the anagrams together.

## Solution
```java
public List<List<String>> groupAnagrams(String[] strs) {
    return Arrays.stream(strs)
        .collect(Collectors.groupingBy(s -> {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            return new String(chars);
        }))
        .values()
        .stream()
        .collect(Collectors.toList());
}
```

## Alternative (Frequency Array Key)
For better performance (avoiding $O(K \log K)$ sort per string):
```java
public List<List<String>> groupAnagrams(String[] strs) {
    return Arrays.stream(strs)
        .collect(Collectors.groupingBy(s -> {
            int[] count = new int[26];
            for (char c : s.toCharArray()) count[c - 'a']++;
            return Arrays.toString(count);
        }))
        .values().stream().toList();
}
```

## Complexity
- **Time**: $O(N \cdot K \log K)$ where $N$ is number of strings and $K$ is max length.
- **Space**: $O(N \cdot K)$.

## Interview Explanation
We normalize each string by sorting its characters alphabetically. Anagrams will result in the same sorted string, which we use as the key for the `groupingBy` collector.