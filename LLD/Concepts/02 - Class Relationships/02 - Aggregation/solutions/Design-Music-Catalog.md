# Design Music Catalog (Aggregation)

**Source:** AlgoMaster · Low-Level Design Practice · **hard** · **Relationship:** Aggregation
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-music-catalog)

### Problem

Design a music catalog organised as **artists → albums → tracks**. The catalog **aggregates** artists;
an artist aggregates albums; an album aggregates tracks. Each level can exist on its own — a track can
be featured on a compilation, an album can be re-released under a different label — so these are
**aggregation** relationships, not composition.

### Approach — Aggregation (multi-level)

- `Track` is a value object (title, duration).
- `Album` holds a list of tracks it aggregates.
- `Artist` holds a list of albums it aggregates.
- `MusicCatalog` indexes artists and answers queries.

### Java Solution

```java
import java.util.*;

public record Track(String title, int seconds) {}

public class Album {
    private final String title;
    private final List<Track> tracks = new ArrayList<>();   // aggregates (tracks may reappear elsewhere)

    public Album(String title) { this.title = title; }
    public Album add(Track track) { tracks.add(track); return this; }

    public String title() { return title; }
    public List<Track> tracks() { return List.copyOf(tracks); }
    public int duration() { return tracks.stream().mapToInt(Track::seconds).sum(); }
}

public class Artist {
    private final String name;
    private final List<Album> albums = new ArrayList<>();    // aggregates albums

    public Artist(String name) { this.name = name; }
    public Artist add(Album album) { albums.add(album); return this; }

    public String name() { return name; }
    public List<Album> albums() { return List.copyOf(albums); }
    public int catalogueSeconds() {
        int total = 0;
        for (Album a : albums) total += a.duration();        // recurses into aggregated parts
        return total;
    }
}

public class MusicCatalog {
    private final Map<String, Artist> artists = new LinkedHashMap<>();

    public Artist artist(String name) { return artists.computeIfAbsent(name, Artist::new); }

    /** Adds a track to an album, creating the album/artist chain as needed. */
    public void addTrack(String artistName, String albumTitle, Track track) {
        Artist artist = artist(artistName);
        Album album = artist.albums().stream()
                .filter(a -> a.title().equals(albumTitle)).findFirst()
                .orElseGet(() -> { Album a = new Album(albumTitle); artist.add(a); return a; });
        album.add(track);
    }

    public Set<String> artistNames() { return artists.keySet(); }
    public int totalTracks() {
        int total = 0;
        for (Artist a : artists.values()) for (Album al : a.albums()) total += al.tracks().size();
        return total;
    }
}
```

**Usage**
```java
MusicCatalog catalog = new MusicCatalog();
catalog.addTrack("Adele", "25",   new Track("Hello", 295));
catalog.addTrack("Adele", "25",   new Track("Send My Love", 223));
catalog.addTrack("Adele", "21",   new Track("Rolling in the Deep", 228));

catalog.artist("Adele").catalogueSeconds();   // 746
catalog.totalTracks();                         // 3
```

### Why Aggregation (at every level)
- **Shared/reusable parts** — tracks and albums outlive any single catalog or artist.
- **Independent lifetimes** — removing an artist does not destroy their albums elsewhere.
- **Weak ownership** — each level references the parts it was given.

**Complexity:** O(1) index, O(catalog) aggregates · Space O(tracks)

---
#oop #aggregation #lld #practice