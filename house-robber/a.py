from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0

        for i in range(1, len(nums)):
            tmp = max(one + nums[i], two)
            one = two
            two = tmp

        return two


s = Solution()
print(s.rob([0, 0]))
# print(s.rob([1, 2, 3, 1]))
