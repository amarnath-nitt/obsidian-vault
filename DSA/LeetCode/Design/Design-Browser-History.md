# Design Browser History

**LeetCode Problem:** [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/)  
**Difficulty:** Medium  
**Topic:** Design, Stack, Doubly Linked List, Array

---

## Problem Statement

You have a **browser** of one tab where you start on the `homepage` and you can visit another `url`, get back in the history number of `steps` or move forward in the history number of `steps`.

Implement the `BrowserHistory` class:

- `BrowserHistory(string homepage)` Initializes the object with the `homepage` of the browser.
- `void visit(string url)` Visits `url` from the current page. It clears up all the forward history.
- `string back(int steps)` Move `steps` back in history. If you can only return `x` steps in the history and `steps > x`, you will return only `x` steps. Return the current `url` after moving back in history **at most** `steps`.
- `string forward(int steps)` Move `steps` forward in history. If you can only forward `x` steps in the history and `steps > x`, you will forward only `x` steps. Return the current `url` after forwarding in history **at most** `steps`.

---

## Examples

### Example 1:
```
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
```

---

## Approach 1: Two Stacks

### Key Insights:
1.  **History Stack**: Stores past URLs (back button).
2.  **Forward Stack**: Stores future URLs (forward button).
3.  **Visit**: Push current to History, clear Forward, update Current.
4.  **Back**: Pop from History, Push to Forward.
5.  **Forward**: Pop from Forward, Push to History.

This is a classic way to implement Undo/Redo operations.

---

## Java Implementation - Approach 1 (Two Stacks)

```java
class BrowserHistory {
    private Stack<String> history;
    private Stack<String> forward;
    private String current;

    public BrowserHistory(String homepage) {
        history = new Stack<>();
        forward = new Stack<>();
        current = homepage;
    }
    
    public void visit(String url) {
        history.push(current);
        current = url;
        forward.clear(); // Clear forward history
    }
    
    public String back(int steps) {
        while (steps > 0 && !history.isEmpty()) {
            forward.push(current);
            current = history.pop();
            steps--;
        }
        return current;
    }
    
    public String forward(int steps) {
        while (steps > 0 && !forward.isEmpty()) {
            history.push(current);
            current = forward.pop();
            steps--;
        }
        return current;
    }
}
```

**Pros**: Intuitive, uses standard data structures.
**Cons**: `visit` clearing forward stack is O(N) if we strictly follow stack API (though `Stack.clear()` is fast). Moving `steps` takes O(steps) time.

---

## Approach 2: Doubly Linked List

### Key Insights:
1.  **Nodes**: Each URL is a node.
2.  **Current Pointer**: Points to current node.
3.  **Visit**: Create new node, link `current.next` to it (dropping old `next` chain), move `current`.
4.  **Back/Forward**: Traverse pointers.

---

## Java Implementation - Approach 2 (Doubly Linked List)

```java
class BrowserHistory {
    class Node {
        String url;
        Node prev, next;
        Node(String url) { this.url = url; }
    }
    
    private Node current;

    public BrowserHistory(String homepage) {
        current = new Node(homepage);
    }
    
    public void visit(String url) {
        Node newNode = new Node(url);
        current.next = newNode;
        newNode.prev = current;
        current = newNode; // Move to new page
    }
    
    public String back(int steps) {
        while (steps > 0 && current.prev != null) {
            current = current.prev;
            steps--;
        }
        return current.url;
    }
    
    public String forward(int steps) {
        while (steps > 0 && current.next != null) {
            current = current.next;
            steps--;
        }
        return current.url;
    }
}
```

**Complexity**: O(1) for visit, O(steps) for back/forward.

---

## Approach 3: Dynamic Array (ArrayList) - Optimized

### Key Insights:
1.  **Single List**: Use an `ArrayList` to store linear history.
2.  **Pointer**: `currentIndex` tracks where we are.
3.  **Boundary**: `lastIndex` tracks the effective end of history (since `visit` overwrites forward history).
4.  **Visit**: Overwrite next index if exists, or add to end. Update `lastIndex`.
5.  **Back/Forward**: Simple index math. `Math.min` / `Math.max`.

This is the most efficient approach because `back` and `forward` become O(1) mathematical operations rather than loops.

---

## Java Implementation - Approach 3 (ArrayList)

```java
class BrowserHistory {
    private ArrayList<String> history;
    private int current; // current index
    private int total;   // total valid history length

    public BrowserHistory(String homepage) {
        history = new ArrayList<>();
        history.add(homepage);
        current = 0;
        total = 1;
    }
    
    public void visit(String url) {
        if (history.size() > current + 1) {
            // Overwrite existing slot
            history.set(current + 1, url);
        } else {
            // Add new slot
            history.add(url);
        }
        current++;
        total = current + 1; // Clear forward history by setting limit
    }
    
    public String back(int steps) {
        current = Math.max(0, current - steps);
        return history.get(current);
    }
    
    public String forward(int steps) {
        current = Math.min(total - 1, current + steps);
        return history.get(current);
    }
}
```

---

## Complexity Analysis (ArrayList Approach)

### Time Complexity:
-   **visit(url)**: O(1) - Adding to end or setting index is O(1).
-   **back(steps)**: O(1) - Direct index calculation.
-   **forward(steps)**: O(1) - Direct index calculation.

### Space Complexity:
-   **O(N)**: Stores history of size N.

---

## Key Points for Interviews

1.  **Why ArrayList is Best?**
    -   O(1) back/forward is superior to O(steps) in Stack/LinkedList approaches.
    -   We don't literally need to "delete" the forward history in memory, just maintain a pointer to the valid `total` size.

2.  **Memory Management:**
    -   In the ArrayList approach, "cleared" forward history might still linger in the list until overwritten. In Java, this holds references to Strings. If memory is tight, we might want to manually clear or use `.subList().clear()` (though that might be O(N)).

3.  **Edge Cases:**
    -   Back more steps than available.
    -   Forward more steps than available.
    -   Visit after Back (truncates forward).

---

## Related Problems

-   [Min Stack](https://leetcode.com/problems/min-stack/)
-   [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

---

## Tags

`#design` `#array` `#stack` `#linked-list` `#medium`
