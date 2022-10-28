from typing import List
from collections import defaultdict
import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(lambda: 0)
        for t in tasks:
            count[t] += 1
        maxHeap = [-i for i in count.values()]
        heapq.heapify(maxHeap)

        q = deque()

        time = 0
        while maxHeap or q:
            time += 1
            if q and q[0][0] < time:
                _, todo = q.popleft()
                heapq.heappush(maxHeap, todo)
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task:
                    q.append([time + n, task])

        return time


s = Solution()
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(s.leastInterval(tasks, n))
