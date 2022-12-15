from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        nums = set()
        for triplet in triplets:
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue

            for i, v in enumerate(triplet):
                if v == target[i]:
                    nums.add(i)

        return len(nums) == 3


s = Solution()
# print(s.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]))
# print(s.mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]))
print(s.mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]))
