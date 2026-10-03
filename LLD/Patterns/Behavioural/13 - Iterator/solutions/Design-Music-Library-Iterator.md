# Design a Music Library Iterator

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Iterator
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-music-library-iterator)

### Problem

A music library stores tracks with an artist and album. Support **multiple traversal orders** over
the *same* collection — all tracks, only a given artist, or in a shuffled order — without exposing
the internal storage.

### Approach — Iterator

- One `MusicLibrary` aggregate; several iterator factory methods.
- Each iterator encapsulates its own ordering/filtering logic.
- The library never leaks its internal `List`.

### Java Solution

```java
import java.util.*;

final class Track {
    final String title, artist, album;
    Track(String title, String artist, String album) {
        this.title = title; this.artist = artist; this.album = album;
    }
    @Override public String toString() { return artist + " – " + title; }
}

class MusicLibrary {
    private final List<Track> tracks = new ArrayList<>();

    MusicLibrary add(Track t) { tracks.add(t); return this; }

    /** Iterate every track in insertion order. */
    public Iterable<Track> all() {
        return () -> tracks.iterator();
    }

    /** Iterate only the tracks by one artist. */
    public Iterable<Track> byArtist(String artist) {
        return () -> new FilteredIterator(tracks.iterator(), t -> t.artist.equals(artist));
    }

    /** Iterate the tracks in a shuffled order. */
    public Iterable<Track> shuffled(Random random) {
        return () -> {
            List<Track> copy = new ArrayList<>(tracks);
            Collections.shuffle(copy, random);
            return copy.iterator();
        };
    }

    // Reusable filtering iterator
    private static final class FilteredIterator implements Iterator<Track> {
        private final Iterator<Track> source;
        private final java.util.function.Predicate<Track> predicate;
        private Track next;
        FilteredIterator(Iterator<Track> source, java.util.function.Predicate<Track> predicate) {
            this.source = source; this.predicate = predicate;
        }
        @Override public boolean hasNext() {
            while (next == null && source.hasNext()) {
                Track candidate = source.next();
                if (predicate.test(candidate)) next = candidate;
            }
            return next != null;
        }
        @Override public Track next() {
            if (!hasNext()) throw new NoSuchElementException();
            Track t = next; next = null; return t;
        }
    }
}
```

**Usage**
```java
MusicLibrary lib = new MusicLibrary()
        .add(new Track("Song 1", "Adele", "25"))
        .add(new Track("Song 2", "Coldplay", "Parachutes"))
        .add(new Track("Song 3", "Adele", "21"));

for (Track t : lib.byArtist("Adele")) System.out.println(t);   // only Adele tracks
for (Track t : lib.shuffled(new Random(1))) System.out.println(t);
```

### Design points
- **One collection, many iterators** — ordering/filtering is a property of the iterator.
- **Lazy filtering** — the `FilteredIterator` pulls from the source only as needed.
- **Encapsulation** — the library exposes `Iterable` views, never the backing list.

**Complexity:** O(1) amortised per `next` · Space O(1) (O(n) for a shuffled copy)

---
#iterator #lld #practice