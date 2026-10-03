# Design Board Game Pieces

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Flyweight
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-board-game-pieces)

### Problem

A board game (e.g. chess/checkers) places many pieces on a board. Most pieces share the same
appearance — **colour**, **shape/symbol**, **image** — on thousands of squares. Storing that
appearance on every piece wastes memory. Share the appearance (**intrinsic** state) and keep only the
**position** (**extrinsic**) per piece.

### Approach — Flyweight

- **Intrinsic** (shared, immutable): piece type = colour + symbol.
- **Extrinsic** (per piece): row, column.
- A `PieceFlyweightFactory` caches types by key; pieces reference a shared type.

### Java Solution

```java
import java.util.*;

// Flyweight — intrinsic state (shared, immutable)
final class PieceType {
    private final String color;   // "white" / "black"
    private final String symbol;  // "K", "Q", "P", ...
    PieceType(String color, String symbol) { this.color = color; this.symbol = symbol; }

    String render(int row, int col) {           // extrinsic passed in
        return color.charAt(0) + symbol + "@" + row + "," + col;
    }
    @Override public String toString() { return color + " " + symbol; }
}

// FlyweightFactory — cache by intrinsic key
class PieceTypeFactory {
    private static final Map<String, PieceType> CACHE = new HashMap<>();
    static PieceType get(String color, String symbol) {
        return CACHE.computeIfAbsent(color + symbol, k -> new PieceType(color, symbol));
    }
    static int cacheSize() { return CACHE.size(); }
}

// Context — extrinsic state (position)
class Piece {
    private final PieceType type;
    private int row, col;
    Piece(PieceType type, int row, int col) { this.type = type; this.row = row; this.col = col; }

    void moveTo(int row, int col) { this.row = row; this.col = col; }
    String describe() { return type.render(row, col); }
}
```

**Usage**
```java
Board: place 32 pieces but only a handful of shared types
List<Piece> board = new ArrayList<>();
board.add(new Piece(PieceTypeFactory.get("white", "K"), 0, 4));
board.add(new Piece(PieceTypeFactory.get("white", "P"), 1, 0));
board.add(new Piece(PieceTypeFactory.get("black", "P"), 6, 0));

System.out.println(PieceTypeFactory.cacheSize());  // 3 distinct types, not 3 allocations per move
```

### Design points
- **Appearance shared** — colour/symbol exist **once** per type, however many pieces use them.
- **Position extrinsic** — each piece stores only what is unique to it.
- **Factory cache** — `computeIfAbsent` guarantees one flyweight per type.

**Complexity:** O(1) lookup · Space O(distinct types) + O(pieces) for positions

---
#flyweight #games #lld #practice