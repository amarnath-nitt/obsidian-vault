# Design Stack Overflow (Easy)

**Difficulty:** Easy · **Patterns:** Observer, Strategy
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a Q&A forum: users ask questions, post answers, vote, comment; reputation and badges follow from votes.

**Functional**
- Post **questions** (title, body, tags); post **answers**; accept one answer.
- **Vote** +1/−1 on questions and answers; **comment** on both.
- **Reputation** on upvote/downvote/accept; **badges** at thresholds; **notifications** on answers/comments/accepts.

**Non-functional**
- Pluggable vote weights (`VotingStrategy`); vote → reputation → badge fan-out without coupling.

### The failure, before

```java
// ❌ Reputation math inside vote(), badges inside reputation(), notifications everywhere —
// adding "downvote costs the voter" touches five methods.
public void vote(Post p, int v) { p.score += v; user.rep += v * 10; checkBadges(user); notifyAll(...); }
```

### The Fix (after)

`Votable` interface + `VotingStrategy` + Observer services for reputation/badges/notifications.

```java
import java.util.*;

class User {
    private final String name;
    private int reputation = 1;
    private final Set<String> badges = new HashSet<>();
    User(String name) { this.name = name; }
    public String getName() { return name; }
    public int getReputation() { return reputation; }
    public void addReputation(int d) { reputation = Math.max(1, reputation + d); }
    public void award(String b) { badges.add(b); }
    public Set<String> getBadges() { return Set.copyOf(badges); }
}

class Vote {
    private final User voter; private final int value;   // +1 / -1
    Vote(User voter, int value) { this.voter = voter; this.value = value; }
    public User getVoter() { return voter; }
    public int getValue() { return value; }
}

interface VotingStrategy { int weight(Vote v, boolean isQuestion); }

class DefaultVoting implements VotingStrategy {
    public int weight(Vote v, boolean isQuestion) {
        if (v.getValue() > 0) return isQuestion ? 5 : 10;
        return -2;
    }
}

interface VoteListener { void onVote(Votable post, Vote vote); }

interface Votable {
    void addVote(Vote v);
    User getAuthor();
    int getScore();
}

abstract class Post implements Votable {
    protected final User author;
    protected final String body;
    protected int score = 0;
    protected final Map<String, Vote> votesByUser = new HashMap<>();
    protected final List<String> comments = new ArrayList<>();
    protected final List<VoteListener> listeners = new ArrayList<>();
    protected final VotingStrategy voting = new DefaultVoting();

    protected Post(User author, String body) { this.author = author; this.body = body; }
    public void subscribe(VoteListener l) { listeners.add(l); }
    public void addComment(String c) { comments.add(c); }
    public User getAuthor() { return author; }
    public int getScore() { return score; }

    public void addVote(Vote v) {
        if (votesByUser.containsKey(v.getVoter().getName()))
            throw new IllegalStateException("Already voted");
        votesByUser.put(v.getVoter().getName(), v);
        score += v.getValue();
        author.addReputation(voting.weight(v, this instanceof Question));
        for (VoteListener l : listeners) l.onVote(this, v);   // fan-out: badges, feeds
    }
}

class Question extends Post {
    private final String title;
    private final List<String> tags = new ArrayList<>();
    private final List<Answer> answers = new ArrayList<>();
    private Answer accepted;
    private boolean closed;
    Question(User author, String title, String body, List<String> tags) {
        super(author, body); this.title = title; this.tags.addAll(tags);
    }
    public void addAnswer(Answer a) {
        if (closed) throw new IllegalStateException("Closed");
        answers.add(a);
    }
    public void accept(Answer a) {
        if (!answers.contains(a)) throw new IllegalArgumentException("Not an answer here");
        accepted = a; a.markAccepted();
        a.getAuthor().addReputation(15); author.addReputation(2);
    }
    public List<Answer> getAnswers() { return List.copyOf(answers); }
}

class Answer extends Post {
    private boolean accepted;
    Answer(User author, String body) { super(author, body); }
    void markAccepted() { accepted = true; }
    public boolean isAccepted() { return accepted; }
}

class BadgeService implements VoteListener {
    public void onVote(Votable post, Vote vote) {
        User u = post.getAuthor();
        if (u.getReputation() >= 1000) u.award("GOLD");
        else if (u.getReputation() >= 500) u.award("SILVER");
        else if (u.getReputation() >= 100) u.award("BRONZE");
    }
}
```

**Usage**
```java
User alice = new User("alice"), bob = new User("bob");
Question q = new Question(alice, "What is DCL?", "Explain double-checked locking", List.of("java"));
q.subscribe(new BadgeService());
Answer a = new Answer(bob, "volatile + two null checks...");
q.addAnswer(a); a.addVote(new Vote(alice, +1)); q.accept(a);
```

### Design points
- **One vote per user** — voter-keyed map; repeat vote rejected, not double-counted.
- **Strategy holds the numbers** — accept bonus, weights, thresholds change in one place.
- **Observers for side effects** — badges/notifications subscribe; `Post` never imports them.
- **Accept is a transaction** — marks answer, closes the loop, pays both sides.

**Complexity:** vote O(1) listeners · Space O(votes + comments).

---
#lld #machine-coding #stack-overflow #easy #practice
