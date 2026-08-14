# Flatten Nested List Iterator (LC 341)

**Difficulty**: Medium  
**Pattern**: Recursion / Stack  
**LeetCode**: https://leetcode.com/problems/flatten-nested-list-iterator/

## Problem Statement
Implement an iterator over a nested list of integers.

## Approach: Recursive Pre-Flatten
Walk through the nested list once. If the item is an integer, add it. Otherwise, recursively flatten its list.

## Intuition: Recursion vs Lazy Evaluation

### Approach 1: Recursive Pre-Flatten (Simple)
Walk through the **ENTIRE nested list at construction time**, flattening into a single flat list.

**Algorithm:**
```
function flatten(nestedList):
    for each item in nestedList:
        if item is an integer:
            add it to values
        else:
            recursively flatten item.getList()
```

**Pros:**
- Simple to implement and understand
- `next()` and `hasNext()` are trivial (just array operations)
- Debugging is straightforward

**Cons:**
- Must load ALL integers into memory upfront
- If the nested list is huge, initialization is slow/memory-intensive
- If you only iterate partially, you wasted work

**Complexity:**
- Time: O(n) to flatten all integers initially
- Space: O(n) to store all integers

### Approach 2: Lazy Stack Iterator (Efficient)
Keep a stack of iterators. Only expand nested lists when `hasNext()` needs the next value.

**Algorithm:**
```
Push iterator of nestedList onto stack
When hasNext() called:
    while stack not empty:
        current = stack.peek()
        if current.hasNext():
            item = current.next()
            if item is integer:
                return it (nextValue found!)
            else:
                push item.getList().iterator() onto stack
        else:
            pop from stack

```

**Pros:**
- On-demand expansion: only materializes values you actually use
- Memory-efficient if you don't iterate the full list
- Better performance if iteration stops early

**Cons:**
- More complex state management (stack of iterators)
- Need to understand iterator pattern
- Debugging is harder (abstract stack representation)

**Complexity:**
- Time: O(n) amortized (each element examined once)
- Space: O(d) where d is maximum nesting depth

### When to Use Which

**Use Pre-Flatten if:**
- Simplicity matters (interview soft skills: clear code)
- The nested list isn't too large
- You'll iterate the full list anyway
- Time pressure in interview

**Use Lazy Iterator if:**
- Interviewer emphasizes efficiency
- The nested list could be massive
- You want to show advanced patterns and optimization awareness
- Partial iteration is expected

### Interview Tip
In an actual interview, you might say:
> "I'll start with the pre-flatten approach for clarity. For production, I'd optimize with lazy evaluation 
> using a stack of iterators to handle massive nested structures without loading everything upfront."

This shows both pragmatism and optimization awareness.

## Java Code
```java
public class NestedIterator implements Iterator<Integer> {
    private final List<Integer> values = new ArrayList<>();
    private int index = 0;

    public NestedIterator(List<NestedInteger> nestedList) {
        flatten(nestedList);
    }

    private void flatten(List<NestedInteger> nestedList) {
        for (NestedInteger item : nestedList) {
            if (item.isInteger()) {
                values.add(item.getInteger());
            } else {
                flatten(item.getList());
            }
        }
    }

    @Override
    public Integer next() {
        return values.get(index++);
    }

    @Override
    public boolean hasNext() {
        return index < values.size();
    }
}
```

## Alternative Optimal Solution: Lazy Stack Iterator
Pre-flattening is simple, but it loads every integer up front. A stack-based iterator expands nested lists only when `hasNext()` needs another value.

```java
public class NestedIterator implements Iterator<Integer> {
    private final Deque<Iterator<NestedInteger>> stack = new ArrayDeque<>();
    private Integer nextValue = null;

    public NestedIterator(List<NestedInteger> nestedList) {
        stack.push(nestedList.iterator());
    }

    @Override
    public Integer next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        int value = nextValue;
        nextValue = null;
        return value;
    }

    @Override
    public boolean hasNext() {
        if (nextValue != null) {
            return true;
        }

        while (!stack.isEmpty()) {
            Iterator<NestedInteger> iterator = stack.peek();
            if (!iterator.hasNext()) {
                stack.pop();
                continue;
            }

            NestedInteger item = iterator.next();
            if (item.isInteger()) {
                nextValue = item.getInteger();
                return true;
            }
            stack.push(item.getList().iterator());
        }

        return false;
    }
}
```

### Alternative Complexity
- **Time**: O(1) amortized per `next()` / `hasNext()`
- **Space**: O(d), where `d` is the nesting depth

## Complexity
- **Time**: O(n), where `n` is the total count of nested integers
- **Space**: O(n)

## Key Takeaways
- Recursion naturally handles unknown nesting depth.
- Pre-flattening makes `next()` and `hasNext()` simple.
