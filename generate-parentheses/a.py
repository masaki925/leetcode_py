from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(leftN, rightN):
            if leftN == rightN == n:
                res.append("".join(stack))

            if leftN > n or rightN > n:
                return

            stack.append("(")
            dfs(leftN + 1, rightN)
            stack.pop()

            if leftN > rightN:
                stack.append(")")
                dfs(leftN, rightN + 1)
                stack.pop()

            return

        dfs(0, 0)

        return res


s = Solution()
print(s.generateParenthesis(3))
