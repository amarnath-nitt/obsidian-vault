# Design Playlist Library (Aggregation)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Relationship:** Aggregation
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-playlist-library)

### Problem

Design a music library that groups **playlists**, where each playlist holds **songs**. A playlist can
be added to many libraries and can outlive any single library — so the library **aggregates**
playlists rather than owning them.

### Approach — Aggregation

- `Song` is a simple value.
- `Playlist` holds a list of songs (aggregation of songs too).
- `Library` holds references to playlists that were created elsewhere — the playlists survive the
  library.

### Java Solution

```java
import java.util.*;

public record Song(String title, String artist, int seconds) {}

public class Playlist {
    private final String name;
    private final List<Song> songs = new ArrayList<>();

    public Playlist(String name) { this.name = name; }

    public Playlist add(Song song) { songs.add(song); return this; }
    public String name() { return name; }
    public List<Song> songs() { return List.copyOf(songs); }
    public int totalSeconds() { return songs.stream().mapToInt(Song::seconds).sum(); }
}

public class Library {

    // Aggregation: the library references playlists it does NOT own.
    private final List<Playlist> playlists = new ArrayList<>();

    public void addPlaylist(Playlist playlist) { playlists.add(playlist); }
    public boolean removePlaylist(Playlist playlist) { return playlists.remove(playlist); }

    public int playlistCount() { return playlists.size(); }
    public List<Playlist> playlists() { return List.copyOf(playlists); }

    public int totalSeconds() {
        int total = 0;
        for (Playlist p : playlists) total += p.totalSeconds();   // recurses into aggregated parts
        return total;
    }
}
```

**Usage**
```java
Playlist chill = new Playlist("Chill").add(new Song("Sunrise", "A", 210))
                                      .add(new Song("Drift", "B", 190));

Library homeLibrary = new Library();
homeLibrary.addPlaylist(chill);       // aggregate, not own

Library sharedLibrary = new Library();  // the SAME playlist can belong to another library
sharedLibrary.addPlaylist(chill);

homeLibrary.totalSeconds();            // 400
```

### Why Aggregation
- **Shared parts** — `chill` belongs to two libraries simultaneously.
- **Independent lifetime** — removing the playlist from a library does not delete it.
- **Weak ownership** — the library holds references, not exclusive control.

### Aggregation vs Composition
If the library *created* the playlists internally and they could not exist without it, this would be
**composition**. Here the playlists are passed in and shared → **aggregation**.

**Complexity:** O(playlists × songs) for totals · Space O(playlists)

---
#oop #aggregation #lld #practice