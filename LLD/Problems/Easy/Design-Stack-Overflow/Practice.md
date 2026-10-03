# Design Stack Overflow - Practice

## Key Concepts
- **Votable interface** — questions and answers share vote handling; one code path
- **Reputation derived via Observer** — vote event → reputation → badge → notification fan-out
- **Accepted answer is a state change** — marks question answered, pays the accept bonus

## Common Moves in LLD
1. **One-vote-per-user rule** — voter-keyed map on each Votable, toggle on repeat
2. **Strategy for vote weights** — upvote/downvote/accept values pluggable
3. **Observers for side effects** — reputation, badges, notifications subscribe; voters stay dumb
4. **Tags as value objects** — validated strings, indexed for search later

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Stack Overflow](solutions/Design-Stack-Overflow.md) — Easy · Observer, Strategy

---

## Extra Practice (self-study)

- [ ] Add downvote cost (−1 to voter) — inside the strategy, no voter changes
- [ ] Add close-vote (5 votes closes) — state transition on Question
- [ ] Add bounty (+50..500, 7 days) — escrow on accept or expiry

## Tips
- Say **"reputation is derived, never stored as input"** — votes are the source of truth
- One vote per user per post — say it before they ask
- Accept bonus (+15 answerer / +2 asker) is the number interviewers check

---

#lld #machine-coding #stack-overflow #easy #practice
