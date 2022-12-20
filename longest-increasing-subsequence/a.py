from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            res = max(res, dp[i])

        return res


s = Solution()
print(s.lengthOfLIS([1, 9]))
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
