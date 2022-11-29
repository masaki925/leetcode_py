from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1

        arr = []
        for i in range(len(nums) + 1):
            arr.append([])

        for key, val in counts.items():
            arr[val].append(key)

        res = []
        for a in arr[::-1]:
            for r in a:
                res.append(r)
                k -= 1
                if k == 0:
                    return res


s = Solution()
# print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(s.topKFrequent([1], 1))
