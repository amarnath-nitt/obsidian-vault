# Reverse String

[Problem Link](https://leetcode.com/problems/reverse-string/)

## Problem Statement
Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.

## Approach
Use two pointers, `left` at start and `right` at end. Swap elements and move pointers towards center.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public void reverseString(char[] s) {
        int left = 0; 
        int right = s.length - 1;
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
}
```
