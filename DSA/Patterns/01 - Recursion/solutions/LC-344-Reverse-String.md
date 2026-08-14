# Reverse String (LC 344)

**Difficulty**: Easy  
**Pattern**: Recursion / Two Pointers  
**LeetCode**: https://leetcode.com/problems/reverse-string/

## Problem Statement
Reverse the input character array in-place.

## Recursive Idea
Swap the outside characters, then recursively reverse the inside range.

## Intuition: Two-Pointer Shrinking Window

### The Core Idea
Reverse by swapping from the outside inward:
- Start: pointers at both ends (left and right)
- Swap them
- Move both pointers inward (left→right, right→left)
- Stop when they meet or cross (left >= right)

This **shrinking window pattern** reverses the entire string in-place.

### Why It Works
After each swap, the outermost unmoved elements are in correct final positions:

```
Original: [a, b, c, d, e]
           L           R

Step 1: Swap L and R
       [e, b, c, d, a]  ← 'a' and 'e' now in correct positions
        L           R

Move L→right, R→left:
       [e, b, c, d, a]
           L     R

Step 2: Swap L and R
       [e, d, c, b, a]  ← 'd' and 'b' now in correct positions
           L     R

Move L→right, R→left:
       [e, d, c, b, a]
             L R

Step 3: left >= right, stop (middle element 'c' already correct)
Result: [e, d, c, b, a] ✓
```

### Recursion vs Iteration

**Recursive Version:**
- Uses call stack to shrink the range by one level each call
- Elegant and intuitive
- Space: O(n) for call stack (not ideal for large arrays)

```java
reverse(s, 0, s.length()-1)  // Level 1: swap s[0] and s[n-1]
  → reverse(s, 1, s.length()-2)  // Level 2: swap s[1] and s[n-2]
    → reverse(s, 2, s.length()-3)  // Level 3: etc.
      → ...
```

**Iterative Version:**
- Explicitly manages two pointers without call stack
- More direct and efficient
- Space: O(1)

### Interview Perspective
"I can solve this with recursion, which uses the call stack to shrink the range at each level. However, the iterative two-pointer approach is more efficient with O(1) space, which I'd prefer to show in an interview since it has the same logic without the recursion overhead."

## Java Code
```java
class Solution {
    public void reverseString(char[] s) {
        reverse(s, 0, s.length - 1);
    }

    private void reverse(char[] s, int left, int right) {
        if (left >= right) {
            return;
        }

        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        reverse(s, left + 1, right - 1);
    }
}
```

## Alternative Optimal Solution: Iterative Two Pointers
The iterative version uses the same shrinking-window idea without recursion stack space.

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

### Alternative Complexity
- **Time**: O(n)
- **Space**: O(1)

## Complexity
- **Time**: O(n)
- **Space**: O(n) recursion stack

## Key Takeaways
- Recursive two-pointer problems usually shrink both ends.
