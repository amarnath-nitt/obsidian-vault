# Alien Dictionary

**LeetCode 269** · Hard

### Problem
Given sorted list of words in alien language, find the alien alphabet order.

### Approach

1. Compare adjacent words char by char → find first difference → edge `c1 → c2`
2. Topological sort on character graph
3. If `word2` is prefix of `word1` → invalid ("abc" before "ab" is wrong)

```java
public String alienOrder(String[] words) {
    Map<Character, Set<Character>> adj = new HashMap<>();
    Map<Character, Integer> inDegree = new HashMap<>();
    for (String w : words) for (char c : w.toCharArray()) {
        adj.putIfAbsent(c, new HashSet<>());
        inDegree.putIfAbsent(c, 0);
    }

    for (int i = 0; i < words.length - 1; i++) {
        String w1 = words[i], w2 = words[i+1];
        if (w1.length() > w2.length() && w1.startsWith(w2)) return "";
        for (int j = 0; j < Math.min(w1.length(), w2.length()); j++) {
            if (w1.charAt(j) != w2.charAt(j)) {
                if (!adj.get(w1.charAt(j)).contains(w2.charAt(j))) {
                    adj.get(w1.charAt(j)).add(w2.charAt(j));
                    inDegree.merge(w2.charAt(j), 1, Integer::sum);
                }
                break;
            }
        }
    }

    Queue<Character> queue = new LinkedList<>();
    for (char c : inDegree.keySet()) if (inDegree.get(c) == 0) queue.offer(c);
    StringBuilder sb = new StringBuilder();
    while (!queue.isEmpty()) {
        char c = queue.poll();
        sb.append(c);
        for (char next : adj.get(c))
            if (inDegree.merge(next, -1, Integer::sum) == 0) queue.offer(next);
    }
    return sb.length() == inDegree.size() ? sb.toString() : "";
}
```

#sde-sheet #graphs #topological-sort #day23
