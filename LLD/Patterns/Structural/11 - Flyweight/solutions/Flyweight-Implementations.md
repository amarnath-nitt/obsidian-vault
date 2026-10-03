# Flyweight — Implementations & Examples

**Pattern:** Flyweight (Structural) · **Skill:** sharing intrinsic state to save memory

### Approach

- Split state into **intrinsic** (shared, immutable) and **extrinsic** (per-object).
- Put intrinsic state in an immutable **Flyweight**.
- Cache flyweights in a **Factory** keyed by intrinsic state.
- Clients keep the extrinsic state and pass it to the flyweight's operation.

### Java Solutions

**1. Forest with Shared TreeTypes**
```java
import java.util.*;

final class TreeType {                                   // Flyweight (intrinsic, immutable)
    private final String name, color, texture;
    TreeType(String name, String color, String texture) {
        this.name = name; this.color = color; this.texture = texture;
    }
    void draw(int x, int y) {                            // extrinsic passed in
        System.out.println("🌳 " + name + " (" + color + "/" + texture + ") at " + x + "," + y);
    }
}

class TreeTypeFactory {                                  // FlyweightFactory
    private static final Map<String, TreeType> CACHE = new HashMap<>();
    static TreeType get(String name, String color, String texture) {
        return CACHE.computeIfAbsent(name, k -> new TreeType(name, color, texture));
    }
    static int cacheSize() { return CACHE.size(); }
}

class Tree {                                             // Context (extrinsic state)
    private final int x, y;
    private final TreeType type;
    Tree(int x, int y, TreeType type) { this.x = x; this.y = y; this.type = type; }
    void draw() { type.draw(x, y); }
}

// usage — 1,000,000 trees, but only 2 TreeType objects
List<Tree> forest = new ArrayList<>();
for (int i = 0; i < 1_000_000; i++) {
    TreeType oak = TreeTypeFactory.get("Oak",  "green", "rough");
    forest.add(new Tree(i % 1000, i / 1000, oak));
}
System.out.println("Shared flyweights: " + TreeTypeFactory.cacheSize());  // 1
```

**2. Chess Pieces (types shared, position extrinsic)**
```java
import java.util.*;

enum Color { WHITE, BLACK }

final class PieceType {                                  // flyweight: intrinsic (kind + color)
    private final String kind; private final Color color;
    PieceType(String kind, Color color) { this.kind = kind; this.color = color; }
    String render() { return color + " " + kind; }
}
class PieceTypeFactory {
    private static final Map<String, PieceType> CACHE = new HashMap<>();
    static PieceType get(String kind, Color color) {
        return CACHE.computeIfAbsent(color + kind, k -> new PieceType(kind, color));
    }
}
class Piece {                                            // extrinsic: board position
    private final PieceType type; private int row, col;
    Piece(PieceType t, int row, int col) { type = t; this.row = row; this.col = col; }
    void moveTo(int r, int c) { row = r; col = c; }
    String describe() { return type.render() + "@" + row + "," + col; }
}
```

**3. Text Glyph Styles**
```java
import java.util.*;

final class TextStyle {                                  // intrinsic: font/size/colour
    private final String font; private final int size; private final String color;
    TextStyle(String f, int s, String c) { font = f; size = s; color = c; }
    void print(char ch) { System.out.printf("[%s %d %s]%c", font, size, color, ch); }
}
class TextStyleFactory {
    private static final Map<String, TextStyle> CACHE = new HashMap<>();
    static TextStyle get(String f, int s, String c) {
        return CACHE.computeIfAbsent(f + s + c, k -> new TextStyle(f, s, c));
    }
}
class Glyph {                                            // extrinsic: char + position
    private final char ch; private final TextStyle style;
    Glyph(char ch, TextStyle style) { this.ch = ch; this.style = style; }
    void draw() { style.print(ch); }
}
```

**4. JDK Flyweights (for the interview)**
```java
Integer a = Integer.valueOf(127), b = Integer.valueOf(127);
System.out.println(a == b);                 // true — same cached flyweight (-128..127)

String s1 = "hi", s2 = "hi";
System.out.println(s1 == s2);               // true — interned in the String pool
```

**Complexity:** lookup O(1) · Space O(number of distinct intrinsic states), not O(number of objects)

**Design note:** the payoff is dramatic when objects vastly outnumber distinct *types* — e.g. 1M trees but 2 flyweights.