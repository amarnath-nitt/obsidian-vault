# Top K Frequent Elements

**Difficulty:** Medium  
**Category:** Arrays & Hashing  
**LeetCode Link:** [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Example 1:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`
- It is guaranteed that the answer is unique.

**Follow up:** Your algorithm's time complexity must be better than O(n log n).

---

## Intuition

We need to find the k elements that appear most frequently. This requires counting frequencies and then selecting the top k.

---

## Approach 1: Sort by Frequency (Naive Solution)

### Algorithm
1. Count frequency of each element using HashMap
2. Convert map entries to a list
3. Sort by frequency in descending order
4. Take first k elements

### Java Code
```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Count frequencies
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }
        
        // Convert to list and sort by frequency
        List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(freqMap.entrySet());
        entries.sort((a, b) -> b.getValue() - a.getValue());
        
        // Extract top k elements
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = entries.get(i).getKey();
        }
        
        return result;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n log n) - Sorting dominates
- **Space Complexity:** O(n) - HashMap and list

### Drawbacks
- Sorting is expensive
- Doesn't meet the follow-up requirement

---

## Approach 2: Min Heap (Better Solution)

### Algorithm
1. Count frequencies using HashMap
2. Use a min heap of size k
3. For each element, add to heap
4. If heap size > k, remove minimum
5. Heap contains k most frequent elements

### Java Code
```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Count frequencies
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }
        
        // Min heap based on frequency
        PriorityQueue<Integer> heap = new PriorityQueue<>(
            (a, b) -> freqMap.get(a) - freqMap.get(b)
        );
        
        // Add elements to heap, keep size = k
        for (int num : freqMap.keySet()) {
            heap.offer(num);
            if (heap.size() > k) {
                heap.poll(); // Remove least frequent
            }
        }
        
        // Extract result
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = heap.poll();
        }
        
        return result;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n log k) - Heap operations for n elements
- **Space Complexity:** O(n) - HashMap and heap

---

## Approach 3: Bucket Sort (Optimized Solution)

### Algorithm
1. Count frequencies using HashMap
2. Create buckets where index = frequency
3. Place elements in corresponding frequency buckets
4. Iterate buckets from high to low frequency
5. Collect k elements

### Java Code
```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Count frequencies
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }
        
        // Bucket sort: index = frequency, value = list of numbers
        List<Integer>[] buckets = new List[nums.length + 1];
        for (int num : freqMap.keySet()) {
            int freq = freqMap.get(num);
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(num);
        }
        
        // Collect top k from highest frequency buckets
        int[] result = new int[k];
        int index = 0;
        
        // Iterate from highest frequency to lowest
        for (int i = buckets.length - 1; i >= 0 && index < k; i--) {
            if (buckets[i] != null) {
                for (int num : buckets[i]) {
                    result[index++] = num;
                    if (index == k) {
                        return result;
                    }
                }
            }
        }
        
        return result;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Linear passes through data
- **Space Complexity:** O(n) - HashMap and buckets array

### Why This is Better
- ✅ O(n) time complexity - meets follow-up requirement
- ✅ No sorting or heap operations needed
- ✅ Leverages the constraint that frequency ≤ n
- ✅ Bucket sort is perfect when range is limited

---

## Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sorting | O(n log n) | O(n) | Simple but slow |
| Min Heap | O(n log k) | O(n) | Good when k is small |
| Bucket Sort | O(n) | O(n) | Optimal solution |

---

## Key Takeaways

1. **Pattern:** Bucket sort works when values have limited range
2. **Frequency constraint:** Max frequency = array length
3. **Heap optimization:** Min heap of size k is better than sorting all
4. **Trade-offs:** Bucket sort trades space for optimal time
5. **Follow-up awareness:** Always check if there's a better complexity requirement

---

## Edge Cases

- Single element: `nums = [1], k = 1` → `[1]`
- All same frequency: `nums = [1,2,3], k = 2` → any 2 elements
- All same element: `nums = [1,1,1], k = 1` → `[1]`

---

## Related Problems
- [[Kth-Largest-Element]] - Similar heap usage
- [[Sort-Characters-By-Frequency]] - Similar frequency sorting
- [[Top-K-Frequent-Words]] - String version

---

## Tags
#arrays #hashing #heap #bucket-sort #medium #blind75

---

## Visualization

- Embed: `![](../assets/top-k-frequent/step-1.svg)`
- Obsidian embed: `![[../assets/top-k-frequent/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="140">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <text x="20" y="28" fill="#222">Top-K Frequent Elements (freq buckets)</text>
    <g transform="translate(20,50)">
        <rect x="0" y="10" width="60" height="20" fill="#ffd59e" stroke="#e29a2f"/>
        <text x="30" y="26" text-anchor="middle">1</text>
        <rect x="80" y="10" width="60" height="20" fill="#bfe7c6" stroke="#57b86b"/>
        <text x="110" y="26" text-anchor="middle">2</text>
        <rect x="160" y="10" width="60" height="20" fill="#9ad0f5" stroke="#4b9be6"/>
        <text x="190" y="26" text-anchor="middle">3</text>
    </g>
</svg>
