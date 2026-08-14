# Day 15 — Strings I

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** String Algorithms — Anagram, KMP, Hashing
**Difficulty Mix:** Easy / Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Valid Anagram]] | 242 | Easy | ⬜ |
| 2 | [[#Group Anagrams]] | 49 | Medium | ⬜ |
| 3 | [[#Longest Palindromic Substring]] | 5 | Medium | ⬜ |
| 4 | [[#Count and Say]] | 38 | Medium | ⬜ |
| 5 | [[#KMP — Find Pattern in String]] | 28 | Medium | ⬜ |
| 6 | [[#Rabin-Karp String Hashing]] | — | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Valid Anagram | Sort both strings and compare. O(n log n). | Frequency HashMap. O(n) space. | Fixed-size count array. O(n), O(1) for bounded alphabet. |
| Group Anagrams | Compare each word against existing groups. O(n^2*k). | Sort each word as the key. O(n*k log k). | Character-count signature as key. O(n*k). |
| Longest Palindromic Substring | Check every substring. O(n^3). | DP palindrome table. O(n^2) space. | Expand around centers. O(n^2) time, O(1) space. |
| Count and Say | Recompute previous terms recursively. Repeated work. | Iteratively run-length encode the previous term. | StringBuilder per row; total work is proportional to generated output. |
| KMP - Find Pattern in String | Try every start and compare pattern. O(n*m). | Rolling hash / Rabin-Karp average O(n+m). | KMP LPS table avoids rechecking characters. O(n+m). |
| Rabin-Karp String Hashing | Compare every substring directly. O(n*m). | Rolling hash for O(1) window hash updates. | Double hash or verify matches to control collisions. |

---

## Valid Anagram

**LeetCode 242** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/valid-anagram/)

### Approach

- Use frequency array of size 26
- Increment for `s`, decrement for `t`
- Check all zeros

### Java Solution

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
            freq[t.charAt(i) - 'a']--;
        }
        for (int f : freq) if (f != 0) return false;
        return true;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Group Anagrams

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

## Longest Palindromic Substring

**LeetCode 5** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/longest-palindromic-substring/)

### Approach (Expand Around Center)

- For each center position (2n-1 centers including between chars)
- Expand outward while characters match
- Track max length palindrome

### Java Solution

```java
class Solution {
    String result = "";

    public String longestPalindrome(String s) {
        for (int i = 0; i < s.length(); i++) {
            expand(s, i, i);     // odd length
            expand(s, i, i + 1); // even length
        }
        return result;
    }

    private void expand(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--; r++;
        }
        // [l+1, r-1] is the palindrome
        if (r - l - 1 > result.length())
            result = s.substring(l + 1, r);
    }
}
```

**Complexity:** Time O(n²) · Space O(1)

> **Manacher's Algorithm** solves this in O(n) — complex but worth knowing.

---

## Count and Say

**LeetCode 38** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/count-and-say/)

### Problem
RLE sequence: 1 → "1", 11 → "21", 21 → "1211", ...

### Approach

- Start from "1", build each level by counting consecutive chars

### Java Solution

```java
class Solution {
    public String countAndSay(int n) {
        String result = "1";
        for (int i = 1; i < n; i++) {
            StringBuilder next = new StringBuilder();
            int j = 0;
            while (j < result.length()) {
                char c = result.charAt(j);
                int count = 0;
                while (j < result.length() && result.charAt(j) == c) {
                    j++; count++;
                }
                next.append(count).append(c);
            }
            result = next.toString();
        }
        return result;
    }
}
```

**Complexity:** Time O(n × max_length) · Space O(max_length)

---

## KMP — Find Pattern in String

**LeetCode 28** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

### Problem
Find first occurrence of `needle` in `haystack`.

### Approach (KMP Algorithm)

**Phase 1: Build LPS (Longest Proper Prefix which is also Suffix) array**
- `lps[i]` = length of longest proper prefix of `pattern[0..i]` that is also a suffix

**Phase 2: Search using LPS**
- On mismatch: jump using `lps[j-1]` instead of restarting from beginning

### Java Solution

```java
class Solution {
    public int strStr(String haystack, String needle) {
        int n = haystack.length(), m = needle.length();
        if (m == 0) return 0;

        // Build LPS
        int[] lps = new int[m];
        for (int i = 1, len = 0; i < m; ) {
            if (needle.charAt(i) == needle.charAt(len)) lps[i++] = ++len;
            else if (len > 0) len = lps[len - 1];
            else lps[i++] = 0;
        }

        // Search
        for (int i = 0, j = 0; i < n; ) {
            if (haystack.charAt(i) == needle.charAt(j)) { i++; j++; }
            if (j == m) return i - j;
            else if (i < n && haystack.charAt(i) != needle.charAt(j)) {
                if (j > 0) j = lps[j - 1];
                else i++;
            }
        }
        return -1;
    }
}
```

**Complexity:** Time O(n+m) · Space O(m)

---

## Rabin-Karp String Hashing

**Approach:** Rolling hash to find pattern in text in O(n+m) average.

```java
public int search(String text, String pattern) {
    int n = text.length(), m = pattern.length();
    long base = 31, mod = 1_000_000_007;
    long patHash = 0, winHash = 0, power = 1;

    for (int i = 0; i < m - 1; i++) power = power * base % mod;

    for (int i = 0; i < m; i++) {
        patHash = (patHash * base + pattern.charAt(i)) % mod;
        winHash = (winHash * base + text.charAt(i)) % mod;
    }

    for (int i = 0; i <= n - m; i++) {
        if (winHash == patHash) {
            // Verify (collision check)
            if (text.substring(i, i + m).equals(pattern)) return i;
        }
        if (i < n - m) {
            winHash = (winHash - text.charAt(i) * power % mod + mod) % mod;
            winHash = (winHash * base + text.charAt(i + m)) % mod;
        }
    }
    return -1;
}
```

**Complexity:** Time O(n+m) average, O(nm) worst · Space O(1)

---

## String Algorithm Comparison

| Algorithm | Time | Space | Use When |
|-----------|------|-------|----------|
| Brute Force | O(nm) | O(1) | Short strings |
| KMP | O(n+m) | O(m) | Pattern search, guaranteed linear |
| Rabin-Karp | O(n+m) avg | O(1) | Multiple pattern search |
| Z-Algorithm | O(n+m) | O(n+m) | Pattern + string properties |

#sde-sheet #strings #kmp #day15
