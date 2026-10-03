# Design a Playlist Iterator

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Pattern:** Iterator
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-playlist-iterator)

### Problem

A music playlist holds songs. Provide a way to traverse them **sequentially** without exposing the
playlist's internal storage, and make it work with a standard loop.

### Approach — Iterator

- `Playlist` implements `Iterable<Song>` so `for-each` works.
- `iterator()` returns a fresh iterator whose traversal state lives **inside the iterator**, not the
  playlist.

### Java Solution

```java
import java.util.*;

final class Song {
    private final String title;
    Song(String title) { this.title = title; }
    @Override public String toString() { return title; }
}

class Playlist implements Iterable<Song> {
    private final List<Song> songs = new ArrayList<>();

    Playlist add(Song s) { songs.add(s); return this; }

    @Override
    public Iterator<Song> iterator() {          // fresh iterator per call
        return new Iterator<Song>() {
            private int index = 0;              // traversal state lives here
            @Override public boolean hasNext() { return index < songs.size(); }
            @Override public Song next() {
                if (!hasNext()) throw new NoSuchElementException();
                return songs.get(index++);
            }
        };
    }
}
```

**Usage**
```java
Playlist playlist = new Playlist()
        .add(new Song("Song A"))
        .add(new Song("Song B"))
        .add(new Song("Song C"));

for (Song s : playlist) System.out.println(s);     // Song A / Song B / Song C
```

### Design points
- **Internal list hidden** — callers get an iterator, never the backing `List`.
- **Independent traversals** — each `iterator()` call returns a new cursor.
- **`Iterable`** — enables the enhanced for-loop and stream APIs.

**Complexity:** O(1) per `next` · Space O(1) per iterator

---
#iterator #lld #practice