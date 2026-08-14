# Day 7 — Two Pointers & Sliding Window

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Two Pointers · Sliding Window
**Difficulty Mix:** Easy / Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#3-Sum]] | 15 | Medium | ⬜ |
| 2 | [[#Trapping Rain Water]] | 42 | Hard | ⬜ |
| 3 | [[#Remove Duplicates from Sorted Array]] | 26 | Easy | ⬜ |
| 4 | [[#Max Consecutive Ones III]] | 1004 | Medium | ⬜ |
| 5 | [[#Minimum Window Substring]] | 76 | Hard | ⬜ |
| 6 | [[#Longest Substring Without Repeating Characters]] | 3 | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| 3-Sum | Check every triplet. O(n^3). | Fix one number and use a HashSet for two-sum. O(n^2) space/time. | Sort, fix one number, two pointers, skip duplicates. O(n^2). |
| Trapping Rain Water | For each index, scan left and right max. O(n^2). | Prefix max and suffix max arrays. O(n) space. | Two pointers tracking leftMax/rightMax. O(n), O(1). |
| Remove Duplicates from Sorted Array | Use a set/new array. O(n) space. | Shift elements left after duplicates. O(n^2). | Slow/fast overwrite unique values. O(n), O(1). |
| Max Consecutive Ones III | Check every window and count zeros. O(n^2). | Prefix zero counts with binary search. O(n log n). | Sliding window with at most k zeros. O(n). |
| Minimum Window Substring | Test every substring against target counts. O(n^3). | Use frequency counts to validate faster. O(n^2). | Sliding window with need/have counts. O(n). |
| Longest Substring Without Repeating Characters | Check every substring for uniqueness. O(n^3). | Sliding window with a HashSet. O(n). | Last-seen index map to jump left pointer. O(n). |

---

## 3-Sum

**LeetCode 15** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/3sum/)

### Problem
Find all unique triplets that sum to zero.

### Approach

1. **Sort** the array
2. Fix one element `nums[i]`
3. Use **Two Pointers** on the rest
4. Skip duplicates carefully

### Java Solution

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue; // skip outer dup

            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left+1]) left++;
                    while (left < right && nums[right] == nums[right-1]) right--;
                    left++; right--;
                } else if (sum < 0) left++;
                else right--;
            }
        }
        return result;
    }
}
```

**Complexity:** Time O(n²) · Space O(1) excluding output

---

## Trapping Rain Water

**LeetCode 42** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/trapping-rain-water/)

### Problem
Given an elevation map, compute how much water can be trapped.

### Approach 1 — Prefix Max Arrays O(n) time, O(n) space

- `leftMax[i]` = max height from left up to i
- `rightMax[i]` = max height from right up to i
- Water at i = `min(leftMax[i], rightMax[i]) - height[i]`

### Approach 2 — Two Pointers O(n) time, O(1) space ✅

- If `leftMax < rightMax` → process left pointer (it's the bottleneck)
- Else → process right pointer

### Java Solution (Two Pointers)

```java
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0, water = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) leftMax = height[left];
                else water += leftMax - height[left];
                left++;
            } else {
                if (height[right] >= rightMax) rightMax = height[right];
                else water += rightMax - height[right];
                right--;
            }
        }
        return water;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Remove Duplicates from Sorted Array

**LeetCode 26** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

### Problem
Remove duplicates in-place from sorted array, return new length.

### Approach (Slow-Fast Write Pointer)

- `slow` = where to write the next unique element
- `fast` scans the array

### Java Solution

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int slow = 1;
        for (int fast = 1; fast < nums.length; fast++) {
            if (nums[fast] != nums[fast - 1]) {
                nums[slow++] = nums[fast];
            }
        }
        return slow;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Max Consecutive Ones III

**LeetCode 1004** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/max-consecutive-ones-iii/)

### Problem
Given binary array, you can flip at most k zeros. Find max length of consecutive 1s.

### Approach (Sliding Window)

- Maintain a window with at most k zeros
- Expand right; when zeros > k, shrink from left

### Java Solution

```java
class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0, zeros = 0, maxLen = 0;

        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > k) {
                if (nums[left] == 0) zeros--;
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Minimum Window Substring

**LeetCode 76** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/minimum-window-substring/)

### Problem
Find the minimum window in `s` that contains all characters of `t`.

### Approach (Sliding Window + Frequency Map)

1. Count all characters in `t` → `need` map
2. Expand `right` until window contains all required chars
3. Once valid, shrink `left` to minimize
4. Track minimum window

### Java Solution

```java
class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> need = new HashMap<>();
        for (char c : t.toCharArray()) need.merge(c, 1, Integer::sum);

        int left = 0, matched = 0, minLen = Integer.MAX_VALUE, minStart = 0;
        Map<Character, Integer> window = new HashMap<>();

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            window.merge(c, 1, Integer::sum);
            if (need.containsKey(c) && window.get(c).equals(need.get(c))) matched++;

            while (matched == need.size()) {
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minStart = left;
                }
                char lc = s.charAt(left);
                window.merge(lc, -1, Integer::sum);
                if (need.containsKey(lc) && window.get(lc) < need.get(lc)) matched--;
                left++;
            }
        }
        return minLen == Integer.MAX_VALUE ? "" : s.substring(minStart, minStart + minLen);
    }
}
```

**Complexity:** Time O(|s| + |t|) · Space O(|t|)

---

## Longest Substring Without Repeating Characters

**LeetCode 3** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

### Problem
Find the length of the longest substring without repeating characters.

### Approach (Sliding Window + HashMap)

- Track last seen index of each character
- When duplicate found, move `left` to `max(left, lastSeen[char] + 1)`

### Java Solution

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> lastSeen = new HashMap<>();
        int maxLen = 0, left = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (lastSeen.containsKey(c) && lastSeen.get(c) >= left) {
                left = lastSeen.get(c) + 1;
            }
            lastSeen.put(c, right);
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

**Complexity:** Time O(n) · Space O(min(n, alphabet))

---

## Sliding Window Template

```java
// Fixed size window of size k
int sum = 0;
for (int i = 0; i < k; i++) sum += arr[i];
int maxSum = sum;
for (int i = k; i < arr.length; i++) {
    sum += arr[i] - arr[i - k];
    maxSum = Math.max(maxSum, sum);
}

// Variable size window (expand right, shrink left when invalid)
int left = 0;
for (int right = 0; right < arr.length; right++) {
    // add arr[right] to window state
    while (/* window is invalid */) {
        // remove arr[left] from window state
        left++;
    }
    // update answer with window [left, right]
}
```

#sde-sheet #two-pointers #sliding-window #day7
