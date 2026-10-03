# Design a Snake and Ladder Game - Practice

## Key Concepts
- **Exact roll wins** — an overshoot keeps you in place; the boundary rule is a first-class requirement
- **One hop per turn** — a snake landing on a cell that contains a ladder does not chain (classic house rule)
- **Dice is a Strategy** — `ScriptedDice` makes whole games reproducible in tests

## Common Moves in LLD
1. **Board owns the jump map** — validation on setup (ladder up, snake down) means the game never checks
2. **`step()` = one turn** — roll, move, resolve, check win, advance turn — in that order
3. **Observers after the move settles** — log gets `(from, landed, to, roll)`; UI never guesses
4. **Winner freezes the game** — further `step()` calls throw; the loop is over

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design a Snake and Ladder Game](solutions/Design-Snake-and-Ladder.md) — Hard · Strategy, Observer

---

## Extra Practice (self-study)

- [ ] Add rule variants — sixes grant an extra roll; three sixes forfeit the turn
- [ ] Add two dice — a sum-based variant, same loop
- [ ] Add a min-roll board solver — expected turns to win via simulation

## Tips
- Say **"the die is injected; the game is deterministic given a roll sequence"** — testing story in one line
- Walk the exact-roll boundary first (99 + 4) — it is the most-missed rule
- Resolve jumps once per turn and say so — chaining is a deliberate *non*-feature

---

#lld #machine-coding #snake-and-ladder #hard #practice