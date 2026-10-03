# Design Slide Deck (Composition)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Relationship:** Composition
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-slide-deck)

### Problem

Design a presentation **slide deck**. A deck is made of **slides**, and a slide only makes sense as
part of its deck — delete the deck and its slides are gone. The deck **owns** its slides (composition)
and creates them internally.

### Approach — Composition

- `SlideDeck` creates and holds `Slide` objects internally.
- Slides are **never handed out** for others to own or share.
- Deleting the deck destroys its slides.

### Java Solution

```java
import java.util.*;

public class SlideDeck {

    private final String title;
    private final List<Slide> slides = new ArrayList<>();   // created & owned here

    public SlideDeck(String title) { this.title = title; }

    /** Creates a slide inside the deck — callers never construct slides themselves. */
    public Slide addSlide(String heading, String body) {
        Slide slide = new Slide(slides.size() + 1, heading, body);
        slides.add(slide);
        return slide;
    }

    public int slideCount() { return slides.size(); }
    public String title()   { return title; }

    /** Returns a read-only summary, not the live slides (keeps ownership exclusive). */
    public List<String> outline() {
        List<String> lines = new ArrayList<>();
        for (Slide s : slides) lines.add(s.number() + ". " + s.heading());
        return lines;
    }
}

/** Owned exclusively by a SlideDeck — its constructor is package-private. */
class Slide {
    private final int number;
    private final String heading;
    private final String body;

    Slide(int number, String heading, String body) {     // created only by SlideDeck
        this.number = number; this.heading = heading; this.body = body;
    }
    int number()     { return number; }
    String heading() { return heading; }
    String body()    { return body; }
}
```

**Usage**
```java
SlideDeck deck = new SlideDeck("LLD 101");
deck.addSlide("Intro", "What is LLD?");
deck.addSlide("OOP", "The four pillars");

deck.outline();      // ["1. Intro", "2. OOP"]
deck.slideCount();   // 2
```

### Why Composition
- **Exclusive ownership** — a slide belongs to exactly one deck.
- **Lifetime bound** — destroying the deck destroys its slides.
- **Creation internal** — the deck's `addSlide` is the only way to make a slide.
- **Parts not shared** — `outline()` returns strings, not `Slide` references.

**Complexity:** O(slides) per outline · Space O(slides)

---
#oop #composition #lld #practice