# Design a Snake and Ladder Game (Hard)

**Difficulty:** Hard · **Patterns:** Strategy, Observer
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design Snake and Ladder: configurable board with snakes/ladders, N players, exact-roll win condition, and a move log.

**Functional**
- Jump map with validated ladders (up) and snakes (down); 2+ players in turn order.
- Roll → move → resolve jump; overshoot stays; exact landing wins; every move observed.

**Non-functional**
- Dice swappable (fair / scripted); game deterministic under a scripted dice.

### The failure, before

```java
// ❌ position math inline in the loop: 99 + 4 lands at "103" (no board),
// snakes/ladders resolved in an unordered if-chain that can chain twice,
// and the die is `new Random()` buried inside — untestable.
// pos += dice.nextInt(6) + 1; if (pos > 100) pos = 100;  // house rules trampled
```

### The Fix (after)

`Board.resolve` owns jumps; `step()` is one guarded turn; `Dice` is injected.

```java
import java.util.*;

interface Dice { int roll(); }

class FairDice implements Dice {
    private final Random rnd = new Random();
    public int roll() { return rnd.nextInt(6) + 1; }
}

class ScriptedDice implements Dice {                    // deterministic games in tests
    private final int[] rolls; private int i = 0;
    ScriptedDice(int... rolls) { this.rolls = rolls; }
    public int roll() { return rolls[i++ % rolls.length]; }
}

class Board {
    final int last;
    private final Map<Integer, Integer> jumps = new HashMap<>();   // snakes + ladders together
    Board(int last) { this.last = last; }
    void addLadder(int from, int to) {
        if (to <= from || to > last) throw new IllegalArgumentException("Ladder must go up");
        jumps.put(from, to);
    }
    void addSnake(int from, int to) {
        if (to >= from) throw new IllegalArgumentException("Snake must go down");
        jumps.put(from, to);
    }
    int resolve(int cell) { return jumps.getOrDefault(cell, cell); }   // one hop per turn
}

class Player {
    final String name; int position = 0;
    Player(String name) { this.name = name; }
}

interface MoveObserver { void onMove(Player player, int from, int landed, int to, int roll); }

class Game {
    private final Board board; private final List<Player> players; private final Dice dice;
    private final List<MoveObserver> observers = new ArrayList<>();
    private int turn = 0; private Player winner;

    Game(Board board, List<Player> players, Dice dice) {
        if (players.size() < 2) throw new IllegalArgumentException("Need 2+ players");
        this.board = board; this.players = players; this.dice = dice;
    }
    void subscribe(MoveObserver o) { observers.add(o); }
    Player current() { return players.get(turn % players.size()); }
    Optional<Player> winner() { return Optional.ofNullable(winner); }

    void step() {                                                    // exactly one turn
        if (winner != null) throw new IllegalStateException("Game over — " + winner.name + " won");
        Player p = current();
        int roll = dice.roll();
        int from = p.position;
        int landed = from + roll;
        int to = landed > board.last ? from                          // exact roll to finish
               : board.resolve(landed);                              // ladder up / snake down
        p.position = to;
        observers.forEach(o -> o.onMove(p, from, landed, to, roll));
        if (to == board.last) winner = p; else turn++;
    }
}
```

**Usage**
```java
Board board = new Board(100);
board.addLadder(4, 25); board.addLadder(21, 42);
board.addSnake(99, 41);

Game game = new Game(board,
        List.of(new Player("Asha"), new Player("Bharat")),
        new ScriptedDice(4, 6, 2, 5));
game.subscribe((p, from, landed, to, roll) ->
        System.out.println(p.name + " rolled " + roll + ": " + from + " → " + to));

game.step();        // Asha rolls 4 → lands 4 → ladder to 25
game.step();        // Bharat rolls 6 → 6
game.step();        // Asha rolls 2 → 27
```

### Design points
- **The board validates its own jumps** — a ladder that goes down cannot be built; the game trusts the map.
- **Exact roll is a boundary rule** — `landed > last → stay`; the win check only ever sees `to == last`.
- **One resolution per turn** — `resolve()` applies a single jump; chaining is a documented non-feature.
- **Injected dice make games replayable** — `ScriptedDice(4, 6, 2, 5)` replays the same game forever.

**Complexity:** step O(1) · setup O(jumps).

---
#lld #machine-coding #snake-and-ladder #hard #practice