# Add Two Numbers

**Difficulty:** Medium  
**Category:** Linked Lists  
**LeetCode Link:** [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

---

## Problem Statement

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

**Example 1:**
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
```

**Example 2:**
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

**Constraints:**
- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

---

## Intuition

Simulate addition digit by digit, tracking the carry. Since digits are in reverse order, we can add from left to right.

---

## Approach: Digit-by-Digit Addition with Carry

### Algorithm
1. Create dummy node for result
2. Traverse both lists simultaneously
3. Add corresponding digits + carry
4. Create new node with sum % 10
5. Update carry = sum / 10
6. Handle remaining carry at the end

### Java Code
```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carry = 0;
        
        while (l1 != null || l2 != null || carry > 0) {
            int sum = carry;
            
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            
            carry = sum / 10;
            current.next = new ListNode(sum % 10);
            current = current.next;
        }
        
        return dummy.next;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(max(m, n)) where m, n are list lengths
- **Space Complexity:** O(max(m, n)) for result list

---

## Key Takeaways

1. **Pattern:** Digit-by-digit processing with carry
2. **Reverse order:** Makes addition straightforward
3. **Handle unequal lengths:** Continue while either list exists
4. **Final carry:** Don't forget to add if carry remains

---

## Tags
#linked-lists #math #medium #blind75
