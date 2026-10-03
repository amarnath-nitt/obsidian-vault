# Design a Social Network like Facebook - Practice

## Key Concepts
- **Friendship is two writes** — accept adds the edge to both adjacency sets; removal deletes both
- **BFS depth 2 finds suggestions** — friends-of-friends minus self minus existing friends, ranked by mutuals
- **Feed = merge + sort** — collect friends' posts, sort by time desc, cap; fan-out-on-read keeps posts simple

## Common Moves in LLD
1. **Requests are pending edges** — a separate `pending` map keeps accepted vs proposed friendships distinct
2. **Mutual ranking** — count which candidate appears from most friends; ties break by insertion order
3. **Observer for side effects** — accept → notify both; post → feed workers/notifications, decoupled
4. **Cap the feed** — a limit parameter now; cursor pagination when the model grows

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design a Social Network like Facebook](solutions/Design-Social-Network.md) — Medium · Observer, Strategy, Graph

---

## Extra Practice (self-study)

- [ ] Add blocked users — a block hides posts and stops suggestions both ways
- [ ] Add pagination — feed cursor as `(timestamp, postId)` for stable paging
- [ ] Add mutual-friend listing — reuse the BFS internals for "3 mutual friends"

## Tips
- Say **"the graph is the product"** — adjacency + BFS beats any memoized friend list
- Keep pending requests separate from edges — mixed semantics is the classic bug
- Feed first, ranking later — recency is honest and testable

---

#lld #machine-coding #social-network #medium #practice