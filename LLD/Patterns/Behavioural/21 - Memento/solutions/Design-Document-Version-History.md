# Design a Document Version History

**Source:** AlgoMaster · Low-Level Design Practice · **hard (premium)** · **Pattern:** Memento
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

A collaborative document keeps a **history of versions**. Each save captures a snapshot; users can
list the versions and restore any earlier one. The history must not expose the document's internal
state representation, and it should be **bounded** so memory does not grow without limit.

### Approach — Memento

- **Originator** = `Document` — `snapshot()` returns a memento; `restore(m)` applies it.
- **Memento** = an immutable version snapshot with metadata (version number, timestamp).
- **Caretaker** = `VersionHistory` — a **bounded** list of snapshots (drops the oldest).

### Java Solution

```java
import java.util.*;

final class Document {                                      // Originator
    private String title = "";
    private String body = "";

    void edit(String title, String body) { this.title = title; this.body = body; }
    @Override public String toString() { return "\"" + title + "\": " + body; }

    Version snapshot(int versionNumber) {
        return new Version(versionNumber, title, body, System.currentTimeMillis());
    }
    void restore(Version v) { this.title = v.title(); this.body = v.body(); }

    /** Immutable, opaque snapshot with version metadata. */
    static final class Version {
        private final int number; private final String title, body; private final long timestamp;
        private Version(int number, String title, String body, long timestamp) {
            this.number = number; this.title = title; this.body = body; this.timestamp = timestamp;
        }
        private String title() { return title; }
        private String body()  { return body; }
        public int number()    { return number; }            // safe to expose
        public long timestamp(){ return timestamp; }
    }
}

class VersionHistory {                                      // Caretaker (bounded)
    private final Deque<Document.Version> versions = new ArrayDeque<>();
    private final int maxVersions;
    private int counter = 0;

    VersionHistory(int maxVersions) { this.maxVersions = maxVersions; }

    /** Capture a new version, dropping the oldest if the limit is exceeded. */
    Document.Version commit(Document doc) {
        Document.Version v = doc.snapshot(++counter);
        if (versions.size() == maxVersions) versions.removeLast();   // drop oldest
        versions.push(v);
        return v;
    }

    /** Restore a specific version number, or the latest if none given. */
    boolean restore(Document doc, int versionNumber) {
        for (Document.Version v : versions) {
            if (v.number() == versionNumber) { doc.restore(v); return true; }
        }
        return false;
    }
    List<Integer> availableVersions() {
        List<Integer> nums = new ArrayList<>();
        for (Document.Version v : versions) nums.add(v.number());
        return nums;
    }
}
```

**Usage**
```java
Document doc = new Document();
VersionHistory history = new VersionHistory(3);     // keep at most 3 versions

doc.edit("Draft", "Hello");
history.commit(doc);
doc.edit("Draft", "Hello world");
history.commit(doc);
doc.edit("Final", "Hello world!");
history.commit(doc);

System.out.println(history.availableVersions());     // [3, 2, 1]

doc.edit("Final", "Hello world!!!");
history.commit(doc);                                  // drops the oldest (v1)
System.out.println(history.availableVersions());     // [4, 3, 2]

history.restore(doc, 2);
System.out.println(doc);                              // "Draft": Hello world
```

### Design points
- **Opaque memento** — only `Document` reads `title`/`body`; the history stores and returns versions.
- **Bounded history** — `maxVersions` caps memory growth (oldest dropped first).
- **Version numbers** — metadata the caretaker *may* expose without breaking encapsulation.

### Scaling note
For large documents, store **deltas** between versions instead of full snapshots, or persist
snapshots to storage rather than keeping them all in memory.

**Complexity:** O(1) commit, O(versions) restore · Space O(maxVersions × document size)

---
#memento #lld #practice