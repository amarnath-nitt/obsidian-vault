# Majority Element II (n/3 times)

**LeetCode 229** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/majority-element-ii/)

### Problem
Find all elements that appear more than `n/3` times. Return as list.

### Approach (Extended Boyer-Moore — 2 candidates)

- At most **2** elements can appear > n/3 times
- Track 2 candidates and 2 counts
- Two-pass: first pass finds candidates, second pass verifies

### Java Solution

```java
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int cand1 = 0, cand2 = 0, cnt1 = 0, cnt2 = 0;

        for (int num : nums) {
            if (num == cand1) cnt1++;
            else if (num == cand2) cnt2++;
            else if (cnt1 == 0) { cand1 = num; cnt1 = 1; }
            else if (cnt2 == 0) { cand2 = num; cnt2 = 1; }
            else { cnt1--; cnt2--; }
        }

        cnt1 = 0; cnt2 = 0;
        for (int num : nums) {
            if (num == cand1) cnt1++;
            else if (num == cand2) cnt2++;
        }

        List<Integer> result = new ArrayList<>();
        int threshold = nums.length / 3;
        if (cnt1 > threshold) result.add(cand1);
        if (cnt2 > threshold) result.add(cand2);
        return result;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
