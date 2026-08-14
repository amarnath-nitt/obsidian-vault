# Longest Word in Dictionary

[Problem Link](https://leetcode.com/problems/longest-word-in-dictionary/)

## Problem Statement
Given an array of strings `words` representing an English Dictionary, return the longest word in `words` that can be built one character at a time by other words in `words`.
If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

## Approach
Trie + DFS/BFS or Set.
Using Set: Sort words. Iterate. If `word.substring(0, len-1)` is in set, add word to set and update best.
Using Trie: Insert all. Mark ends. DFS from root, only go to nodes that are ends.

## Time and Space Complexity
- **Time Complexity:** O(N * L).
- **Space Complexity:** O(N * L).

## Code
```java
class Solution {
    public String longestWord(String[] words) {
        Arrays.sort(words);
        Set<String> built = new HashSet<>();
        String res = "";
        
        for (String w : words) {
            if (w.length() == 1 || built.contains(w.substring(0, w.length() - 1))) {
                built.add(w);
                if (w.length() > res.length() || (w.length() == res.length() && w.compareTo(res) < 0)) {
                    res = w; // W is already sorted lexicographically, but string comparison needed if lengths equal?
                             // Actually if sorted by string, longer words come later? No.
                             // Arrays.sort sorts lexicographically. 
                             // So "apple" comes after "app".
                             // We check length. If length > res.length, take it.
                             // If length == res.length, we prefer lexicographically smaller.
                             // But since we iterate in sorted order, we replace only if strictly longer?
                             // Wait. "a", "banana". "app", "appl", "apple".
                             // "apply".
                             // "apple" (5) vs "apply" (5). "apple" comes first.
                             // So if we see "apple", update res. 
                             // Later see "apply". Length is same. We do NOT update.
                             // So simple length check > is sufficient if processed in lex order.
                             // Actually, is it?
                             // "a", "b". Res="a". Visiting "b". Length same. Don't update. Correct.
                             // So strict length > is enough.
                    res = w;
                }
            }
        }
        return res;
    }
}
```
