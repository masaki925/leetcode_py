from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0

        while r < len(nums) - 1:
            maxJamp = 0
            for i in range(l, r + 1):
                maxJamp = max(maxJamp, i + nums[i])
            l = r + 1
            r = maxJamp
            res += 1

        return res


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
