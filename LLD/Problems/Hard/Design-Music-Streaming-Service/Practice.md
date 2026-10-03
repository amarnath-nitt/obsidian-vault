# Design Music Streaming Service like Spotify - Practice

## Key Concepts
- **The player is a state machine** — STOPPED → PLAYING ⇄ PAUSED; next/previous are queue operations, not states
- **Shuffle is a strategy over the queue** — Fisher–Yates re-arranges; unshuffling restores the original order
- **Playback events fan out** — count observers fire on play and track-change; no polling

## Common Moves in LLD
1. **Two lists: original + queue** — toggling shuffle rebuilds the queue from the original, keeping the current song at the front
2. **Repeat semantics in `next()`** — ONE replays, ALL wraps, OFF stops at the end
3. **Tier gating at the facade** — FREE → shuffle forced on; the gating lives in `MusicService`, not `Player`
4. **Search is a filter** — title/artist contains, case-insensitive; add indexes only when asked

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Music Streaming Service like Spotify](solutions/Design-Music-Streaming-Service.md) — Hard · State, Strategy, Observer

---

## Extra Practice (self-study)

- [ ] Add a recommendation strategy — "next up" from play history
- [ ] Add offline downloads — per-user download set gating playback
- [ ] Add lyrics sync — timestamped lines advanced by the player clock

## Tips
- Say **"the queue is data, the player is state, shuffle is policy"** — three-way split, everything follows
- Demo repeat-ONE on `next()` — the only place the song does not change
- Keep unshuffle faithful: save the original order *before* shuffling

---

#lld #machine-coding #spotify #hard #practice