# Concurrency vs Parallelism — Concept

## What Is It?

Two different ideas that interviews routinely conflate:

| | **Concurrency** | **Parallelism** |
|---|---|---|
| **Question** | How do we structure *multiple tasks*? | How do we *execute* them simultaneously? |
| **Mechanism** | interleaving on (possibly) one core | true simultaneous execution on multiple cores |
| **Needs** | a scheduler / event loop | multiple hardware resources |
| **Can exist alone?** | yes — one core, many tasks | no — parallelism implies concurrency is happening |

---

## When to Use

> **Trigger keywords:** "at the same time", "multi-core", "event loop", "why does one CPU still support threads"

| Trigger | Answer |
|---------|--------|
| "Is my program concurrent?" | Do it structure work so tasks can **interleave**? |
| "Is it parallel?" | Are tasks **actually executing simultaneously**? |
| "One core, many threads — concurrent or parallel?" | **Concurrent, not parallel** |
| "We need speed on 8 cores" | **Parallelism** — split the work |

---

## The mental model

```text
Concurrency (1 core)          Parallelism (4 cores)
─────────────────────         ─────────────────────
A A . B B . C C               A A A A
  time-sliced                   │
B runs while A waits            B B B B   (all at once)
                                C C C C
```

- A **concurrent** system can be correct with **zero** parallelism.
- A **parallel** system is necessarily concurrent.
- Concurrency is a **design** problem; parallelism is (also) a **hardware/scheduling** problem.

---

## Notes

- The dangerous bugs — race conditions, deadlock — are **concurrency** problems. Parallelism just makes them easier to hit.
- Java gives you concurrency (threads) regardless of core count; parallelism depends on the OS scheduler and cores available.
- `parallelStream()` is parallelism; a thread pool serving a queue is concurrency (and may be parallel too).

---

## Common Mistakes

1. Using "concurrent" and "parallel" interchangeably in an interview — say the distinction, it scores points.
2. Assuming more threads = more parallelism — beyond core count, threads **context-switch**, they don't add capacity.
3. Concluding that single-core code can't have race conditions — it can (interleaving still happens).

---

## Related

- [[../00 - Index|Concurrency Concepts Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Processes-vs-Threads/Concept|Processes vs Threads]]

---

#concurrency #lld #concept
