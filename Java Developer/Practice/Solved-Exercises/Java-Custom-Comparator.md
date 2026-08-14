# Custom Comparator

**Concept tested**: Comparator chaining

## Problem
Sort strings by length ascending, then alphabetically.

## Solution
```java
List<String> words = Arrays.asList("banana", "apple", "kiwi", "pear", "grape");

words.sort(
    Comparator.comparingInt(String::length)
              .thenComparing(String::compareTo)
);
```

## Complexity
- **Time**: O(n log n)
- **Space**: O(1) to O(n), depending on sort implementation

## Interview Explanation
The first comparator sorts by length. `thenComparing` is used as a tie-breaker when two strings have the same length.
