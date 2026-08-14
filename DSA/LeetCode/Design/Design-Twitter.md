# Design Twitter

**LeetCode Problem:** [355. Design Twitter](https://leetcode.com/problems/design-twitter/)  
**Difficulty:** Medium  
**Topic:** Design, Hash Table, Heap, Linked List

---

## Problem Statement

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and see the 10 most recent tweets in the user's news feed.

Implement the `Twitter` class:

- `Twitter()` Initializes your twitter object.
- `void postTweet(int userId, int tweetId)` Composes a new tweet with ID tweetId by the user userId.
- `List<Integer> getNewsFeed(int userId)` Retrieves the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
- `void follow(int followerId, int followeeId)` The user with ID followerId started following the user with ID followeeId.
- `void unfollow(int followerId, int followeeId)` The user with ID followerId started unfollowing the user with ID followeeId.

---

## Examples

### Example 1:
```
Input:
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

Output:
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation:
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return [6, 5]. Tweet 6 should come before 5 because it is posted after 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return [5].
```

---

## Approach: HashMap + Max Heap

### Key Insights:
1. **Tweet Storage**: Each user has a list of tweets (chronological order)
2. **Following System**: HashMap of userId -> Set of followees
3. **News Feed**: Merge K sorted lists using Max Heap (Priority Queue)
4. **Timestamp**: Use global counter to order tweets

### Data Structures:
- `HashMap<userId, List<Tweet>>`: User's tweets
- `HashMap<userId, Set<followeeId>>`: Following relationships
- Tweet class: (tweetId, timestamp)
- Max Heap: To merge recent tweets from multiple users

---

## Java Implementation

```java
class Twitter {
    // Tweet class with timestamp for ordering
    class Tweet {
        int tweetId;
        int timestamp;
        
        Tweet(int tweetId, int timestamp) {
            this.tweetId = tweetId;
            this.timestamp = timestamp;
        }
    }
    
    private static int timeCounter = 0; // Global timestamp
    private HashMap<Integer, List<Tweet>> userTweets; // userId -> tweets
    private HashMap<Integer, Set<Integer>> following; // userId -> followees
    
    public Twitter() {
        userTweets = new HashMap<>();
        following = new HashMap<>();
    }
    
    public void postTweet(int userId, int tweetId) {
        userTweets.putIfAbsent(userId, new ArrayList<>());
        userTweets.get(userId).add(new Tweet(tweetId, timeCounter++));
    }
    
    public List<Integer> getNewsFeed(int userId) {
        // Max heap to get 10 most recent tweets
        PriorityQueue<Tweet> maxHeap = new PriorityQueue<>(
            (a, b) -> b.timestamp - a.timestamp
        );
        
        // Add user's own tweets
        if (userTweets.containsKey(userId)) {
            maxHeap.addAll(userTweets.get(userId));
        }
        
        // Add tweets from people the user follows
        if (following.containsKey(userId)) {
            for (int followeeId : following.get(userId)) {
                if (userTweets.containsKey(followeeId)) {
                    maxHeap.addAll(userTweets.get(followeeId));
                }
            }
        }
        
        // Get top 10 most recent tweets
        List<Integer> newsFeed = new ArrayList<>();
        int count = 0;
        
        while (!maxHeap.isEmpty() && count < 10) {
            newsFeed.add(maxHeap.poll().tweetId);
            count++;
        }
        
        return newsFeed;
    }
    
    public void follow(int followerId, int followeeId) {
        // Can't follow yourself
        if (followerId == followeeId) {
            return;
        }
        
        following.putIfAbsent(followerId, new HashSet<>());
        following.get(followerId).add(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        if (following.containsKey(followerId)) {
            following.get(followerId).remove(followeeId);
        }
    }
}
```

---

## Optimized Implementation (More Efficient getNewsFeed)

**Instead of adding all tweets to heap, use k-way merge with indices**

```java
class Twitter {
    class Tweet {
        int tweetId;
        int timestamp;
        
        Tweet(int tweetId, int timestamp) {
            this.tweetId = tweetId;
            this.timestamp = timestamp;
        }
    }
    
    // Custom class for heap to track which list and position
    class HeapNode {
        Tweet tweet;
        int userId;
        int index; // Position in user's tweet list
        
        HeapNode(Tweet tweet, int userId, int index) {
            this.tweet = tweet;
            this.userId = userId;
            this.index = index;
        }
    }
    
    private static int timeCounter = 0;
    private HashMap<Integer, List<Tweet>> userTweets;
    private HashMap<Integer, Set<Integer>> following;
    
    public Twitter() {
        userTweets = new HashMap<>();
        following = new HashMap<>();
    }
    
    public void postTweet(int userId, int tweetId) {
        userTweets.putIfAbsent(userId, new ArrayList<>());
        userTweets.get(userId).add(new Tweet(tweetId, timeCounter++));
    }
    
    public List<Integer> getNewsFeed(int userId) {
        List<Integer> newsFeed = new ArrayList<>();
        
        // Max heap based on timestamp
        PriorityQueue<HeapNode> maxHeap = new PriorityQueue<>(
            (a, b) -> b.tweet.timestamp - a.tweet.timestamp
        );
        
        // Get all users to fetch tweets from (self + followees)
        Set<Integer> users = new HashSet<>();
        users.add(userId);
        if (following.containsKey(userId)) {
            users.addAll(following.get(userId));
        }
        
        // Add most recent tweet from each user to heap
        for (int user : users) {
            if (userTweets.containsKey(user)) {
                List<Tweet> tweets = userTweets.get(user);
                if (!tweets.isEmpty()) {
                    int lastIndex = tweets.size() - 1;
                    maxHeap.offer(new HeapNode(tweets.get(lastIndex), user, lastIndex));
                }
            }
        }
        
        // Extract top 10 tweets
        while (!maxHeap.isEmpty() && newsFeed.size() < 10) {
            HeapNode node = maxHeap.poll();
            newsFeed.add(node.tweet.tweetId);
            
            // Add next tweet from same user if available
            if (node.index > 0) {
                int nextIndex = node.index - 1;
                List<Tweet> tweets = userTweets.get(node.userId);
                maxHeap.offer(new HeapNode(tweets.get(nextIndex), node.userId, nextIndex));
            }
        }
        
        return newsFeed;
    }
    
    public void follow(int followerId, int followeeId) {
        if (followerId == followeeId) return;
        
        following.putIfAbsent(followerId, new HashSet<>());
        following.get(followerId).add(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        if (following.containsKey(followerId)) {
            following.get(followerId).remove(followeeId);
        }
    }
}
```

---

## Complexity Analysis

### Approach 1 (Simple):
- **postTweet**: O(1)
- **follow**: O(1)
- **unfollow**: O(1)
- **getNewsFeed**: O(N × log N)
  - N = total tweets from user + followees
  - Add all to heap, then extract 10

### Approach 2 (Optimized):
- **postTweet**: O(1)
- **follow**: O(1)
- **unfollow**: O(1)
- **getNewsFeed**: O(k × log k) where k = number of users (self + followees)
  - Only need to process 10 tweets maximum
  - Much better when users have many tweets

**Space**: O(U × T) where U = users, T = tweets per user

---

## Key Points for Interviews

1. **Why Max Heap?**
   - Need to efficiently get most recent tweets
   - Heap gives us O(log n) insertion and extraction
   - Alternative: sort entire list (O(n log n))

2. **Timestamp Strategy:**
   - Global counter ensures correct ordering
   - More recent tweets have higher timestamps
   - No need for actual time (Date/Time objects)

3. **Follow/Unfollow:**
   - Use HashSet for O(1) add/remove
   - Handle self-following edge case
   - Don't create unnecessary entries

4. **Edge Cases:**
   - User follows themselves
   - User has no tweets
   - User follows no one
   - Less than 10 tweets available
   - Unfollow someone not followed

5. **Optimization: K-Way Merge**
   - Only process what's needed (10 tweets)
   - Instead of adding ALL tweets to heap
   - Add most recent from each user, then incrementally fetch older

6. **Common Mistakes:**
   - Not handling user following themselves
   - Forgetting to include user's own tweets
   - Wrong heap comparator (min instead of max)
   - Not checking if user/tweets exist

7. **Follow-up Questions:**
   - How to handle millions of users?
   - How to implement like/retweet?
   - How to add real-time updates?
   - How to implement trending topics?

---

## Visual Example

```
Users and Tweets:
User 1: [Tweet5 (t=0)]
User 2: [Tweet6 (t=1), Tweet7 (t=3)]
User 3: [Tweet8 (t=2)]

Following:
User 1 follows: {2, 3}

getNewsFeed(1):
1. Get tweets from: user 1, 2, 3
2. Max Heap (by timestamp):
   [Tweet7(t=3), Tweet8(t=2), Tweet6(t=1), Tweet5(t=0)]
3. Extract top 10: [7, 8, 6, 5]
4. Return: [7, 8, 6, 5]
```

---

## Related Problems

- [[LRU-Cache|146. LRU Cache]]
- [[Design-HashMap|706. Design HashMap]]
- [1286. Iterator for Combination](https://leetcode.com/problems/iterator-for-combination/)
- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

---

## Tags

`#design` `#hash-table` `#heap` `#priority-queue` `#medium` `#merge-k-lists`
