from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            if nums[i] in hm:
                return [i, hm[nums[i]]]

            hm[target - nums[i]] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
