# Design Logging Framework - Practice

## Key Concepts
- **Level gate before fan-out** — logger checks once, handlers each re-check at their own level
- **Chain of handlers** — console/file/network linked via `setNext`; order is configuration
- **Formatter as Strategy** — plain/JSON renderers plug into any handler

## Common Moves in LLD
1. **Singleton registry** — `LogManager.getLogger(name)` returns the same logger per name
2. **Record as value object** — level + message + timestamp + thread captured once
3. **Fail-safe handlers** — catch, count, continue; logging never throws into app code
4. **Hierarchy via propagation** — child logger forwards up to root handlers

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Logging Framework](solutions/Design-Logging-Framework.md) — Easy · Singleton, Chain of Responsibility

---

## Extra Practice (self-study)

- [ ] Add JSON formatter — one class, wired per handler, no logger change
- [ ] Add module filter — drops records outside the allow-list
- [ ] Add async handler — queue + background thread drains to the wrapped handler

## Tips
- Say **"logging never throws"** — the sentence interviewers wait for
- Levels are ordered ints — comparison, not a switch
- Hierarchy = propagation to parent handlers, not inheritance of loggers

---

#lld #machine-coding #logging #easy #practice
