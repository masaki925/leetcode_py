from typing import List

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x != y:
                new = x - y
                heapq.heappush(maxHeap, new)

        return -maxHeap[0] if maxHeap else 0


s = Solution()
print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))
