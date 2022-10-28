from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        candidates.sort()

        def backtrack(i, total):
            if total == target:
                res.append(sub.copy())
                return

            if i >= len(candidates) or total > target:
                return

            sub.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            sub.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, total)

        backtrack(0, 0)

        return res


s = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(s.combinationSum2(candidates, target))
