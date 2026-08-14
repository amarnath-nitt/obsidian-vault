# First Non-Repeated Character in a `char[]`

## Problem

Return the first character that occurs exactly once, while preserving the input order.

```java
char[] chars = {'a', 'b', 'c', 'a', 'd', 'b', 'e', 'f', 'a', 'c'};
// Expected result: d
```

## Key Interview Point: Create a Stream from `char[]`

`Arrays.stream(chars)` does not compile because Java has no `char[]` stream overload. `String.chars()` and `CharBuffer.chars()` both return an `IntStream` of UTF-16 code units, so convert each value to `char` before grouping.

## Solution: `String.chars()`

```java
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public static Character firstNonRepeated(char[] chars) {
    return new String(chars)
            .chars()                         // IntStream
            .mapToObj(value -> (char) value)  // Stream<Character>
            .collect(Collectors.groupingBy(
                    character -> character,
                    LinkedHashMap::new,
                    Collectors.counting()
            ))
            .entrySet()
            .stream()
            .filter(entry -> entry.getValue().equals(1L))
            .map(Map.Entry::getKey)
            .findFirst()
            .orElse(null);
}
```

```java
System.out.println(firstNonRepeated(chars)); // d
```

`LinkedHashMap` preserves the order in which each distinct character first appears. After counting, the first entry with count `1` is therefore the first non-repeated character.

## Alternative: No `String` Allocation

```java
import java.nio.CharBuffer;

Stream<Character> characterStream = CharBuffer.wrap(chars)
        .chars()
        .mapToObj(value -> (char) value);
```

The remaining grouping pipeline is identical.

## Complexity

- Time: **O(n)**
- Space: **O(k)**, where `k` is the number of distinct characters

## Interview Explanation

"I convert the `char[]` to an `IntStream` using `new String(chars).chars()`, then box each UTF-16 code unit as a `Character`. I count occurrences in a `LinkedHashMap` so first-occurrence order is retained, and return the first map entry with count one. I use `.equals(1L)` because `Collectors.counting()` produces `Long` values."

For the complete set of standard-library stream sources, see [Java Stream Creation Guide](../../Reference/Java-Stream-Creation-Guide.md).
