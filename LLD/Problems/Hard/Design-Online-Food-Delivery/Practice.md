# Design Online Food Delivery Service like Swiggy - Practice

## Key Concepts
- **One order machine, three parties** — restaurant accepts, kitchen prepares, agent delivers; each party owns exactly one transition
- **Dispatch = filter + nearest + assign, atomic** — the same pattern as Uber; agents flip to ON_DELIVERY on assignment
- **Tracking is an Observer** — every transition fires `onUpdate`; the app never polls

## Common Moves in LLD
1. **Cancel is time-boxed** — allowed before OUT_FOR_DELIVERY; after dispatch there is no un-ringing that bell
2. **Fee at delivery** — distance is a fact then; base + per-km (+ surge wrapper if asked)
3. **Item validation at placement** — cart lines must map to menu items; prices snapshot into the order
4. **Reuse the Uber vocabulary** — Location, nearest-match, agent status — recognition is free

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Online Food Delivery Service like Swiggy](solutions/Design-Online-Food-Delivery.md) — Hard · State, Strategy, Observer

---

## Extra Practice (self-study)

- [ ] Add agent acceptance with timeout — retry the next nearest on expiry
- [ ] Add per-restaurant prep times — OUT_FOR_DELIVERY trigger at ready time
- [ ] Add surge fees — a `SurgeFee` wrapping `DistanceFee` by zone/hour

## Tips
- Say **"three parties, one machine — each transition has exactly one owner"**
- Rehearse cancel from PLACED and from OUT_FOR_DELIVERY — different answers, one method
- Status fan-out is the demo moment: print every `onUpdate` and the story tells itself

---

#lld #machine-coding #swiggy #hard #practice