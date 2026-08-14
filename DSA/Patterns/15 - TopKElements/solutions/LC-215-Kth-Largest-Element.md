# Kth Largest Element in an Array (LC 215)

**Difficulty**: Medium  
**Pattern**: Top 'K' Elements  
**LeetCode**: https://leetcode.com/problems/kth-largest-element-in-an-array/

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.
Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

**Example 1:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2:**
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## Approach 1: Sorting (Brute Force)

### Java Code
```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
    }
}
```

### Complexity
- **Time**: O(n log n)
- **Space**: O(1) or O(log n) dependent on sort implementation

## Approach 2: Min-Heap (Optimized for Stream)

### Intuition
Keep a Min-Heap of size k. The heap will store the k largest elements seen so far. The root of the heap is the smallest among the top k (which is the kth largest).

### Java Code
```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        for (int num : nums) {
            minHeap.add(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        
        return minHeap.peek();
    }
}
```

### Complexity
- **Time**: O(n log k)
- **Space**: O(k)

## Approach 3: QuickSelect (Best Average Time)

### Intuition
Use the partitioning logic from QuickSort. Pick a pivot, partition array such that elements >= pivot are on left, < pivot on right. The pivot ends up in its final sorted position. Recursively partition only the relevant half.

### Java Code
```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        // Convert k to 0-based index in sorted array (0 = largest, n-1 = smallest)
        // Or easier: find (n-k)th smallest
        int targetIndex = nums.length - k;
        return quickSelect(nums, 0, nums.length - 1, targetIndex);
    }
    
    private int quickSelect(int[] nums, int left, int right, int k) {
        if (left == right) return nums[left];
        
        Random rand = new Random();
        int pivotIndex = left + rand.nextInt(right - left + 1);
        
        pivotIndex = partition(nums, left, right, pivotIndex);
        
        if (k == pivotIndex) {
            return nums[k];
        } else if (k < pivotIndex) {
            return quickSelect(nums, left, pivotIndex - 1, k);
        } else {
            return quickSelect(nums, pivotIndex + 1, right, k);
        }
    }
    
    private int partition(int[] nums, int left, int right, int pivotIndex) {
        int pivot = nums[pivotIndex];
        swap(nums, pivotIndex, right);
        int storeIndex = left;
        
        for (int i = left; i < right; i++) {
            if (nums[i] < pivot) {
                swap(nums, storeIndex, i);
                storeIndex++;
            }
        }
        
        swap(nums, storeIndex, right);
        return storeIndex;
    }
    
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

### Complexity
- **Time**: Average O(n), Worst case O(n²)
- **Space**: O(1) iterative or O(log n) recursive stack

## Key Takeaways
- Min-Heap is excellent for "Top K" problems (O(n log k))
- QuickSelect is faster on average (O(n)) but trickier to implement
- Sorting is easiest but suboptimal for large N
