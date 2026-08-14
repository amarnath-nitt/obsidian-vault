# String Manipulation

**Concept tested**: `flatMap`, `distinct`, `joining`

## Problem
From a list of sentences, get unique words, convert them to uppercase, and join with commas.

## Solution
```java
List<String> sentences = Arrays.asList("hello world", "java programming", "hello java");

String result = sentences.stream()
    .flatMap(sentence -> Arrays.stream(sentence.split(" ")))
    .distinct()
    .map(String::toUpperCase)
    .collect(Collectors.joining(", "));
```

## Complexity
- **Time**: O(n), assuming average word length is bounded
- **Space**: O(k), where `k` is the number of unique words

## Interview Explanation
Split each sentence into words, flatten all words into one stream, remove duplicates, transform to uppercase, and join into a single string.
