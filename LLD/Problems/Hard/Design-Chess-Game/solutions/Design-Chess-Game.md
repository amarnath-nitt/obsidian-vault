# Design Chess Game (Hard)

**Difficulty:** Hard · **Patterns:** Command, State
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design chess: the standard setup, per-piece movement rules, alternating turns, capture, check detection, and undo.

**Functional**
- Movement geometry per piece type; path must be clear for rook/bishop/queen; no capturing your own piece.
- A move leaving your king in check is illegal; undo restores board and turn exactly.

**Non-functional**
- New piece types plug in without touching `Game`; no board cloning on the hot path.

### The failure, before

```java
// ❌ One giant `if (pieceType.equals("rook")) {...} else if (...)` block in Game.move:
// pawn captures and double steps interleave with knight jumps, `cloneBoard()` runs per move,
// and undo re-derives the old position — drift after three moves.
// if (type == ROOK && sameRowOrCol(...)) { board[a][b] = null; board[x][y] = piece; } // undo? nowhere.
```

### The Fix (after)

Piece polymorphism for geometry + `Move` as a reversible command + apply/test/undo for check.

```java
import java.util.*;

enum Color { WHITE, BLACK;
    Color opposite() { return this == WHITE ? BLACK : WHITE; } }

abstract class Piece {
    final Color color; int r, c;
    Piece(Color color, int r, int c) { this.color = color; this.r = r; this.c = c; }
    abstract char symbol();
    abstract boolean canMove(Board board, int toR, int toC);
}

class Board {
    final Piece[][] grid = new Piece[8][8];
    Piece at(int r, int c) { return inside(r, c) ? grid[r][c] : null; }
    void set(int r, int c, Piece p) {
        grid[r][c] = p;
        if (p != null) { p.r = r; p.c = c; }
    }
    static boolean inside(int r, int c) { return r >= 0 && r < 8 && c >= 0 && c < 8; }
    boolean clearPath(int r1, int c1, int r2, int c2) {          // sliding pieces only
        int dr = Integer.signum(r2 - r1), dc = Integer.signum(c2 - c1);
        for (int r = r1 + dr, c = c1 + dc; r != r2 || c != c2; r += dr, c += dc)
            if (grid[r][c] != null) return false;
        return true;
    }
    int[] findKing(Color color) {
        for (int r = 0; r < 8; r++) for (int c = 0; c < 8; c++)
            if (grid[r][c] instanceof King k && k.color == color) return new int[]{r, c};
        throw new IllegalStateException("No king of " + color);
    }
}

class Rook extends Piece {
    Rook(Color color, int r, int c) { super(color, r, c); }
    char symbol() { return 'R'; }
    boolean canMove(Board b, int tr, int tc) {
        return (r == tr ^ c == tc) && b.clearPath(r, c, tr, tc);          // exactly one axis
    }
}
class Bishop extends Piece {
    Bishop(Color color, int r, int c) { super(color, r, c); }
    char symbol() { return 'B'; }
    boolean canMove(Board b, int tr, int tc) {
        return Math.abs(tr - r) == Math.abs(tc - c) && b.clearPath(r, c, tr, tc);
    }
}
class Queen extends Piece {
    Queen(Color color, int r, int c) { super(color, r, c); }
    char symbol() { return 'Q'; }
    boolean canMove(Board b, int tr, int tc) {
        boolean straight = (r == tr ^ c == tc);
        boolean diagonal = Math.abs(tr - r) == Math.abs(tc - c);
        return (straight || diagonal) && b.clearPath(r, c, tr, tc);
    }
}
class Knight extends Piece {
    Knight(Color color, int r, int c) { super(color, r, c); }
    char symbol() { return 'N'; }
    boolean canMove(Board b, int tr, int tc) {
        int dr = Math.abs(tr - r), dc = Math.abs(tc - c);
        return dr * dc == 2;                                               // 1×2 L, jumps over
    }
}
class King extends Piece {
    King(Color color, int r, int c) { super(color, r, c); }
    char symbol() { return 'K'; }
    boolean canMove(Board b, int tr, int tc) {
        return Math.max(Math.abs(tr - r), Math.abs(tc - c)) == 1;
    }
}
class Pawn extends Piece {
    Pawn(Color color, int r, int c) { super(color, r, c); }
    char symbol() { return 'P'; }
    boolean canMove(Board b, int tr, int tc) {
        int dir = color == Color.WHITE ? -1 : 1;                           // white marches up
        int startRow = color == Color.WHITE ? 6 : 1;
        if (tc == c && tr == r + dir) return b.at(tr, tc) == null;         // single step
        if (tc == c && tr == r + 2 * dir && r == startRow)
            return b.at(tr, tc) == null && b.at(r + dir, c) == null;       // double from home
        return Math.abs(tc - c) == 1 && tr == r + dir && b.at(tr, tc) != null;   // capture
    }
}

class Move {                                                              // Command: exact undo
    final Piece piece; final int fr, fc, tr, tc; final Piece captured;
    Move(Piece piece, int fr, int fc, int tr, int tc, Piece captured) {
        this.piece = piece; this.fr = fr; this.fc = fc; this.tr = tr; this.tc = tc; this.captured = captured;
    }
    void apply(Board b) { b.set(fr, fc, null); b.set(tr, tc, piece); }
    void undo(Board b)  { b.set(tr, tc, null); b.set(fr, fc, piece); b.set(tr, tc, captured); }
}

class Game {
    final Board board = new Board();
    Color turn = Color.WHITE;
    private final Deque<Move> history = new ArrayDeque<>();

    void setup() {
        Piece[] back = { new Rook(turn, 0, 0), new Knight(turn, 0, 0), new Bishop(turn, 0, 0),
                         new Queen(turn, 0, 0), new King(turn, 0, 0), new Bishop(turn, 0, 0),
                         new Knight(turn, 0, 0), new Rook(turn, 0, 0) };
        for (Color color : Color.values()) {
            int backRow = color == Color.WHITE ? 7 : 0;
            int pawnRow = color == Color.WHITE ? 6 : 1;
            for (int c = 0; c < 8; c++) {
                Piece p = switch (back[c].symbol()) {
                    case 'R' -> new Rook(color, backRow, c);
                    case 'N' -> new Knight(color, backRow, c);
                    case 'B' -> new Bishop(color, backRow, c);
                    case 'Q' -> new Queen(color, backRow, c);
                    default  -> new King(color, backRow, c);
                };
                board.set(backRow, c, p);
                board.set(pawnRow, c, new Pawn(color, pawnRow, c));
            }
        }
    }

    void move(int fr, int fc, int tr, int tc) {
        Piece p = board.at(fr, fc);
        if (p == null) throw new IllegalStateException("Empty square");
        if (p.color != turn) throw new IllegalStateException("Not " + p.color + "'s turn");
        if (!Board.inside(tr, tc)) throw new IllegalStateException("Off board");
        Piece target = board.at(tr, tc);
        if (target != null && target.color == p.color) throw new IllegalStateException("Own piece");
        if (!p.canMove(board, tr, tc)) throw new IllegalStateException(p.symbol() + " cannot move there");

        Move m = new Move(p, fr, fc, tr, tc, target);
        m.apply(board);
        if (inCheck(board, turn)) {                    // apply → test → roll back
            m.undo(board);
            throw new IllegalStateException("Move leaves the king in check");
        }
        history.push(m);
        turn = turn.opposite();
    }

    void undo() {
        if (history.isEmpty()) throw new IllegalStateException("No moves to undo");
        history.pop().undo(board);
        turn = turn.opposite();
    }

    boolean inCheck(Board b, Color color) {
        int[] king = b.findKing(color);
        for (int r = 0; r < 8; r++) for (int c = 0; c < 8; c++) {
            Piece p = b.grid[r][c];
            if (p != null && p.color != color && p.canMove(b, king[0], king[1])) return true;
        }
        return false;
    }
    boolean opponentInCheck() { return inCheck(board, turn.opposite()); }
}
```

**Usage**
```java
Game g = new Game();
g.setup();
g.move(6, 4, 4, 4);       // e2-e4
g.move(1, 4, 3, 4);       // e7-e5
g.undo();                 // e5 pawn back; BLACK to move again
g.move(6, 3, 4, 3);       // d2-d4
System.out.println(g.opponentInCheck());   // false — for now
```

### Design points
- **Geometry per piece** — five tiny `canMove` implementations replace one mega-switch; adding a variant piece changes one file.
- **Apply, test, roll back** — check legality without cloning the board; the `Move` undoes itself exactly.
- **`clearPath` is shared machinery** — rook, bishop, and queen all lean on the same walker; knight and pawn bypass it.
- **Undo restores all three** — moving piece, captured piece, and the turn — from data captured at move time.

**Complexity:** move O(64) check scan + O(8) path · undo O(1) · memory O(history).

---
#lld #machine-coding #chess #hard #practice