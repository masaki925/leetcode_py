from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        tmp = 0

        for n in nums:
            tmp += n
            res = max(res, tmp)

            if tmp < 0:
                tmp = 0

        return res


s = Solution()
print(s.maxSubArray([-1]))
# print(s.maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
