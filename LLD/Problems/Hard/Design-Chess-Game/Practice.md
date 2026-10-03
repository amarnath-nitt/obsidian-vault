# Design Chess Game - Practice

## Key Concepts
- **Validation is polymorphic** — each piece answers `canMove`; `Game` never switches on `type`
- **Apply, test, roll back** — make the move, ask "is my king in check?", undo if yes — no board copying needed
- **Move is a Command** — it knows both squares, captures the displaced piece, and can undo itself exactly

## Common Moves in LLD
1. **`clearPath` for sliders** — rook/bishop/queen share one path walker; knights skip it
2. **Pawn logic is the fiddly one** — direction flips by color; double step only from start; capture only diagonal
3. **Check = enemy piece attacks your king square** — iterate enemies, reuse `canMove`
4. **Undo restores everything** — piece position, captured piece, and the turn — in one place

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Chess Game](solutions/Design-Chess-Game.md) — Hard · Command, State

---

## Extra Practice (self-study)

- [ ] Add checkmate / stalemate — scan all legal moves for the side to move
- [ ] Add castling — the only move that touches two of your own pieces
- [ ] Add pawn promotion — swap the piece on the promotion square, still one `Move`

## Tips
- Say **"pieces validate, the game arbitrates"** — it answers where each rule lives
- Apply-and-undo beats board cloning in every follow-up about performance
- Walk one pinned-piece scenario (a rook pinned by a bishop) — that is the check rule, live

---

#lld #machine-coding #chess #hard #practice