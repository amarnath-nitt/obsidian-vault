# Design a Game Save System

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Memento
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-game-save-system)

### Problem

A game needs **save and load** checkpoints. When the player saves, the game's current state (level,
score, position, inventory) is captured; loading restores it exactly. The save system must not expose
the game's internals.

### Approach — Memento

- **Originator** = `Game` — `save()` returns a memento; `load(memento)` restores.
- **Memento** = an immutable snapshot of the game state.
- **Caretaker** = `SaveManager` — named saves, never reads their contents.

### Java Solution

```java
import java.util.*;

final class Game {                                          // Originator
    private int level, score, posX, posY;
    private final List<String> inventory = new ArrayList<>();

    void play(int level, int score, int x, int y) {
        this.level = level; this.score = score; this.posX = x; this.posY = y;
    }
    void pickUp(String item) { inventory.add(item); }

    @Override public String toString() {
        return "L" + level + " score=" + score + " pos=(" + posX + "," + posY + ") inv=" + inventory;
    }

    GameState save() {                                       // capture a deep snapshot
        return new GameState(level, score, posX, posY, inventory);
    }
    void load(GameState state) {
        this.level = state.level();
        this.score = state.score();
        this.posX  = state.posX();
        this.posY  = state.posY();
        this.inventory.clear();
        this.inventory.addAll(state.inventory());
    }

    /** Immutable, opaque snapshot. */
    static final class GameState {
        private final int level, score, posX, posY;
        private final List<String> inventory;
        private GameState(int level, int score, int posX, int posY, List<String> inventory) {
            this.level = level; this.score = score; this.posX = posX; this.posY = posY;
            this.inventory = List.copyOf(inventory);         // copy → no aliasing
        }
        private int level() { return level; }
        private int score() { return score; }
        private int posX()  { return posX; }
        private int posY()  { return posY; }
        private List<String> inventory() { return inventory; }
    }
}

class SaveManager {                                         // Caretaker
    private final Map<String, Game.GameState> saves = new LinkedHashMap<>();

    void save(String slot, Game game) { saves.put(slot, game.save()); }
    boolean load(String slot, Game game) {
        Game.GameState state = saves.get(slot);
        if (state == null) return false;
        game.load(state);
        return true;
    }
    Set<String> slots() { return saves.keySet(); }
}
```

**Usage**
```java
Game game = new Game();
SaveManager saves = new SaveManager();

game.play(1, 100, 5, 7);
game.pickUp("sword");
saves.save("slot1", game);

game.play(3, 900, 40, 40);      // player progresses
game.pickUp("shield");

saves.load("slot1", game);      // restore the earlier checkpoint
System.out.println(game);       // L1 score=100 pos=(5,7) inv=[sword]
```

### Design points
- **Deep snapshot** — `List.copyOf` prevents later inventory changes leaking into the save.
- **Opaque memento** — `SaveManager` stores and restores but never reads `GameState`.
- **Named slots** — the caretaker is a `Map<String, Memento>` for multiple checkpoints.

**Complexity:** O(state size) per save/load · Space O(saves × state size)

---
#memento #games #lld #practice