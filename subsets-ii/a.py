from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sub = []

        def backtrack(i):
            if i >= len(nums):
                res.append(sub.copy())
                return

            sub.append(nums[i])
            backtrack(i + 1)
            sub.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)

        return res


s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
