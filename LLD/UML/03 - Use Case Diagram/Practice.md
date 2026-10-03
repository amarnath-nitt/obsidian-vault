# Use Case Diagram - Practice

## Key Concepts
- **Actors + goals + boundary** — roles outside, ovals inside, the box says what you build
- **Goals, not steps** — "Pay Fee" is a use case; "Enter Card Number" is a step inside it
- **`<<include>>` vs `<<extend>>`** — always-needed vs optional add-on

## Common Triggers in Interviews
| Trigger | Response |
|---------|----------|
| "what should the system do" / "scope" | draw actors + ovals **before** any class |
| "who uses it" | humans *and* external systems are actors |
| "is X in scope?" | no oval → explicitly out unless added |

---

## Exercises (self-study)

> UML has no AlgoMaster exercise — the use case diagram is your 2-minute scoping tool. Work these on paper or a whiteboard.

- [ ] **Scope Parking Lot** — actors Driver / Attendant / Payment Gateway; 4–6 ovals; draw the boundary
- [ ] **Goals vs steps** — sort into ovals vs steps: Pay Fee, Enter Card Number, Park Vehicle, Scan Ticket, Issue Ticket
- [ ] **Include vs extend** — Pay Fee includes Calculate Fare; Apply Coupon extends Pay Fee — draw both dashed arrows correctly
- [ ] **Find the missing actor** — a design mentions "send SMS receipt" but shows no actor: add Notification Service and re-draw

---

## Extra Practice

- [ ] Scope any Medium problem in 6 ovals or fewer before touching its class diagram
- [ ] Practice the 60-second narration: *"actors are X, goals are Y, out of scope is Z"*

## Tips
- **Draw it while clarifying requirements** — it turns vague prompts into an agreed feature list
- 3–6 ovals; more means you haven't scoped
- Name the out-of-scope items out loud — interviewers score that
