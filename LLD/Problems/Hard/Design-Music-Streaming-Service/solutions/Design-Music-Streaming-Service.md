# Design Music Streaming Service like Spotify (Hard)

**Difficulty:** Hard · **Patterns:** State, Strategy, Observer
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design music streaming: catalogue + playlists, a player state machine with next/previous, shuffle and repeat strategies, play-count events, and tier gating.

**Functional**
- Search songs; playlists add/remove; play/pause/stop/next/previous; repeat OFF/ONE/ALL; shuffle toggle.
- Play-count observers on every playback; FREE tier keeps shuffle forced on.

**Non-functional**
- Illegal transitions throw; shuffle is swappable; unshuffling restores the original order.

### The failure, before

```java
// ❌ `boolean playing` + `int index` loose in the service: pause-then-next behaves
// like play-then-next, shuffle mutates the playlist in place (unshuffle impossible),
// and repeat-ONE restarts by index arithmetic that breaks at the edges.
// if (playing) index++;   // pause semantics? repeat? shuffle? all undefined.
```

### The Fix (after)

Player state machine + original/queue pair + `ShuffleStrategy` + play observers.

```java
import java.util.*;

class Song {
    final String id, title, artist; final int seconds;
    Song(String id, String title, String artist, int seconds) {
        this.id = id; this.title = title; this.artist = artist; this.seconds = seconds;
    }
}

class Playlist {
    final String name; final List<Song> songs = new ArrayList<>();
    Playlist(String name) { this.name = name; }
    void add(Song s) { songs.add(s); }
    void remove(Song s) { songs.remove(s); }
}

enum PlaybackState { STOPPED, PLAYING, PAUSED }
enum Repeat { OFF, ONE, ALL }

interface ShuffleStrategy { void arrange(List<Song> queue); }

class InOrder implements ShuffleStrategy {
    public void arrange(List<Song> queue) { /* leave as loaded */ }
}

class FisherYates implements ShuffleStrategy {
    private final Random rnd = new Random();
    public void arrange(List<Song> queue) {
        for (int i = queue.size() - 1; i > 0; i--) {
            int j = rnd.nextInt(i + 1);
            Collections.swap(queue, i, j);
        }
    }
}

interface PlayCountObserver { void onPlay(Song song); }

class Player {
    private final List<Song> original = new ArrayList<>();     // as loaded / as listed
    private final List<Song> queue = new ArrayList<>();        // current play order
    private final List<PlayCountObserver> observers = new ArrayList<>();
    private int index = 0;
    private PlaybackState state = PlaybackState.STOPPED;
    private Repeat repeat = Repeat.OFF;
    private ShuffleStrategy shuffle = new InOrder();

    void subscribe(PlayCountObserver o) { observers.add(o); }

    void load(List<Song> songs) {
        if (songs.isEmpty()) throw new IllegalArgumentException("Nothing to load");
        original.clear(); original.addAll(songs);
        queue.clear(); queue.addAll(songs);
        shuffle.arrange(queue);
        index = 0;
        state = PlaybackState.STOPPED;
    }

    void play() {
        if (queue.isEmpty()) throw new IllegalStateException("Nothing loaded");
        state = PlaybackState.PLAYING;
        observers.forEach(o -> o.onPlay(current()));           // every start counts once
    }
    void pause() {
        if (state != PlaybackState.PLAYING) throw new IllegalStateException("Not playing");
        state = PlaybackState.PAUSED;
    }
    void stop() { state = PlaybackState.STOPPED; }

    Song current() { return queue.get(index); }

    void next() {
        if (queue.isEmpty()) throw new IllegalStateException("Nothing loaded");
        if (repeat == Repeat.ONE) { play(); return; }          // same track, counts again
        if (index + 1 < queue.size()) index++;
        else if (repeat == Repeat.ALL) index = 0;
        else { state = PlaybackState.STOPPED; return; }        // end of queue
        if (state == PlaybackState.PLAYING) observers.forEach(o -> o.onPlay(current()));
    }
    void previous() {
        if (queue.isEmpty()) throw new IllegalStateException("Nothing loaded");
        if (index > 0) index--;
    }

    void setRepeat(Repeat r) { repeat = r; }

    void setShuffle(boolean on) {
        shuffle = on ? new FisherYates() : new InOrder();
        Song now = queue.isEmpty() ? null : current();
        queue.clear();
        queue.addAll(original);
        shuffle.arrange(queue);
        if (now != null) index = Math.max(0, queue.indexOf(now));   // keep the playing track
    }
    PlaybackState state() { return state; }
}

class MusicService {
    private final Map<String, Song> catalogue = new LinkedHashMap<>();
    private final Map<String, Playlist> playlists = new LinkedHashMap<>();
    private final Map<String, Player> players = new HashMap<>();
    private final Set<String> premium = new HashSet<>();

    void addSong(Song s) { catalogue.put(s.id, s); }
    void upgrade(String userId) { premium.add(userId); }
    Player playerOf(String userId) { return players.computeIfAbsent(userId, k -> new Player()); }

    List<Song> search(String q) {
        String needle = q.toLowerCase();
        return catalogue.values().stream()
                .filter(s -> s.title.toLowerCase().contains(needle)
                          || s.artist.toLowerCase().contains(needle))
                .toList();
    }
    Playlist createPlaylist(String name) {
        Playlist p = new Playlist(name);
        playlists.put(name, p);
        return p;
    }
    void setShuffle(String userId, boolean on) {
        if (!on && !premium.contains(userId))
            throw new IllegalStateException("Shuffle stays on for FREE — upgrade to choose order");
        playerOf(userId).setShuffle(on);
    }
}
```

**Usage**
```java
MusicService svc = new MusicService();
svc.addSong(new Song("s1", "Kesariya", "Arijit Singh", 268));
svc.addSong(new Song("s2", "Tum Hi Ho", "Arijit Singh", 262));

Playlist chill = svc.createPlaylist("Chill");
chill.add(svc.search("Kesariya").get(0));
chill.add(svc.search("Tum Hi Ho").get(0));

Player p = svc.playerOf("u1");
p.load(chill.songs);
p.subscribe(song -> System.out.println("play: " + song.title));
p.play();          // play: Kesariya
p.next();          // play: Tum Hi Ho
p.setRepeat(Repeat.ONE);
p.next();          // play: Tum Hi Ho (again)

svc.setShuffle("u1", true);   // allowed: shuffle is on for everyone
svc.setShuffle("u1", false);  // throws: FREE tier
```

### Design points
- **State machine in `play/pause/stop`** — pausing from STOPPED throws; the media-player clichés stay legal-only.
- **Original vs queue** — shuffle re-arranges a copy; unshuffle restores by rebuilding from `original`.
- **Repeat lives in `next()`** — ONE replays, ALL wraps, OFF stops; previous never wraps.
- **Tier gating at the facade** — `MusicService` enforces FREE vs PREMIUM; `Player` stays policy-free.

**Complexity:** play/next O(1) (+observers) · shuffle O(n) · search O(catalogue).

---
#lld #machine-coding #spotify #hard #practice