# Majority Element (n/2 times)

**LeetCode 169** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/majority-element/)

### Problem
Find the element that appears more than `n/2` times. Guaranteed to exist.

### Approach (Boyer-Moore Voting Algorithm)

- Maintain a `candidate` and a `count`
- If count == 0 → new candidate
- If current == candidate → count++
- Else → count--
- The candidate at the end is the majority element

### Java Solution

```java
class Solution {
    public int majorityElement(int[] nums) {
        int candidate = nums[0], count = 1;

        for (int i = 1; i < nums.length; i++) {
            if (count == 0) {
                candidate = nums[i];
                count = 1;
            } else if (nums[i] == candidate) {
                count++;
            } else {
                count--;
            }
        }
        return candidate;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
