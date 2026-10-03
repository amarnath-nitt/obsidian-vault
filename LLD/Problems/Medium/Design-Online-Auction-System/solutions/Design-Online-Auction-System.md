# Design an Online Auction System (Medium)

**Difficulty:** Medium · **Patterns:** Observer, State, Strategy
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design an auction: create items with start/close and reserve, place ascending bids by minimum increment, notify watchers, close to a winner.

**Functional**
- Create an auction (item, min increment, reserve); place bids only above the ladder floor.
- Close once — highest qualifying bidder wins; watchers notified on every bid and on close.

**Non-functional**
- Concurrent bids lose no updates; auto-bidding layers on without touching `Auction`.

### The failure, before

```java
// ❌ `long currentBid` with no increment or reserve, notified outside the critical section:
// two bidders read the same current value, the second overwrites the first, observers miss updates.
if (amount > current) current = amount;   // reserved? increment? race?
notifyWatchers();                          // outside the update → notifications can reorder
```

### The Fix (after)

An atomic bid ladder (`max(reserve, current + increment)`) + observers notified inside the update.

```java
import java.util.*;

enum AuctionState { SCHEDULED, ACTIVE, CLOSED }

record Bid(String bidder, long amount, long at) {}

interface BidObserver {
    void onBid(Auction auction, Bid bid);
    default void onClose(Auction auction, Bid winner) {}
}

class Auction {
    final String item; final long increment; final long reserve;
    private final List<BidObserver> observers = new ArrayList<>();
    private AuctionState state = AuctionState.SCHEDULED;
    private Bid highest;

    Auction(String item, long increment, long reserve) {
        this.item = item; this.increment = increment; this.reserve = reserve;
    }

    void watch(BidObserver o) { observers.add(o); }
    synchronized AuctionState state() { return state; }

    void open() {
        if (state != AuctionState.SCHEDULED) throw new IllegalStateException("Cannot open from " + state);
        state = AuctionState.ACTIVE;
    }

    synchronized void placeBid(String bidder, long amount) {
        if (state != AuctionState.ACTIVE) throw new IllegalStateException("Auction is " + state);
        long floor = highest == null ? reserve : Math.max(reserve, highest.amount() + increment);
        if (amount < floor) throw new IllegalArgumentException("Bid must be ≥ " + floor);
        highest = new Bid(bidder, amount, System.currentTimeMillis());
        observers.forEach(o -> o.onBid(this, highest));     // inside the lock: order matches ladder
    }

    synchronized Bid close() {
        if (state != AuctionState.ACTIVE) throw new IllegalStateException("Cannot close from " + state);
        state = AuctionState.CLOSED;
        Bid winner = highest != null && highest.amount() >= reserve ? highest : null;
        observers.forEach(o -> o.onClose(this, winner));
        return winner;
    }
}

class AutoBidder implements BidObserver {                  // proxy: raise up to `max`
    private final String bidder; private final long max;
    AutoBidder(String bidder, long max) { this.bidder = bidder; this.max = max; }
    public void onBid(Auction a, Bid bid) {
        if (bid.bidder().equals(bidder)) return;           // never outbid yourself
        long next = bid.amount() + a.increment;
        if (next <= max) a.placeBid(bidder, next);         // recurses until someone caps out
    }
}

class AuctionSystem {
    private final Map<String, Auction> auctions = new LinkedHashMap<>();
    private int seq = 0;
    Auction create(String item, long increment, long reserve) {
        Auction a = new Auction(item, increment, reserve);
        auctions.put("A" + (++seq), a);
        return a;
    }
}
```

**Usage**
```java
AuctionSystem sys = new AuctionSystem();
Auction a = sys.create("Vintage Camera", 10, 500);
a.watch(new AutoBidder("alice", 600));
a.open();
a.placeBid("bob", 500);          // accepted (== reserve)
a.placeBid("alice", 510);        // alice's manual bid wins the floor race
a.placeBid("bob", 530);          // bob raises; auto-bidder answers 540
Bid winner = a.close();          // alice @ 540 (reserve met)
```

### Design points

- **One ladder formula** — `max(reserve, current + increment)` is the single acceptance rule; no special cases.
- **Notify inside the lock** — bid observers see the ladder in order; a nested auto-bid is safe (same thread re-enters).
- **Close is terminal and idempotent-safe** — the second `close()` throws; winner is computed from final state.
- **Reserve guards the seller** — a close without a qualifying bid returns `null` — a real outcome, not an error.

**Complexity:** placeBid O(observers) · close O(observers) · storage O(bids).

---
#lld #machine-coding #auction #medium #practice