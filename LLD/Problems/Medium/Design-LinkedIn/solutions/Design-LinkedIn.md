# Design LinkedIn (Medium)

**Difficulty:** Medium · **Patterns:** Observer, Strategy
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a professional network: profiles, connection graph, posts + ranked feed, jobs + applications, messaging, notifications.

**Functional**
- **Profiles**; **invite/accept** connections; **posts** with like/comment; ranked **feed**; **jobs** + apply; recruiter notifications.

**Non-functional**
- Pluggable ranking; async fan-out; degree derived, never stored.

### The failure, before

```java
// ❌ Member with a feed list that the poster loops over inline — posting to 10k
// followers blocks; degree stored as an int that rots; jobs copy-paste the notify code.
public void post(String t) { for (Member f : followers) f.feed.add(t); }
```

### The Fix (after)

Directed connection edges + publish event + `FeedService` observer + ranking strategy.

```java
import java.util.*;

class Profile {
    private String headline; private final List<String> skills = new ArrayList<>();
    Profile(String headline) { this.headline = headline; }
    public void addSkill(String s) { skills.add(s); }
    public String snapshot() { return headline + " | " + String.join(",", skills); }
}

enum InviteStatus { PENDING, ACCEPTED }

class Member {
    private final String id;
    private final Profile profile;
    private final Set<String> connections = new HashSet<>();   // accepted, mutual ids
    private final List<Post> feed = new ArrayList<>();
    Member(String id, String headline) { this.id = id; this.profile = new Profile(headline); }
    public String getId() { return id; }
    public Profile getProfile() { return profile; }
    public void befriend(String other) { connections.add(other); }
    public boolean connected(String other) { return connections.contains(other); }
    public Set<String> getConnections() { return Set.copyOf(connections); }
    void deliver(Post p) { feed.add(p); }
    public List<Post> getFeed() { return List.copyOf(feed); }
}

class Post {
    private final String id; private final String text; private final String author;
    private final long ts = System.currentTimeMillis();
    private int likes;
    private final List<String> comments = new ArrayList<>();
    Post(String id, String author, String text) { this.id = id; this.author = author; this.text = text; }
    public String getAuthor() { return author; }
    public long getTs() { return ts; }
    public void like() { likes++; }
    public void comment(String c) { comments.add(c); }
    public int getLikes() { return likes; }
}

interface FeedRanking { double score(Post p, Member reader); }

class RecencyAffinityRanking implements FeedRanking {
    public double score(Post p, Member reader) {
        long ageMin = (System.currentTimeMillis() - p.getTs()) / 60000 + 1;
        double affinity = reader.connected(p.getAuthor()) ? 2.0 : 1.0;
        return (p.getLikes() + 1) * affinity / ageMin;   // engagement × affinity ÷ age
    }
}

interface PostListener { void onPost(Post p); }

class FeedService implements PostListener {
    private final Map<String, Member> members;
    private final FeedRanking ranking = new RecencyAffinityRanking();
    FeedService(Map<String, Member> members) { this.members = members; }
    public void onPost(Post p) {
        Member author = members.get(p.getAuthor());
        for (String cid : author.getConnections())   // fan-out to 1st degree
            members.get(cid).deliver(p);
        author.deliver(p);
    }
    public List<Post> readFeed(Member m) {
        List<Post> out = new ArrayList<>(m.getFeed());
        out.sort((a, b) -> Double.compare(ranking.score(b, m), ranking.score(a, m)));
        return out;
    }
}

class JobPosting {
    private final String id, title; private final String recruiterId;
    private final List<String> applications = new ArrayList<>();  // profile snapshots
    private final List<PostListener> dummy = new ArrayList<>();
    JobPosting(String id, String title, String recruiterId) {
        this.id = id; this.title = title; this.recruiterId = recruiterId;
    }
    public void apply(Member m, java.util.function.Consumer<String> notifyRecruiter) {
        applications.add(m.getId() + ": " + m.getProfile().snapshot());  // snapshot at apply time
        notifyRecruiter.accept("New application for " + title + " from " + m.getId());
    }
    public List<String> getApplications() { return List.copyOf(applications); }
}
```

**Usage**
```java
Map<String, Member> db = new HashMap<>();
Member amy = new Member("amy", "Backend Engineer"); Member bo = new Member("bo", "Recruiter");
db.put("amy", amy); db.put("bo", bo);
amy.befriend("bo"); bo.befriend("amy");
FeedService feeds = new FeedService(db);
Post p = new Post("p1", "amy", "Shipped our new cache layer");
feeds.onPost(p); p.like();
feeds.readFeed(bo);   // ranked: engagement × affinity ÷ age
```

### Design points
- **Edges are mutual ids, degree is BFS** — 2nd degree = friends-of-friends minus directs; nothing stored to rot.
- **Publish returns, fan-out follows** — the observer queue is the async boundary; posting never blocks on 10k writes.
- **Rank on read** — scores computed at read time so new likes reorder without rewrites.
- **Applications snapshot** — later profile edits can't rewrite history; recruiter notify rides the same event shape.

**Complexity:** post O(followers) fan-out · feed read O(n log n) rank · Space O(members + posts).

---
#lld #machine-coding #linkedin #medium #practice
