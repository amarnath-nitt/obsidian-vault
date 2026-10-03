# Design LRU Cache - Practice

## Key Concepts
- **Map for lookup, list for order** — HashMap key to node; head is MRU, tail is LRU
- **Splice on every hit** — get and put-update both detach + attach-head identically
- **Evict-after-insert in one place** — overflow check only after the new node is linked

## Common Moves in LLD
1. **Key lives in the node** — tail eviction deletes from the map with no reverse lookup
2. **Sentinels remove branches** — head/tail dummies make detach/attach null-free
3. **One lock per op** — lookup + splice is atomic; striped locks only on demand
4. **Policy behind an interface** — LRU now, LFU/TTL later without touching the cache

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design LRU Cache](solutions/Design-LRU-Cache.md) — Medium · Data structure (HashMap + doubly-linked list)

---

## Extra Practice (self-study)

- [ ] Add TTL per entry — expiry checked on get, swept on put
- [ ] Add LFU eviction — frequency map + min-heap, same interface
- [ ] Add striped locks — per-shard map + list when contention is proven

## Tips
- Say **"every access splices to head"** — the sentence that ends the question
- Draw map arrows into list nodes before coding — the two-structure picture is the design
- Miss returns −1, never throws — say it before they ask

---

#lld #machine-coding #lru-cache #medium #practice
