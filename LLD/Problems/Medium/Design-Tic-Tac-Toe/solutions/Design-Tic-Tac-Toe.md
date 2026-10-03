# Design Tic Tac Toe Game (Medium)

**Difficulty:** Medium · **Patterns:** State, Strategy, Command
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design an N×N Tic Tac Toe engine: alternate moves, validate, detect win/draw in O(1), undo, bot players.

**Functional**
- N×N board; X / O alternate; validate bounds + occupancy + live game.
- Win on full row/col/diag; draw on full board; undo last move.

**Non-functional**
- O(1) win detection; pluggable bot strategies.

### The failure, before

```java
// ❌ Full-board scan after every move — O(N^2) per turn, undo forgotten,
// bot logic if-else'd inside the engine.
public boolean won() { for (rows) for (cols) ... }  // scans everything, every time
```

### The Fix (after)

Row/col/diag counters per symbol + move history + bot strategy.

```java
import java.util.*;

enum Mark { X, O, EMPTY }
enum GameState { IN_PROGRESS, WON, DRAWN }

interface BotStrategy { int[] pick(Board b, Mark s); }

class Board {
    private final int n; private final Mark[][] grid;
    Board(int n) { this.n = n; grid = new Mark[n][n]; for (Mark[] r : grid) Arrays.fill(r, Mark.EMPTY); }
    public int size() { return n; }
    public Mark at(int r, int c) { return grid[r][c]; }
    public void set(int r, int c, Mark s) { grid[r][c] = s; }
    public boolean full(int filled) { return filled == n * n; }
}

class Game {
    private final Board board;
    private final int[] rows, cols; private int diag, anti;
    private Mark turn = Mark.X; private int filled = 0;
    private GameState state = GameState.IN_PROGRESS;
    private final Deque<int[]> history = new ArrayDeque<>();
    private final BotStrategy bot = (b, s) -> {   // random bot: replace with minimax
        Random rnd = new Random();
        int r, c; do { r = rnd.nextInt(b.size()); c = rnd.nextInt(b.size()); }
        while (b.at(r, c) != Mark.EMPTY);
        return new int[]{r, c};
    };

    Game(int n) { board = new Board(n); rows = new int[n]; cols = new int[n]; }

    public synchronized GameState makeMove(int r, int c) {
        if (state != GameState.IN_PROGRESS) throw new IllegalStateException("Game over");
        int n = board.size();
        if (r < 0 || c < 0 || r >= n || c >= n) throw new IllegalArgumentException("Off board");
        if (board.at(r, c) != Mark.EMPTY) throw new IllegalStateException("Occupied");
        board.set(r, c, turn);
        history.push(new int[]{r, c});
        int d = (turn == Mark.X) ? 1 : -1, N = board.size();
        rows[r] += d; cols[c] += d;
        if (r == c) diag += d;
        if (r + c == N - 1) anti += d;
        filled++;
        if (Math.abs(rows[r]) == N || Math.abs(cols[c]) == N
                || Math.abs(diag) == N || Math.abs(anti) == N) state = GameState.WON;
        else if (board.full(filled)) state = GameState.DRAWN;
        else turn = (turn == Mark.X) ? Mark.O : Mark.X;   // flip only on success
        return state;
    }

    public synchronized void undo() {
        if (history.isEmpty()) throw new IllegalStateException("Nothing to undo");
        int[] m = history.pop();
        int d = (board.at(m[0], m[1]) == Mark.X) ? 1 : -1, N = board.size();
        rows[m[0]] -= d; cols[m[1]] -= d;
        if (m[0] == m[1]) diag -= d;
        if (m[0] + m[1] == N - 1) anti -= d;
        board.set(m[0], m[1], Mark.EMPTY);
        filled--; state = GameState.IN_PROGRESS;
        turn = (turn == Mark.X) ? Mark.O : Mark.X;
    }
    public int[] botMove() { return bot.pick(board, turn); }
    public GameState state() { return state; }
}
```

**Usage**
```java
Game g = new Game(3);
g.makeMove(0, 0); g.makeMove(1, 0); g.makeMove(0, 1); g.makeMove(1, 1); g.makeMove(0, 2); // X wins row 0
```

### Design points
- **Counters hit N, game ends** — signed tallies (+1 X / −1 O) detect either winner with one abs check.
- **Undo mirrors place** — pop + decrement restores every counter exactly.
- **Turn flips only on success** — illegal moves throw before the flip, so the turn never skips.
- **Bots behind one method** — `pick(board, symbol)`; minimax plugs in with no engine change.

**Complexity:** move/undo O(1) · Space O(N²) board + O(moves) history.

---
#lld #machine-coding #tic-tac-toe #medium #practice
