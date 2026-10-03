# Design Tic Tac Toe Game - Practice

## Key Concepts
- **Counters, not scans** — per-row / per-col / two-diag tallies per symbol; a win is a counter hitting N
- **Moves are commands** — place + push history; undo pops and decrements
- **Bots are strategies** — random now, minimax later, engine untouched

## Common Moves in LLD
1. **Validate before mutate** — bounds, empty, live game; one guard method
2. **Detect right after place** — row, col, diag (if on one), then full-board draw check
3. **Turn flips only on success** — illegal move keeps the turn
4. **State is terminal** — WON/DRAWN rejects further moves

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Tic Tac Toe Game](solutions/Design-Tic-Tac-Toe.md) — Medium · State, Strategy, Command

---

## Extra Practice (self-study)

- [ ] Add NxN + K-in-a-row — counters generalise, scans do not
- [ ] Add minimax bot — a strategy over the same `pick` interface
- [ ] Add replay — re-execute the move list on a fresh board

## Tips
- Say **"O(1) win detection via counters"** in the first minute — it is the whole differentiator
- Undo = pop + decrement — show both halves
- Draw only after no win — order matters

---

#lld #machine-coding #tic-tac-toe #medium #practice
