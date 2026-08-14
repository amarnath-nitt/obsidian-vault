# Fruit Into Baskets

[Problem Link](https://leetcode.com/problems/fruit-into-baskets/)

## Problem Statement
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `i`th tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
1.  You only have **two** baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
2.  Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
3.  Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array `fruits`, return the *maximum number of fruits you can pick*.

## Approach
This problem can be translated to finding the longest subarray with at most 2 distinct elements. We can use the sliding window technique.
1.  Use a Hash Map to keep track of the count of each fruit type in the current window.
2.  Expand the window by moving the `right` pointer.
3.  If the number of distinct fruits (map size) exceeds 2, shrink the window from the `left` until distinct fruits are back to 2 or less.
4.  Update the maximum length of the valid window.

## Time and Space Complexity
- **Time Complexity:** O(N), where N is the number of trees.
- **Space Complexity:** O(1), as the map will store at most 3 distinct fruit types.

## Code
```java
class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> countMap = new HashMap<>();
        int maxFruits = 0;
        int left = 0;
        
        for (int right = 0; right < fruits.length; right++) {
            // Add current fruit to the basket
            countMap.put(fruits[right], countMap.getOrDefault(fruits[right], 0) + 1);
            
            // If we have more than 2 types of fruits, shrink the window
            while (countMap.size() > 2) {
                int leftFruit = fruits[left];
                countMap.put(leftFruit, countMap.get(leftFruit) - 1);
                
                if (countMap.get(leftFruit) == 0) {
                    countMap.remove(leftFruit);
                }
                left++;
            }
            
            // Update maximum fruits collected
            maxFruits = Math.max(maxFruits, right - left + 1);
        }
        
        return maxFruits;
    }
}
```
