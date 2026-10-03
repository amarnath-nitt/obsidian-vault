# Design Team Directory (Aggregation)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Relationship:** Aggregation
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-team-directory)

### Problem

Design a directory of **teams**, each containing **members**. A member belongs to the organisation
independently and may sit on **several** teams; a team references its members but does not own them.
This shared "has-a" is **aggregation**.

### Approach — Aggregation

- `Member` and `Team` are independent entities.
- `Team` holds references to members (can be shared across teams).
- A `Directory` indexes teams by name.

### Java Solution

```java
import java.util.*;

public record Member(String id, String name) {}

public class Team {

    private final String name;
    private final Set<Member> members = new LinkedHashSet<>();   // references, not ownership

    public Team(String name) { this.name = name; }

    public void addMember(Member member) { members.add(member); }   // share, don't consume
    public boolean removeMember(Member member) { return members.remove(member); }

    public String name() { return name; }
    public Set<Member> members() { return Set.copyOf(members); }
    public int size() { return members.size(); }
}

public class Directory {

    private final Map<String, Team> teams = new LinkedHashMap<>();

    public Team createTeam(String name) { return teams.computeIfAbsent(name, Team::new); }
    public Team team(String name) { return teams.get(name); }

    /** Which teams a member belongs to (they can be in many). */
    public List<String> teamsOf(Member member) {
        List<String> result = new ArrayList<>();
        teams.forEach((name, team) -> { if (team.members().contains(member)) result.add(name); });
        return result;
    }
}
```

**Usage**
```java
Directory directory = new Directory();
Member alice = new Member("M1", "Alice");     // created independently

Team platform = directory.createTeam("Platform");
Team security = directory.createTeam("Security");

platform.addMember(alice);
security.addMember(alice);                     // the SAME member is in two teams

directory.teamsOf(alice);                      // [Platform, Security]
```

### Why Aggregation
- **Shared parts** — one member belongs to multiple teams.
- **Independent lifetime** — deleting a team does not delete its members.
- **Weak ownership** — the team holds references it was given.

**Complexity:** O(1) add/remove · O(teams × members) for `teamsOf` · Space O(memberships)

---
#oop #aggregation #lld #practice