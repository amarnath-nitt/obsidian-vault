# Java Stream Creation Guide

This guide covers the common stream-creation options in the Java standard library. Choose the source type that matches your data; a stream is single-use, so create a new one for each independent pipeline.

```java
import java.io.BufferedReader;
import java.nio.CharBuffer;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.regex.MatchResult;
import java.util.regex.Pattern;
import java.util.stream.*;
```

## Object Values and Object Arrays

```java
Stream<String> values = Stream.of("a", "b", "c");
Stream<String> oneNullableValue = Stream.ofNullable(findName()); // Java 9+
Stream<String> empty = Stream.empty();

String[] names = {"Ada", "Lin", "Mia"};
Stream<String> fromArray = Arrays.stream(names);
Stream<String> partOfArray = Arrays.stream(names, 1, 3);
Stream<String> fromArrayWithOf = Stream.of(names);
```

`Stream.of(names)` and `Arrays.stream(names)` both create a `Stream<String>` for an object array. In contrast, `Stream.of(chars)` where `chars` is a `char[]` creates a `Stream<char[]>` containing one array—not a stream of characters.

## Collections, Maps, and Optional

```java
List<Integer> numbers = List.of(1, 2, 3);
Stream<Integer> fromList = numbers.stream();

Set<String> tags = Set.of("java", "spring");
Stream<String> fromSet = tags.stream();

Map<Long, String> users = Map.of(1L, "Ada", 2L, "Lin");
Stream<Map.Entry<Long, String>> entries = users.entrySet().stream();
Stream<Long> keys = users.keySet().stream();
Stream<String> mapValues = users.values().stream();

Optional<String> name = Optional.of("Ada");
Stream<String> optionalValue = name.stream(); // Java 9+
```

Use `parallelStream()` only after measuring a CPU-bound, stateless operation on sufficiently large data. It is not a default performance switch.

## Primitive Streams and Primitive Arrays

```java
IntStream ints = IntStream.of(1, 2, 3);
LongStream longs = LongStream.of(10L, 20L);
DoubleStream doubles = DoubleStream.of(1.5, 2.5);

int[] intArray = {1, 2, 3};
long[] longArray = {10L, 20L};
double[] doubleArray = {1.5, 2.5};

IntStream fromInts = Arrays.stream(intArray);
LongStream fromLongs = Arrays.stream(longArray);
DoubleStream fromDoubles = Arrays.stream(doubleArray);
```

Java provides `Arrays.stream` overloads for `int[]`, `long[]`, and `double[]`, but not for `char[]`, `byte[]`, `short[]`, `float[]`, or `boolean[]`.

Convert a primitive stream to an object stream only when necessary:

```java
Stream<Integer> boxed = IntStream.of(1, 2, 3).boxed();
Stream<String> labels = IntStream.of(1, 2, 3).mapToObj(n -> "item-" + n);
```

## `char[]`, Strings, and Unicode

```java
char[] chars = {'a', 'b', 'c'};

// Simplest: String.chars() returns an IntStream of UTF-16 code units.
IntStream charCodes = new String(chars).chars();
Stream<Character> characterStream = new String(chars)
        .chars()
        .mapToObj(codeUnit -> (char) codeUnit);

// Avoid creating a String: CharBuffer wraps the existing char array.
Stream<Character> fromCharBuffer = CharBuffer.wrap(chars)
        .chars()
        .mapToObj(codeUnit -> (char) codeUnit);

String text = "Java";
IntStream utf16CodeUnits = text.chars();
IntStream unicodeCodePoints = text.codePoints();
```

Use `chars()` for `char`/UTF-16 code-unit questions such as interview inputs with English letters. Use `codePoints()` when real Unicode characters outside the Basic Multilingual Plane must be handled correctly; a code point cannot always fit in one `char` or `Character`.

## Generated, Iterated, and Ranged Streams

```java
Stream<UUID> ids = Stream.generate(UUID::randomUUID); // infinite
Stream<Double> randomValues = Stream.generate(Math::random); // infinite

Stream<Integer> powersOfTwo = Stream.iterate(1, n -> n * 2); // infinite
Stream<Integer> bounded = Stream.iterate(1, n -> n <= 100, n -> n + 1); // Java 9+

IntStream zeroToNine = IntStream.range(0, 10);       // 0..9
IntStream oneToTen = IntStream.rangeClosed(1, 10);   // 1..10
```

Always bound an infinite stream with a terminal condition or `limit`:

```java
List<UUID> firstThree = Stream.generate(UUID::randomUUID)
        .limit(3)
        .toList(); // Java 16+
```

## Builder, Concatenation, and Custom Sources

```java
Stream<String> built = Stream.<String>builder()
        .add("created")
        .add("validated")
        .build();

Stream<String> combined = Stream.concat(
        Stream.of("a", "b"),
        Stream.of("c", "d")
);

Spliterator<String> spliterator = List.of("a", "b", "c").spliterator();
Stream<String> customSource = StreamSupport.stream(spliterator, false);
```

Use `Stream.builder()` when values are discovered imperatively before the pipeline begins. Use `StreamSupport.stream` when adapting a custom `Spliterator` or library source.

## I/O and Regular Expressions

Resources that open files or readers must be closed.

```java
Path path = Path.of("application.log");
try (Stream<String> lines = Files.lines(path)) {
    long errors = lines.filter(line -> line.contains("ERROR")).count();
}

try (BufferedReader reader = Files.newBufferedReader(path)) {
    long linesRead = reader.lines().count();
}

Stream<String> words = Pattern.compile("\\s+").splitAsStream("Java streams are lazy");
```

For a directory traversal, also use try-with-resources:

```java
try (Stream<Path> files = Files.walk(Path.of("src"))) {
    List<Path> javaFiles = files
            .filter(file -> file.toString().endsWith(".java"))
            .toList();
}
```

## Other Useful JDK Sources

```java
Stream<String> textLines = "one\ntwo\nthree".lines(); // Java 11+

Stream<MatchResult> matches = Pattern.compile("\\w+")
        .matcher("Java 25")
        .results(); // Java 9+

Random random = new Random();
IntStream randomInts = random.ints(5, 1, 101); // five values: 1..100
LongStream randomLongs = random.longs().limit(10);
DoubleStream randomDoubles = random.doubles(10);

BitSet enabledFeatures = BitSet.valueOf(new long[] {0b10101});
IntStream enabledIndexes = enabledFeatures.stream();

try (Stream<Path> children = Files.list(Path.of("src"))) {
    long childCount = children.count();
}

try (Stream<Path> matchesByPath = Files.find(
        Path.of("src"),
        10,
        (path, attributes) -> path.toString().endsWith(".java"))) {
    long javaFileCount = matchesByPath.count();
}
```

`String.lines()` is useful for in-memory text, whereas `Files.lines()` reads lazily from a file. `Files.list`, `Files.find`, and `Files.walk` all own resources and must be closed.

## Frequent Interview Pitfalls

| Situation | Correct answer |
|---|---|
| `Arrays.stream(charArray)` | Does not compile; there is no `char[]` overload. |
| `Stream.of(charArray)` | Produces one `char[]` element, not characters. |
| `new String(chars).chars()` | Produces `IntStream`, so use `mapToObj(value -> (char) value)` for `Stream<Character>`. |
| Reusing a stream after `count()` | Invalid; a stream is consumed after a terminal operation. |
| `Files.lines(path)` | Must be closed with try-with-resources. |
| Calling `parallelStream()` by default | Usually a mistake; measure and understand ordering, thread use, and blocking behavior first. |
