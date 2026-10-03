# Design a Terrain Map

**Source:** AlgoMaster · Low-Level Design Practice · **medium (premium)** · **Pattern:** Flyweight
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

A world map is a large grid where every tile is one of a few **terrain types** (grass, water, forest,
mountain). Each terrain type carries heavy shared data — texture, colour, movement cost, sound. With
millions of tiles, storing that data per tile is wasteful. Share the terrain data (**intrinsic**) and
store only the coordinates (**extrinsic**) per tile.

### Approach — Flyweight

- **Intrinsic** (shared, immutable): `TerrainType` (name, colour, movement cost, texture bytes).
- **Extrinsic** (per tile): x, y.
- `TerrainFactory` caches types; the map holds `Tile`s referencing shared types.

### Java Solution

```java
import java.util.*;

// Flyweight — intrinsic, heavy, shared
final class TerrainType {
    private final String name;
    private final String color;
    private final int movementCost;
    private final byte[] texture;                 // pretend this is a big texture

    TerrainType(String name, String color, int movementCost, int textureBytes) {
        this.name = name; this.color = color; this.movementCost = movementCost;
        this.texture = new byte[textureBytes];
    }
    String render(int x, int y) { return color + name + "(" + x + "," + y + ")"; }
    int movementCost() { return movementCost; }
    @Override public String toString() { return name + "[" + color + ",cost=" + movementCost + "]"; }
}

// FlyweightFactory
class TerrainFactory {
    private static final Map<String, TerrainType> CACHE = new HashMap<>();
    static TerrainType get(String name) {
        return CACHE.computeIfAbsent(name, k -> switch (k) {
            case "grass"    -> new TerrainType("grass",    "🟩", 1, 4096);
            case "water"    -> new TerrainType("water",    "🟦", 99, 8192);
            case "forest"   -> new TerrainType("forest",   "🟩", 3, 6144);
            case "mountain" -> new TerrainType("mountain", "⬛", 5, 6144);
            default -> throw new IllegalArgumentException("Unknown terrain: " + k);
        });
    }
    static int cacheSize() { return CACHE.size(); }
}

// Context — extrinsic (coordinates)
class Tile {
    private final int x, y;
    private final TerrainType terrain;
    Tile(int x, int y, TerrainType terrain) { this.x = x; this.y = y; this.terrain = terrain; }

    String render()        { return terrain.render(x, y); }
    int movementCost()     { return terrain.movementCost(); }
}
```

**Usage**
```java
TerrainType grass  = TerrainFactory.get("grass");
TerrainType forest = TerrainFactory.get("forest");

// a 1000x1000 map: 1,000,000 tiles, but only 4 terrain flyweights
Tile tile = new Tile(10, 20, grass);
System.out.println(tile.render());         // 🟩grass(10,20)
System.out.println(TerrainFactory.cacheSize());   // 4
```

### Design points
- **Heavy data shared** — texture/colour/cost stored **once** per terrain, not per tile.
- **Coordinates extrinsic** — each tile only holds x, y.
- **Immutable flyweights** — a terrain type never changes, so it is safe to share.

**Complexity:** O(1) lookup · Space O(terrain types) + O(tiles)

---
#flyweight #games #lld #practice