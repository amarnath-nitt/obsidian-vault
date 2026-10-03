# Design Online Stock Brokerage System - Practice

## Key Concepts
- **Price-time priority is two data structures** — `TreeMap` for price, `Deque` for FIFO inside each level
- **Fills are increments, not transactions** — a fill reduces both remainders; the trade settles both sides
- **Resting vs crossing** — limit remainders rest in the book; market remainders are cancelled (IOC)

## Common Moves in LLD
1. **Cross test per side** — BUY crosses when `bookAsk <= limit`; SELL when `bookBid >= limit`
2. **Partial fill status** — `remaining == 0 → FILLED`, else `PARTIAL`; both orders updated together
3. **Cost basis on sell** — remove shares at *average cost*; realized P&L falls out
4. **Check before placing** — funds for buys, shares for sells; settlement assumes checks passed

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Online Stock Brokerage System](solutions/Design-Online-Stock-Brokerage.md) — Hard · Strategy, Observer

---

## Extra Practice (self-study)

- [ ] Add stop orders — trigger price arms a market order
- [ ] Add market data feed — best bid/ask observers on every book change
- [ ] Add realized P&L — sells book `(price − avgCost) × qty`

## Tips
- Say **"TreeMap for price, Deque for time — that is price-time priority, literally"**
- Demo the partial fill: 80 buy vs 50 in the book → 50 filled, 30 rest
- Market orders never rest; say "IOC" out loud — it signals you know the semantics

---

#lld #machine-coding #stock-brokerage #hard #practice