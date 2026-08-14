# Subarray Sums Divisible by K (LC 974)

**Difficulty**: Medium  
**Pattern**: Prefix Sum / HashMap  
**LeetCode**: https://leetcode.com/problems/subarray-sums-divisible-by-k/

## Problem Statement
Given an integer array `nums` and an integer `k`, return the number of non-empty subarrays that have a sum divisible by `k`.

**Example:**
```
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
```

## Approach: Prefix Sum with Modulo

### Intuition
`Sum(i...j) % k == 0` means `(PrefixSum[j] - PrefixSum[i-1]) % k == 0`.
So `PrefixSum[j] % k == PrefixSum[i-1] % k`.
We just need to count how many times each remainder `0...k-1` appears.
Important: Java `%` operator can return negative. `rem = (rem % k + k) % k` to handle negatives.

### Java Code
```java
class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>(); // Remainder -> Count
        map.put(0, 1); // Base case
        
        int sum = 0;
        int count = 0;
        
        for (int num : nums) {
            sum += num;
            int rem = sum % k;
            if (rem < 0) rem += k; // Handle negative remainder
            
            if (map.containsKey(rem)) {
                count += map.get(rem);
            }
            
            map.put(rem, map.getOrDefault(rem, 0) + 1);
        }
        
        return count;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(K) (Since remainders are 0 to K-1)

## Key Takeaways
- Modulo arithmetic with Prefix Sum
- Handling negative mod results
