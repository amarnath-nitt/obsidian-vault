# Valid Palindrome

[Problem Link](https://leetcode.com/problems/valid-palindrome/)

## Problem Statement
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Approach
Use two pointers, `left` starting at the beginning and `right` at the end or the string.
1.  Move `left` forward until it points to an alphanumeric char.
2.  Move `right` backward until it points to an alphanumeric char.
3.  Compare characters at `left` and `right`. If not equal (ignoring case), return `false`.
4.  Move `left` forward and `right` backward.
5.  Repeat until `left >= right`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
}
```
