# Group Anagrams

**LeetCode 49** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/group-anagrams/)

### Approach

- Key = sorted version of the word (all anagrams share same sorted form)
- Group words by their sorted key in a HashMap

### Java Solution

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
```

**Complexity:** Time O(n × k log k) where k = max string length · Space O(nk)

**Alternative key:** frequency count array as string `"1#0#2#..."` — O(n × k) time

---
