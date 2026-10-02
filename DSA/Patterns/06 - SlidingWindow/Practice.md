# Sliding Window Pattern - Practice Notes

## Pattern Overview
Sliding Window is used to perform operations on a specific window size of an array or string, efficiently sliding the window across the data.

## Key Concepts
- **Fixed Window**: Window size is constant
- **Dynamic Window**: Window size changes based on conditions
- **Time Complexity**: O(n)

## Template Code

### Fixed Window
```java
int windowSum = 0, maxSum = Integer.MIN_VALUE;
for (int i = 0; i < k; i++) {
    windowSum += arr[i];
}
maxSum = windowSum;

for (int i = k; i < arr.length; i++) {
    windowSum = windowSum - arr[i - k] + arr[i];
    maxSum = Math.max(maxSum, windowSum);
}
```

### Dynamic Window
```java
int left = 0, right = 0;
Map<Character, Integer> window = new HashMap<>();

while (right < s.length()) {
    char c = s.charAt(right);
    window.put(c, window.getOrDefault(c, 0) + 1);
    right++;
    
    while (needShrink) {
        char d = s.charAt(left);
        window.put(d, window.get(d) - 1);
        left++;
    }
}
```

## Practice Problems

### Easy
- [x] [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) (LC 643) → [Solution](solutions/LC-643-Maximum-Average-Subarray.md)
- [x] [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) (LC 219) → [Solution](solutions/LC-219-Contains-Duplicate-II.md)

### Medium
- [x] [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (LC 3) → [Solution](solutions/LC-3-Longest-Substring.md)
- [x] [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) (LC 424) → [Solution](solutions/LC-424-Longest-Repeating-Character-Replacement.md)
- [x] [Permutation in String](https://leetcode.com/problems/permutation-in-string/) (LC 567) → [Solution](solutions/LC-567-Permutation-in-String.md)
- [x] [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) (LC 438) → [Solution](solutions/LC-438-Find-All-Anagrams.md)
- [x] [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) (LC 904) → [Solution](solutions/LC-904-Fruit-Into-Baskets.md)
- [x] [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) (LC 1004) → [Solution](solutions/LC-1004-Max-Consecutive-Ones-III.md)

### Hard
- [x] [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (LC 76) → [Solution](solutions/LC-76-Minimum-Window-Substring.md)
- [ ] [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (LC 239) → [Solution](solutions/LC-239-Sliding-Window-Maximum.md)
- [ ] [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) (LC 992) → [Solution](solutions/LC-992-Subarrays-with-K-Different-Integers.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gVqnKNdg)
