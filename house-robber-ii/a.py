from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1_1, dp2_1 = 0, 0

        # nums[:-1]
        for n in nums[:-1]:
            tmp = max(dp1_1 + n, dp2_1)
            dp1_1 = dp2_1
            dp2_1 = tmp

        dp1_2, dp2_2 = 0, 0

        # nums[1:]
        for n in nums[1:]:
            tmp = max(dp1_2 + n, dp2_2)
            dp1_2 = dp2_2
            dp2_2 = tmp

        return max(dp2_1, dp2_2)


s = Solution()
nums = [1]
print(nums[1:])
# print(s.rob([2, 3, 2]))
# print(s.rob([1, 2, 3, 1]))
