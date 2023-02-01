from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minN = prices[0]

        for n in prices:
            if n < minN:
                minN = n

            res = max(res, n - minN)

        return res


s = Solution()
# print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
