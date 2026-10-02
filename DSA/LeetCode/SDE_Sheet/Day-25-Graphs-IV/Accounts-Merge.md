# Accounts Merge

**LeetCode 721** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/accounts-merge/)

### Problem
Merge accounts that share common emails.

### Approach (DSU on emails)

1. Map each email to an account index
2. For each account, union all emails with the first email
3. Group emails by their root (representative)
4. Build result

```java
class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        DSU dsu = new DSU(accounts.size());
        Map<String, Integer> emailToAccount = new HashMap<>();

        for (int i = 0; i < accounts.size(); i++) {
            for (int j = 1; j < accounts.get(i).size(); j++) {
                String email = accounts.get(i).get(j);
                if (emailToAccount.containsKey(email)) {
                    dsu.union(i, emailToAccount.get(email));
                } else {
                    emailToAccount.put(email, i);
                }
            }
        }

        Map<Integer, List<String>> rootToEmails = new HashMap<>();
        for (Map.Entry<String, Integer> entry : emailToAccount.entrySet()) {
            int root = dsu.find(entry.getValue());
            rootToEmails.computeIfAbsent(root, k -> new ArrayList<>()).add(entry.getKey());
        }

        List<List<String>> result = new ArrayList<>();
        for (Map.Entry<Integer, List<String>> entry : rootToEmails.entrySet()) {
            List<String> emails = entry.getValue();
            Collections.sort(emails);
            emails.add(0, accounts.get(entry.getKey()).get(0)); // add name
            result.add(emails);
        }
        return result;
    }
}
```

---
