# Design a Social Network like Facebook (Medium)

**Difficulty:** Medium · **Patterns:** Observer, Strategy, Graph
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a social network: users, mutual friendships (accept flow), posts with likes/comments, a friends' feed, and friends-of-friends suggestions.

**Functional**
- Friend requests: send, accept, remove — friendship mutual when accepted.
- Posts with likes/comments; feed = own + friends' posts newest first; suggestions ranked by mutuals.

**Non-functional**
- Suggestions run BFS depth 2 (no all-pairs scan); feed caps at a limit.

### The failure, before

```java
// ❌ A `List<User> friends` per user with linear scans: accept forgets the reverse edge,
// suggestions compare every pair, and the feed rebuilds a sorted list from scratch per read.
// if (!a.friends.contains(b)) a.friends.add(b);   // and b? never gets the reverse edge.
```

### The Fix (after)

Mutual adjacency map + depth-2 BFS suggestions + merge-and-sort feed + observer hooks.

```java
import java.util.*;

class Post {
    final String id, authorId, text; final long at;
    final Set<String> likes = new HashSet<>();
    final List<String> comments = new ArrayList<>();
    Post(String id, String authorId, String text, long at) { this.id = id; this.authorId = authorId; this.text = text; this.at = at; }
    void like(String userId) { likes.add(userId); }
    void comment(String userId, String text) { comments.add(userId + ": " + text); }
}

interface NotificationObserver {
    default void onFriendAccepted(String a, String b) {}
    default void onPost(Post post) {}
}

class SocialNetwork {
    private final Map<String, String> users = new LinkedHashMap<>();               // id → name
    private final Map<String, Set<String>> friends = new HashMap<>();              // mutual edges
    private final Map<String, Set<String>> pending = new HashMap<>();              // directed requests
    private final Map<String, List<Post>> postsByUser = new HashMap<>();
    private final List<NotificationObserver> observers = new ArrayList<>();
    private int postSeq = 0;

    void join(String id, String name) { users.put(id, name); }
    void subscribe(NotificationObserver o) { observers.add(o); }
    void sendRequest(String from, String to) { pending.computeIfAbsent(from, k -> new HashSet<>()).add(to); }

    void accept(String from, String to) {
        onesided(to, from);                                       // a stale request check
        friends.computeIfAbsent(from, k -> new HashSet<>()).add(to);
        friends.computeIfAbsent(to, k -> new HashSet<>()).add(from);   // both directions, always
        pending.getOrDefault(from, Set.of()).remove(to);
        observers.forEach(o -> o.onFriendAccepted(from, to));
    }
    private void onesided(String from, String to) {
        if (!pending.getOrDefault(to, Set.of()).contains(from))
            throw new IllegalStateException(to + " never requested " + from);
    }

    void unfriend(String a, String b) {
        friends.getOrDefault(a, Set.of()).remove(b);
        friends.getOrDefault(b, Set.of()).remove(a);
    }

    Post post(String userId, String text, long at) {
        Post p = new Post("P" + (++postSeq), userId, text, at);
        postsByUser.computeIfAbsent(userId, k -> new ArrayList<>()).add(p);
        observers.forEach(o -> o.onPost(p));
        return p;
    }

    List<Post> feed(String userId, int limit) {
        List<Post> merged = new ArrayList<>(postsByUser.getOrDefault(userId, List.of()));
        for (String f : friends.getOrDefault(userId, Set.of()))
            merged.addAll(postsByUser.getOrDefault(f, List.of()));
        merged.sort(Comparator.comparingLong((Post p) -> p.at).reversed());
        return merged.size() <= limit ? merged : merged.subList(0, limit);
    }

    List<String> suggestions(String userId) {
        Set<String> direct = friends.getOrDefault(userId, Set.of());
        Map<String, Integer> mutuals = new HashMap<>();
        for (String f : direct)                                   // BFS depth 2, counted
            for (String fof : friends.getOrDefault(f, Set.of()))
                if (!fof.equals(userId) && !direct.contains(fof))
                    mutuals.merge(fof, 1, Integer::sum);
        return mutuals.entrySet().stream()
                .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
                .map(Map.Entry::getKey)
                .toList();
    }
}
```

**Usage**
```java
SocialNetwork sn = new SocialNetwork();
sn.join("u1", "Asha"); sn.join("u2", "Bharat"); sn.join("u3", "Chen");
sn.sendRequest("u1", "u2"); sn.accept("u1", "u2");
sn.sendRequest("u1", "u3"); sn.accept("u1", "u3");
sn.sendRequest("u2", "u3"); sn.accept("u2", "u3");
sn.post("u2", "hello feed", 1_000);
sn.join("u4", "Divya");
sn.sendRequest("u3", "u4"); sn.accept("u3", "u4");
System.out.println(sn.suggestions("u1"));   // [u4] — friend of u3, not yet a friend
```

### Design points
- **Friendship writes both directions** — accept adds the edge twice; unfriend removes it twice; no drift.
- **Pending ≠ accepted** — requests live in their own map; `accept` validates the request really exists.
- **Suggestions are BFS depth 2 with counts** — `merge` counts mutuals; the top candidates are ranked, not guessed.
- **Feed merge is the fan-out** — fan-out-on-read keeps posts cheap; the sort + limit is one honest line.

**Complexity:** accept O(1) · feed O(posts log posts) · suggestions O(Σ friends-of-friends) ≈ O(E).

---
#lld #machine-coding #social-network #medium #practice