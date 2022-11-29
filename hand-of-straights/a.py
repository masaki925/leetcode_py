from typing import List
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = {}
        for n in hand:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1

        minHeap = list(counts.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            for i in range(first, first + groupSize):
                if i in counts:
                    counts[i] -= 1
                    if counts[i] == 0:
                        if i == minHeap[0]:
                            heapq.heappop(minHeap)
                        else:
                            return False
                else:
                    return False

        return True


s = Solution()
# print(s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
print(s.isNStraightHand([1, 2, 3, 4, 5], 4))
