# Design Course Registration System - Practice

## Key Concepts

- **Capacity is an invariant, not a check** — every mutation path (enroll, drop→promote) respects `roster ≤ capacity`
- **Waitlist is a Deque** — FIFO promotion is `poll()`; no fairness bookkeeping needed
- **Checks happen before mutation** — prereq + conflict + already-registered, then place — never the reverse

## Common Moves in LLD
1. **Overlap is interval math** — same day `&&` `start < other.end && other.start < end` (half-open hours)
2. **Promotion is a cascading enroll** — drop → `poll()` → same place() logic minus the checks, then notify
3. **Drop from waitlist ≠ drop from roster** — the first removes silently, the second triggers promotion
4. **Synchronize `enroll` and `drop`** — capacity is a shared invariant; one lock keeps it honest

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Course Registration System](solutions/Design-Course-Registration-System.md) — Hard · Observer, State

---

## Extra Practice (self-study)

- [ ] Add registration windows — seniors open first; a policy checked before enroll
- [ ] Add credit limits — max credits per term, enforced per student
- [ ] Add waitlist expiry — unclaimed promotions return to the list after N hours

## Tips
- Say **"promotion reuses the placement path"** — it shows one code path for roster changes
- Walk the conflict check with two overlapping slots at the boundary (9–10 and 10–11 do not conflict)
- The concurrency answer is one word: `synchronized` around enroll/drop — then discuss striping

---

#lld #machine-coding #course-registration #hard #practice