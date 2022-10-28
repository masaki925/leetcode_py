from typing import List
import heapq


class Twitter:
    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        self.follow(userId, userId)

        for fId in self.follows[userId]:
            if fId in self.tweets:
                tweet = self.tweets[fId][-1]
                maxHeap.append(
                    (tweet[0], tweet[1], fId, -1)
                )  # count, tweetId, followeeId, index

        heapq.heapify(maxHeap)
        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            index -= 1
            if len(self.tweets[followeeId]) >= abs(index):
                tweet = self.tweets[followeeId][index]
                heapq.heappush(maxHeap, (tweet[0], tweet[1], followeeId, index))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:

twitter = Twitter()
twitter.postTweet(1, 5)  # User 1 posts a new tweet (id = 5).
print(
    twitter.getNewsFeed(1)
)  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2)  # // User 1 follows user 2.
twitter.postTweet(2, 6)  # User 2 posts a new tweet (id = 6).
print(
    twitter.getNewsFeed(1)
)  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2)  # User 1 unfollows user 2.
print(
    twitter.getNewsFeed(1)
)  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
