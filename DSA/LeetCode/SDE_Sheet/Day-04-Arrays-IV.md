# Day 4 — Arrays IV (Hard Problems)

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Arrays — Hard Hitters
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Two Sum]] | 1 | Easy | ⬜ |
| 2 | [[#4-Sum]] | 18 | Medium | ⬜ |
| 3 | [[#Longest Consecutive Sequence]] | 128 | Medium | ⬜ |
| 4 | [[#Largest Subarray with Zero Sum]] | — | Medium | ⬜ |
| 5 | [[#Count Subarrays with XOR = k]] | — | Medium | ⬜ |
| 6 | [[#Longest Subarray with Sum K]] | — | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Two Sum | Try every pair. O(n^2). | Sort and use two pointers, preserving original indexes. O(n log n). | HashMap complement lookup in one pass. O(n), O(n) space. |
| 4-Sum | Use four nested loops. O(n^4). | Store pair sums in a map. O(n^2) space. | Sort, fix two numbers, then two pointers with duplicate skipping. O(n^3). |
| Longest Consecutive Sequence | For each number, search for the next values repeatedly. O(n^2) or worse. | Sort and count streaks. O(n log n). | HashSet; start counting only at sequence starts. O(n). |
| Largest Subarray with Zero Sum | Check all subarrays and compute sums. O(n^2) to O(n^3). | Use prefix sums. | Store first index of each prefix sum in a HashMap. O(n). |
| Count Subarrays with XOR = k | Compute XOR for every subarray. O(n^2). | Keep prefix XORs and compare pairs. O(n^2). | Prefix XOR frequency map using x ^ k. O(n). |
| Longest Subarray with Sum K | Try every subarray. O(n^2). | Sliding window works only for non-negative arrays. O(n). | Prefix sum first-index map works with negative numbers too. O(n). |

---

## Two Sum

**LeetCode 1** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/two-sum/)

### Problem
Find indices of two numbers that add up to target.

### Approach

- Use a **HashMap** to store `value → index`
- For each element, check if `target - nums[i]` exists in map

### Java Solution

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement))
                return new int[]{map.get(complement), i};
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---

## 4-Sum

**LeetCode 18** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/4sum/)

### Problem
Find all unique quadruplets in array that sum to target.

### Approach

- Sort the array
- Fix first two elements with nested loops
- Use **Two Pointers** for the remaining two
- Skip duplicates at each level

### Java Solution

```java
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j-1]) continue;
                int left = j + 1, right = n - 1;
                while (left < right) {
                    long sum = (long)nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        while (left < right && nums[left] == nums[left+1]) left++;
                        while (left < right && nums[right] == nums[right-1]) right--;
                        left++; right--;
                    } else if (sum < target) left++;
                    else right--;
                }
            }
        }
        return result;
    }
}
```

**Complexity:** Time O(n³) · Space O(1) excluding output

---

## Longest Consecutive Sequence

**LeetCode 128** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/longest-consecutive-sequence/)

### Problem
Find the length of the longest consecutive elements sequence. Must be O(n).

### Approach

- Add all elements to a **HashSet**
- For each number, check if it's the **start of a sequence** (`num-1` not in set)
- Count consecutive elements from there

### Java Solution

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int n : nums) set.add(n);

        int maxLen = 0;
        for (int n : set) {
            if (!set.contains(n - 1)) { // n is sequence start
                int len = 1;
                while (set.contains(n + len)) len++;
                maxLen = Math.max(maxLen, len);
            }
        }
        return maxLen;
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---

## Largest Subarray with Zero Sum

**Problem:** Find the length of the largest subarray with sum = 0.

### Approach (Prefix Sum + HashMap)

- `prefixSum[i]` = sum of elements from index 0 to i
- If `prefixSum[i] == prefixSum[j]` for i < j, then subarray `(i+1, j)` has sum 0
- Store **first occurrence** of each prefix sum in a map
- If prefix sum repeats → update max length

### Java Solution

```java
public int maxLen(int[] arr) {
    Map<Integer, Integer> map = new HashMap<>();
    map.put(0, -1);
    int maxLen = 0, sum = 0;

    for (int i = 0; i < arr.length; i++) {
        sum += arr[i];
        if (map.containsKey(sum)) {
            maxLen = Math.max(maxLen, i - map.get(sum));
        } else {
            map.put(sum, i);
        }
    }
    return maxLen;
}
```

**Complexity:** Time O(n) · Space O(n)

---

## Count Subarrays with XOR = k

**Problem:** Count subarrays whose XOR equals k.

### Approach (Prefix XOR + HashMap)

- Like prefix sum but with XOR
- `XOR(i, j) = prefXOR[j] ^ prefXOR[i-1]`
- If `prefXOR[j] ^ k = prefXOR[i-1]` → subarray XOR = k
- Store frequency of each prefix XOR in map

### Java Solution

```java
public int countSubarraysWithXOR(int[] arr, int k) {
    Map<Integer, Integer> map = new HashMap<>();
    map.put(0, 1);
    int prefXOR = 0, count = 0;

    for (int num : arr) {
        prefXOR ^= num;
        count += map.getOrDefault(prefXOR ^ k, 0);
        map.put(prefXOR, map.getOrDefault(prefXOR, 0) + 1);
    }
    return count;
}
```

**Complexity:** Time O(n) · Space O(n)

---

## Longest Subarray with Sum K

**Problem:** Find the longest subarray with sum equal to k. Array can have negatives.

### Approach (Prefix Sum + HashMap)

- `prefixSum[i] - k = prefixSum[j]` → subarray `(j+1, i)` has sum k
- Store first occurrence of each prefix sum

### Java Solution

```java
public int longestSubarrayWithSumK(int[] arr, int k) {
    Map<Integer, Integer> map = new HashMap<>();
    map.put(0, -1);
    int sum = 0, maxLen = 0;

    for (int i = 0; i < arr.length; i++) {
        sum += arr[i];
        if (map.containsKey(sum - k))
            maxLen = Math.max(maxLen, i - map.get(sum - k));
        if (!map.containsKey(sum))  // store only first occurrence
            map.put(sum, i);
    }
    return maxLen;
}
```

> **If array has only non-negative numbers:** Use two-pointer sliding window instead (O(n) no extra space).

**Complexity:** Time O(n) · Space O(n)

---

## The Prefix Sum Pattern — Master Template

```
Problem type         → Technique
─────────────────────────────────────────────
Sum = k              → prefixSum + HashMap
XOR = k              → prefixXOR + HashMap
Zero sum subarray    → prefixSum + HashMap (first occurrence)
Max length subarray  → prefixSum + HashMap (first occurrence)
Count subarrays      → prefixSum + HashMap (frequency count)
```

---

## Interview Tips for Arrays IV

> 💡 **Prefix Sum + HashMap** solves a huge class of subarray problems
> 💡 **Always handle long for 4-sum** to avoid integer overflow
> 💡 **HashSet start-detection trick** enables O(n) consecutive sequence

#sde-sheet #arrays #day4 #prefix-sum #hashmap
