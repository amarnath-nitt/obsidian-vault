# Design Pub Sub System - Practice

## Key Concepts
- **Broker owns topics, topics own subscriber lists** — publish looks up once, fans out after
- **Queue between publish and deliver** — publishers never wait on slow subscribers
- **Offsets make it durable** — resubscribe replays from the retained buffer

## Common Moves in LLD
1. **Filter at delivery** — subscriber predicate checked per message, publisher unaware
2. **Unsubscribe is exact** — remove the registration object, not by name match
3. **Retry with backoff, then dead-letter** — failing callbacks never stall the topic
4. **Per-topic order** — single worker per topic preserves publish order

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Pub Sub System](solutions/Design-Pub-Sub-System.md) — Medium · Observer, Singleton

---

## Extra Practice (self-study)

- [ ] Add durable replay — retained ring buffer + offset per subscriber
- [ ] Add wildcard topics — `sports.*` matches `sports.football`
- [ ] Add dead-letter queue — 3 failed deliveries move the message aside

## Tips
- Say **"publish returns before delivery finishes"** — the async sentence
- Ordering per topic only — say the limit before they probe it
- Unsubscribe must actually stop delivery — test it explicitly

---

#lld #machine-coding #pubsub #medium #practice
