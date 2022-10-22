from typing import List

digitToChars = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        sub = []

        def dfs(i):
            if i >= len(digits):
                res.append("".join(sub))
                return

            chars = digitToChars[digits[i]]
            for c in chars:
                sub.append(c)
                dfs(i + 1)
                sub.pop()

        if digits:
            dfs(0)

        return res


s = Solution()
print(f'{s.letterCombinations("23")=}')
