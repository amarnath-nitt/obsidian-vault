# Design CricInfo - Practice

## Key Concepts
- **Events are the source of truth** — `BallEvent`s append to a log; scorecards are projections computed from them
- **One ball mutates many stats** — innings score, striker, bowler, extras, overs — atomically, in one method
- **Observers fan out after state settles** — commentary and screens read a consistent ball, never mid-update

## Common Moves in LLD
1. **Extras do not count as balls** — wide/no-ball add runs but not to `legalBalls`; over-end checks use legal balls only
2. **Strike rotation has three triggers** — odd runs, end of over, wicket (new batter) — keep them in one place
3. **Wicket walks in the next batter** — batting order is a queue, not a lookup
4. **Innings end is a predicate** — `wickets == 10 || legalBalls == quota`; `ball()` refuses when true

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design CricInfo](solutions/Design-CricInfo.md) — Hard · Observer, Command

---

## Extra Practice (self-study)

- [ ] Add **undo** — pop the last `BallEvent` and replay the log (events make this possible)
- [ ] Add a DLS target — par score on stoppage
- [ ] Add player career aggregates — stats roll up from match logs

## Tips
- Say **"balls are events, cards are projections"** — it reframes updates as replay + fold
- Get extras right first — interviewers use wides to test your ball counting
- The wicket + end-of-over double rotations are one combined move — handle both in one check

---

#lld #machine-coding #cricinfo #hard #practice