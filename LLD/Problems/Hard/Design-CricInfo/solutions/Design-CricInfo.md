# Design CricInfo (Hard)

**Difficulty:** Hard · **Patterns:** Observer, Command
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design live cricket scoring: record ball events, update every stat, rotate strike, end innings, and fan out live updates.

**Functional**
- Record balls (0–6 runs, WIDE, NO_BALL, wicket); auto strike rotation and over-end; next batter on wicket.
- Live batter/bowler stats; innings ends at 10 wickets or over quota; chase result.

**Non-functional**
- Ball log is append-only and replayable; observers see only settled state.

### The failure, before

```java
// ❌ score updates sprinkled across the method: runs added in three places,
// `if (runs == 4) fours++` forgets the boundary rule, wides increment the ball count,
// and nobody can replay "what happened" — the log does not exist.
// score += r; balls++; if (r % 2 == 1) swap(); // extras? over-end? wickets? all adrift.
```

### The Fix (after)

Immutable `BallEvent`s applied in one method; every mutation ordered; observers notified once per ball.

```java
import java.util.*;

enum Extra { NONE, WIDE, NO_BALL }

record BallEvent(int runs, Extra extra, boolean wicket) {
    static BallEvent runs(int r) { return new BallEvent(r, Extra.NONE, false); }
    static BallEvent wicketBall() { return new BallEvent(0, Extra.NONE, true); }
    static BallEvent wide() { return new BallEvent(0, Extra.WIDE, false); }
    static BallEvent noBall(int r) { return new BallEvent(r, Extra.NO_BALL, false); }
}

class Batter {
    final String name; int runs, balls, fours, sixes;
    Batter(String name) { this.name = name; }
}

class Bowler {
    final String name; int balls, runs, wickets;
    Bowler(String name) { this.name = name; }
}

interface ScoreObserver { void onBall(Innings innings, BallEvent ball); }

class Innings {
    final String battingTeam;
    private final List<Batter> order; private int nextBatter = 2;    // openers: 0 and 1
    private int striker = 0, nonStriker = 1;
    private final List<ScoreObserver> observers = new ArrayList<>();
    final List<BallEvent> log = new ArrayList<>();                   // command log: replayable
    int runs, wickets, legalBalls;
    Bowler bowler;
    private final int ballQuota;

    Innings(String battingTeam, List<Batter> order, int ballQuota) {
        this.battingTeam = battingTeam; this.order = order; this.ballQuota = ballQuota;
    }
    void subscribe(ScoreObserver o) { observers.add(o); }
    void setBowler(Bowler b) { bowler = b; }
    Batter striker() { return order.get(striker); }
    Batter nonStriker() { return order.get(nonStriker); }
    boolean finished() { return wickets == 10 || legalBalls >= ballQuota; }
    int runs() { return runs; }

    void ball(BallEvent e) {
        if (finished()) throw new IllegalStateException("Innings over");
        Batter bat = order.get(striker);
        boolean legal = e.extra() == Extra.NONE;
        if (legal) { legalBalls++; bat.balls++; bowler.balls++; }

        int total = e.runs() + (legal ? 0 : 1);                     // extras always cost one
        runs += total; bowler.runs += total;
        bat.runs += e.runs();                                        // runs off the bat only
        if (legal && e.runs() == 4) bat.fours++;
        if (legal && e.runs() == 6) bat.sixes++;

        if (e.wicket()) {
            wickets++; bowler.wickets++;
            if (wickets < 10) striker = nextBatter < order.size() ? nextBatter++ : striker;
        } else if (legal && e.runs() % 2 == 1) {
            swap();                                                  // odd runs change ends
        }
        if (legal && legalBalls % 6 == 0 && !finished()) swap();     // end of over
        log.add(e);
        observers.forEach(o -> o.onBall(this, e));                   // after state settles
    }
    private void swap() { int t = striker; striker = nonStriker; nonStriker = t; }
    String scoreLine() { return battingTeam + " " + runs + "/" + wickets + " (" + legalBalls / 6
            + "." + legalBalls % 6 + ")"; }
}

class Match {
    final Innings first, second;
    Match(Innings first, Innings second) { this.first = first; this.second = second; }
    String result() {
        if (second.runs() >= first.runs()) return second.battingTeam + " won chasing";
        return first.battingTeam + " won by " + (first.runs() - second.runs()) + " runs";
    }
}
```

**Usage**
```java
List<Batter> order = new ArrayList<>();
order.add(new Batter("Rohit")); order.add(new Batter("Gill"));
for (int i = 2; i < 11; i++) order.add(new Batter("Batter-" + i));

Innings india = new Innings("India", order, 120);
india.setBowler(new Bowler("Starc"));
india.subscribe((inn, ball) -> System.out.println(inn.scoreLine()));

india.ball(BallEvent.runs(4));      // FOUR — no strike change
india.ball(BallEvent.runs(1));      // single — strike rotates
india.ball(BallEvent.wide());       // +1 run, ball NOT counted
india.ball(BallEvent.wicketBall()); // next batter in
```

### Design points
- **One mutation site per fact** — extras, bat runs, bowler runs, and boundaries each have exactly one line.
- **`legal` drives everything** — ball counts, over-end, and boundary credit all depend on the single legality flag.
- **The log is the system** — `BallEvent`s append in order; undo = drop the last event and replay the fold.
- **Observers fire once, after the ball settles** — commentary duplicates never diverge from the score.

**Complexity:** ball O(1) (+O(observers)) · innings replay O(balls).

---
#lld #machine-coding #cricinfo #hard #practice