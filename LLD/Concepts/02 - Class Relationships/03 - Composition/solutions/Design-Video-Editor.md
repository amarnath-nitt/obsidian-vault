# Design Video Editor (Composition)

**Source:** AlgoMaster · Low-Level Design Practice · **hard** · **Relationship:** Composition
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-video-editor)

### Problem

Design a simple video editor. A **project** contains a **timeline**, and the timeline is made of
**clips** — segments of a media source with a start time and duration. A clip belongs to exactly one
timeline and cannot exist outside it: removing the timeline removes its clips. This is **composition**.

### Approach — Composition

- `Timeline` creates and owns `Clip` objects.
- `VideoProject` owns its `Timeline`.
- Clips are never shared between timelines; trimming/removing happens within the timeline.

### Java Solution

```java
import java.util.*;

public class Timeline {

    private final List<Clip> clips = new ArrayList<>();     // owned, exclusive

    /** Creates a clip owned by this timeline. */
    public Clip append(String source, int startSeconds, int durationSeconds) {
        if (durationSeconds <= 0) throw new IllegalArgumentException("duration must be > 0");
        Clip clip = new Clip(source, startSeconds, durationSeconds);
        clips.add(clip);
        return clip;
    }

    public boolean remove(Clip clip) { return clips.remove(clip); }
    public int clipCount()  { return clips.size(); }
    public int totalSeconds() {
        int total = 0;
        for (Clip c : clips) total += c.durationSeconds();
        return total;
    }
    /** A read-only render plan — returns text, not the live clips. */
    public List<String> renderPlan() {
        List<String> plan = new ArrayList<>();
        int at = 0;
        for (Clip c : clips) {
            plan.add(at + "s: " + c.source() + " [" + c.startSeconds() + "+" + c.durationSeconds() + "]");
            at += c.durationSeconds();
        }
        return plan;
    }
}

/** Exclusively owned by a Timeline (package-private constructor). */
class Clip {
    private final String source;
    private final int startSeconds;
    private int durationSeconds;

    Clip(String source, int startSeconds, int durationSeconds) {
        this.source = source; this.startSeconds = startSeconds; this.durationSeconds = durationSeconds;
    }
    String source()       { return source; }
    int startSeconds()    { return startSeconds; }
    int durationSeconds() { return durationSeconds; }
    void trimTo(int seconds) { durationSeconds = Math.max(1, seconds); }
}

public class VideoProject {
    private final String name;
    private final Timeline timeline = new Timeline();       // composed

    public VideoProject(String name) { this.name = name; }
    public Timeline timeline() { return timeline; }
    public String name() { return name; }
}
```

**Usage**
```java
VideoProject project = new VideoProject("Intro video");
Timeline timeline = project.timeline();

timeline.append("clip1.mp4", 0, 10);
timeline.append("clip2.mp4", 5, 12);

timeline.clipCount();      // 2
timeline.totalSeconds();   // 22
timeline.renderPlan();     // ["0s: clip1.mp4 [0+10]", "10s: clip2.mp4 [5+12]"]
```

### Why Composition
- **Exclusive ownership** — a clip belongs to exactly one timeline.
- **Lifetime bound** — deleting the project/timeline discards its clips.
- **Created internally** — `append` is the only way to create a clip.
- **Nested composition** — `VideoProject ◆── Timeline ◆── Clip`.

**Complexity:** O(clips) per aggregate · Space O(clips)

---
#oop #composition #lld #practice