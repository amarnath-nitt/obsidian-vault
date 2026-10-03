# Design Online Stock Brokerage System (Hard)

**Difficulty:** Hard · **Patterns:** Strategy, Observer
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a brokerage: limit/market orders, price-time priority matching with partial fills, cancels, portfolios with cost basis, funds/share checks.

**Functional**
- Place BUY/SELL limit (resting) or market (IOC) orders; match at best price, FIFO within a level.
- Partial fills keep the remainder; cancel open remainders; portfolios track shares and average cost.

**Non-functional**
- Deterministic matching; every trade settles cash and shares exactly once.

### The failure, before

```java
// ❌ A `List<Order> book` scanned linearly per new order, filled in arrival order
// regardless of price, with `if (buy.price == sell.price)` missing every better price;
// portfolio updates happen inline and double-count on partial fills.
// for (Order o : book) if (o.price == incoming.price) matchBoth(o, incoming);  // price-time? no.
```

### The Fix (after)

Two sorted books (`TreeMap<price, Deque<Order>>`), a crossing match loop, and one settlement path per trade.

```java
import java.util.*;

enum Side { BUY, SELL }
enum OrderType { LIMIT, MARKET }
enum OrderStatus { OPEN, PARTIAL, FILLED, CANCELLED }

class Order {
    final String id, userId, symbol; final Side side; final OrderType type; final long price;
    int remaining; OrderStatus status = OrderStatus.OPEN;
    Order(String id, String userId, String symbol, Side side, OrderType type, long price, int qty) {
        this.id = id; this.userId = userId; this.symbol = symbol;
        this.side = side; this.type = type; this.price = price; remaining = qty;
    }
    void fill(int qty) {
        remaining -= qty;
        status = remaining == 0 ? OrderStatus.FILLED : OrderStatus.PARTIAL;
    }
}

record Trade(String symbol, long price, int qty, String buyerId, String sellerId) {}

class OrderBook {
    private final TreeMap<Long, Deque<Order>> bids = new TreeMap<>(Comparator.reverseOrder());  // best bid first
    private final TreeMap<Long, Deque<Order>> asks = new TreeMap<>();                           // best ask first

    List<Trade> place(Order order) {
        List<Trade> trades = new ArrayList<>();
        TreeMap<Long, Deque<Order>> opposite = order.side == Side.BUY ? asks : bids;
        while (order.remaining > 0 && !opposite.isEmpty()) {
            Map.Entry<Long, Deque<Order>> best = opposite.firstEntry();
            long bookPrice = best.getKey();
            if (order.type == OrderType.LIMIT && !crosses(order, bookPrice)) break;
            Order counter = best.getValue().peekFirst();                    // FIFO at this price
            int qty = Math.min(order.remaining, counter.remaining);
            order.fill(qty);
            counter.fill(qty);
            String buyer  = order.side == Side.BUY ? order.userId : counter.userId;
            String seller = order.side == Side.BUY ? counter.userId : order.userId;
            trades.add(new Trade(order.symbol, bookPrice, qty, buyer, seller));
            if (counter.status == OrderStatus.FILLED) best.getValue().pollFirst();
            if (best.getValue().isEmpty()) opposite.remove(bookPrice);
        }
        if (order.remaining > 0) {
            if (order.type == OrderType.LIMIT) rest(order);                 // remainder waits
            else order.status = OrderStatus.CANCELLED;                      // market remainder: IOC
        }
        return trades;
    }
    private boolean crosses(Order order, long bookPrice) {
        return order.side == Side.BUY ? order.price >= bookPrice : order.price <= bookPrice;
    }
    private void rest(Order order) {
        (order.side == Side.BUY ? bids : asks)
                .computeIfAbsent(order.price, k -> new ArrayDeque<>()).addLast(order);
    }
    boolean cancel(Order order) {
        if (order.status == OrderStatus.FILLED || order.status == OrderStatus.CANCELLED) return false;
        TreeMap<Long, Deque<Order>> book = order.side == Side.BUY ? bids : asks;
        Deque<Order> queue = book.get(order.price);
        if (queue != null) {
            queue.remove(order);
            if (queue.isEmpty()) book.remove(order.price);
        }
        order.status = OrderStatus.CANCELLED;
        return true;
    }
}

class Portfolio {
    private final Map<String, Integer> shares = new HashMap<>();
    private final Map<String, Long> basis = new HashMap<>();                 // total cost

    void buy(String symbol, int qty, long price) {
        shares.merge(symbol, qty, Integer::sum);
        basis.merge(symbol, price * qty, Long::sum);
    }
    void sell(String symbol, int qty, long price) {
        shares.merge(symbol, -qty, Integer::sum);
        basis.merge(symbol, -avgCost(symbol) * qty, Long::sum);
    }
    long avgCost(String symbol) {
        int q = shares.getOrDefault(symbol, 0);
        return q == 0 ? 0 : basis.getOrDefault(symbol, 0L) / q;
    }
    int shares(String symbol) { return shares.getOrDefault(symbol, 0); }
}

class BrokerageService {
    private final Map<String, OrderBook> books = new HashMap<>();
    private final Map<String, Portfolio> portfolios = new HashMap<>();
    private final Map<String, Order> orders = new HashMap<>();
    private final Map<String, Long> cash = new HashMap<>();
    private int seq = 0;

    void deposit(String userId, long amount) { cash.merge(userId, amount, Long::sum); }

    synchronized Order placeOrder(String userId, String symbol, Side side, OrderType type, long price, int qty) {
        Portfolio pf = portfolios.computeIfAbsent(userId, k -> new Portfolio());
        if (side == Side.SELL && pf.shares(symbol) < qty)
            throw new IllegalStateException("Not enough shares");
        if (side == Side.BUY && type == OrderType.LIMIT && cash.getOrDefault(userId, 0L) < price * qty)
            throw new IllegalStateException("Insufficient funds");
        Order order = new Order("O" + (++seq), userId, symbol, side, type, price, qty);
        orders.put(order.id, order);
        List<Trade> trades = books.computeIfAbsent(symbol, k -> new OrderBook()).place(order);
        trades.forEach(this::settle);
        return order;
    }
    private void settle(Trade t) {                                           // one path, both sides
        cash.merge(t.buyerId(),  -t.price() * t.qty(), Long::sum);
        cash.merge(t.sellerId(), +t.price() * t.qty(), Long::sum);
        portfolios.computeIfAbsent(t.buyerId(),  k -> new Portfolio()).buy(t.symbol(), t.qty(), t.price());
        portfolios.computeIfAbsent(t.sellerId(), k -> new Portfolio()).sell(t.symbol(), t.qty(), t.price());
    }
    synchronized boolean cancel(String orderId) {
        Order order = orders.get(orderId);
        return books.get(order.symbol).cancel(order);
    }
    long cashOf(String userId) { return cash.getOrDefault(userId, 0L); }
    Portfolio portfolioOf(String userId) { return portfolios.get(userId); }
}
```

**Usage**
```java
BrokerageService broker = new BrokerageService();
broker.deposit("alice", 1_000_000);
broker.deposit("bob",   1_000_000);

broker.placeOrder("bob", "ACME", Side.SELL, OrderType.LIMIT, 100, 50);     // rests at 100
Order buy = broker.placeOrder("alice", "ACME", Side.BUY, OrderType.LIMIT, 105, 80);
// 50 filled @100 (bob's ask); alice's remaining 30 rests on the bid at 105
System.out.println(buy.status);                                          // PARTIAL
System.out.println(broker.portfolioOf("alice").shares("ACME"));          // 50
System.out.println(broker.cashOf("alice"));                              // 995,000
```

### Design points
- **Price-time priority, literally two structures** — `TreeMap` (price) over `Deque` (time); `firstEntry` + `peekFirst`.
- **The match loop is greedy and blind to sides** — cross test decides continuation; both orders update per fill.
- **IOC semantics for market orders** — a market remainder is cancelled, never rested.
- **Settlement once per trade** — cash and portfolios move in `settle`; no other code touches them.

**Complexity:** place O(fills × log P) · cancel O(1) + O(queue scan) · best bid/ask O(log P).

---
#lld #machine-coding #stock-brokerage #hard #practice