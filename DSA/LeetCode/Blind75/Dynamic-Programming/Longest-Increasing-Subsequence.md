# Longest Increasing Subsequence

**Difficulty:** Medium  
**Category:** Dynamic Programming  
**LeetCode Link:** [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

---

## Approach: DP

### Java Code
```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        int maxLen = 1;
        
        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxLen = Math.max(maxLen, dp[i]);
        }
        
        return maxLen;
    }
}
```

### Complexity
- **Time:** O(n²)
- **Space:** O(n)

---

## Tags
#dynamic-programming #medium #blind75

---

## Visualization

- Embed: `![](../assets/longest-increasing-subsequence/step-1.svg)`
- Obsidian embed: `![[../assets/longest-increasing-subsequence/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="140">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <text x="20" y="28" fill="#222">LIS patience piles visualization</text>
    <g transform="translate(20,50)">
        <rect x="0" y="0" width="30" height="60" fill="#ffd59e" stroke="#e29a2f"/>
        <rect x="40" y="20" width="30" height="40" fill="#bfe7c6" stroke="#57b86b"/>
        <rect x="80" y="40" width="30" height="20" fill="#9ad0f5" stroke="#4b9be6"/>
    </g>
</svg>
