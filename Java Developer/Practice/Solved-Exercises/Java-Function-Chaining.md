# Function Chaining

**Concept tested**: `Function.andThen`

## Problem
Create a pipeline: trim, uppercase, add prefix.

## Solution
```java
Function<String, String> trim = String::trim;
Function<String, String> upper = String::toUpperCase;
Function<String, String> addPrefix = s -> "Hello, " + s;

Function<String, String> pipeline = trim.andThen(upper).andThen(addPrefix);

String result = pipeline.apply("  alice  ");
```

## Complexity
- **Time**: O(n), where `n` is string length
- **Space**: O(n)

## Interview Explanation
`andThen` runs functions from left to right. This keeps each transformation small and readable.
