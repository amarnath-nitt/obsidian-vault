# Palindrome Linked List (LC 234)

**Difficulty**: Easy  
**Pattern**: Fast & Slow Pointers  
**LeetCode**: https://leetcode.com/problems/palindrome-linked-list/

## Problem Statement
Given the `head` of a singly linked list, return `true` if it is a palindrome, `false` otherwise.

**Example 1:**
```
Input: head = [1,2,2,1]
Output: true
```

**Example 2:**
```
Input: head = [1,2]
Output: false
```

## Approach 1: Convert to Array

### Intuition
Copy all values to an array, then use two pointers from both ends to check if it's a palindrome.

### Java Code
```java
class Solution {
    public boolean isPalindrome(ListNode head) {
        List<Integer> values = new ArrayList<>();
        
        // Copy to array
        ListNode current = head;
        while (current != null) {
            values.add(current.val);
            current = current.next;
        }
        
        // Two pointer check
        int left = 0, right = values.size() - 1;
        while (left < right) {
            if (!values.get(left).equals(values.get(right))) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) - Array storage

## Approach 2: Optimized (Fast & Slow + Reverse Second Half)

### Intuition
1. Use fast & slow pointers to find the middle
2. Reverse the second half of the list
3. Compare first half with reversed second half
4. (Optional) Restore the list

### Java Code
```java
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;
        
        // Step 1: Find middle using fast & slow pointers
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Step 2: Reverse second half
        ListNode secondHalf = reverseList(slow);
        ListNode firstHalf = head;
        
        // Step 3: Compare both halves
        ListNode p1 = firstHalf;
        ListNode p2 = secondHalf;
        boolean isPalin = true;
        
        while (p2 != null) {
            if (p1.val != p2.val) {
                isPalin = false;
                break;
            }
            p1 = p1.next;
            p2 = p2.next;
        }
        
        // Step 4: (Optional) Restore list
        // reverseList(secondHalf);
        
        return isPalin;
    }
    
    private ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        
        return prev;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

## Visual Walkthrough

```
Original: 1 → 2 → 2 → 1 → null

Step 1: Find middle
slow/fast: 1 → 2 → 2 → 1
                   ↑
                  slow

Step 2: Reverse from slow
First half: 1 → 2 → 2
Second half (reversed): 1 → 2

Step 3: Compare
1 = 1 ✓
2 = 2 ✓
Result: true
```

## Key Takeaways
- Fast & slow pointer finds middle in O(1) space
- In-place reversal of second half achieves O(1) space
- Handles both odd and even length lists
- Can restore original list structure if needed
- Combines two patterns: fast/slow + list reversal
