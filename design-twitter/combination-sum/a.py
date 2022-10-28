from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def backtrack(i, total):
            if total == target:
                res.append(sub.copy())
                return

            if i >= len(candidates) or total > target:
                return

            sub.append(candidates[i])
            backtrack(i, total + candidates[i])
            sub.pop()
            backtrack(i + 1, total)

        backtrack(0, 0)

        return res


s = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(s.combinationSum(candidates, target))
