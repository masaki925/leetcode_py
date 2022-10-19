from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        items = []
        for p in points:
            items.append([(p[0] ** 2) + (p[1] ** 2), p[0], p[1]])

        heapq.heapify(items)

        for i in range(k):
            item = heapq.heappop(items)
            res.append([item[1], item[2]])

        return res


sol = Solution()
points = [[1, 3], [-2, 2]]
k = 1
print(sol.kClosest(points, k))
