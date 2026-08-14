# Two Pointers Pattern - Practice Notes

## Pattern Overview
Two Pointers technique uses two pointers to traverse an array or list, typically from different positions, to solve problems efficiently.

## Key Concepts
- **Opposite Direction**: Start from both ends, move towards center
- **Same Direction**: Both start from beginning, move at different speeds
- **Time Complexity**: Usually O(n)
- **Space Complexity**: Usually O(1)

## Template Code

### Opposite Direction
```java
int left = 0, right = arr.length - 1;
while (left < right) {
    if (condition) {
        left++;
        right--;
    } else if (needMoveLeft) {
        left++;
    } else {
        right--;
    }
}
```

### Same Direction
```java
int slow = 0, fast = 0;
while (fast < arr.length) {
    if (condition) {
        arr[slow] = arr[fast];
        slow++;
    }
    fast++;
}
```

## Practice Problems

### Easy
- [x] [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (LC 125) → [Solution](solutions/LC-125-Valid-Palindrome.md)
- [x] [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) (LC 26) → [Solution](solutions/LC-26-Remove-Duplicates.md)
- [x] [Move Zeroes](https://leetcode.com/problems/move-zeroes/) (LC 283) → [Solution](solutions/LC-283-Move-Zeroes.md)
- [x] [Reverse String](https://leetcode.com/problems/reverse-string/) (LC 344) → [Solution](solutions/LC-344-Reverse-String.md)
- [x] [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) (LC 88) → [Solution](solutions/LC-88-Merge-Sorted-Array.md)

### Medium
- [x] [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (LC 167) → [Solution](solutions/LC-167-Two-Sum-II.md)
- [x] [3Sum](https://leetcode.com/problems/3sum/) (LC 15) → [Solution](solutions/LC-15-3Sum.md)
- [x] [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (LC 11) → [Solution](solutions/LC-11-Container-With-Most-Water.md)
- [x] [Sort Colors](https://leetcode.com/problems/sort-colors/) (LC 75) → [Solution](solutions/LC-75-Sort-Colors.md)
- [x] [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (LC 42) → [Solution](solutions/LC-42-Trapping-Rain-Water.md)

### Hard
- [ ] [4Sum](https://leetcode.com/problems/4sum/) (LC 18) → [Solution](solutions/LC-18-4Sum.md)
- [ ] [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (LC 76)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gAs6WZ6X)
