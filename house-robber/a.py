from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0

        for n in nums:
            tmp = max(one + n, two)
            one = two
            two = tmp

        return two


s = Solution()
print(s.rob([1]))
# print(s.rob([1, 2, 3, 1]))
