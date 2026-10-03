# Design an Online Auction System - Practice

## Key Concepts
- **The bid ladder** — next floor = `max(reserve, current + increment)`; a bid below the floor never lands
- **Close decides, not bid** — the winner is chosen at close (reserve still matters); bids only record intent
- **Observer fans out** — watchers and auto-bidders react after the ladder update, inside one atomic section

## Common Moves in LLD
1. **Synchronize the ladder** — `placeBid` is atomic: check floor → set highest → notify
2. **State gates everything** — bids only while ACTIVE; close only from ACTIVE, and only once
3. **Auto-bid is a proxy** — an observer that responds to outbids up to its max; recursion terminates at the cap
4. **Reserve without winner** — close with no qualifying bid returns null — no sale, no fake winner

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design an Online Auction System](solutions/Design-Online-Auction-System.md) — Medium · Observer, State, Strategy

---

## Extra Practice (self-study)

- [ ] Add a scheduled close — a time wheel fires `close()` at `endTime`
- [ ] Add anti-sniping — bids in the last 30s extend the deadline
- [ ] Add per-bidder deposit handling — refund losers on close (Facade over payments)

## Tips
- Say **"bids ratchet, close decides"** — it answers 80% of the follow-ups
- Reentrancy is the auto-bid trap — the same lock must tolerate a nested `placeBid`
- Test the reserve boundary: reserve met exactly, and reserve missed by one

---

#lld #machine-coding #auction #medium #practice