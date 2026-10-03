# Design Follow Graph (Association)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Relationship:** Association
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-follow-graph)

### Problem

Design a social follow graph. **Users** follow other **users** — a **self-association** (a user is
associated with other users) with no ownership in either direction. Support follow, unfollow, listing
who a user follows, who follows a user, and mutual-follow detection.

### Approach — Association (self-referential)

- `User` is an independent entity.
- The `FollowGraph` stores an adjacency set `Map<User, Set<User>>` of "follows" edges.
- Deletion of an edge must remove it from both directions of lookup.

### Java Solution

```java
import java.util.*;

public record User(String id) {}

public class FollowGraph {

    private final Map<User, Set<User>> following = new HashMap<>();   // a -> set of whom a follows
    private final Map<User, Set<User>> followers = new HashMap<>();   // b -> set of who follows b

    public void follow(User a, User b) {
        if (a.equals(b)) throw new IllegalArgumentException("cannot follow yourself");
        following.computeIfAbsent(a, k -> new HashSet<>()).add(b);
        followers.computeIfAbsent(b, k -> new HashSet<>()).add(a);
    }

    public boolean unfollow(User a, User b) {
        boolean removed = following.getOrDefault(a, Set.of()).remove(b);
        if (removed) followers.getOrDefault(b, Set.of()).remove(a);
        return removed;
    }

    public Set<User> following(User a) { return Set.copyOf(following.getOrDefault(a, Set.of())); }
    public Set<User> followers(User b) { return Set.copyOf(followers.getOrDefault(b, Set.of())); }

    public boolean isMutual(User a, User b) {
        return following(a).contains(b) && following(b).contains(a);
    }

    public int followingCount(User a) { return following(a).size(); }
    public int followerCount(User b)  { return followers(b).size(); }
}
```

**Usage**
```java
FollowGraph graph = new FollowGraph();
User alice = new User("alice");
User bob   = new User("bob");

graph.follow(alice, bob);
graph.follow(bob, alice);
graph.isMutual(alice, bob);        // true
graph.followers(bob).size();       // 1
graph.unfollow(alice, bob);        // true
graph.following(alice).size();     // 0
```

### Why Association
- **Independent entities** — deleting a user does not delete the users they follow.
- **Peer relationship** — no ownership in either direction.
- **Self-referential** — users associate with other users (many-to-many).
- Two indexes (following/followers) make both directions O(1).

**Complexity:** O(1) follow/unfollow · Space O(edges)

---
#oop #association #lld #practice