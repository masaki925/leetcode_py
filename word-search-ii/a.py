from typing import List


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        root = TrieNode()
        res = set()
        visit = set()

        for word in words:
            root.add(word)

        def dfs(r, c, node, curWord):
            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or board[r][c] not in node.children
                or (r, c) in visit
            ):
                return

            curWord += board[r][c]
            node = node.children[board[r][c]]
            visit.add((r, c))
            if node.isWord:
                res.add(curWord)

            dfs(r + 1, c, node, curWord)
            dfs(r - 1, c, node, curWord)
            dfs(r, c + 1, node, curWord)
            dfs(r, c - 1, node, curWord)

            visit.remove((r, c))

            return

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)


s = Solution()
# board = [
#     ["o", "a", "a", "n"],
#     ["e", "t", "a", "e"],
#     ["i", "h", "k", "r"],
#     ["i", "f", "l", "v"],
# ]
# words = ["oath", "pea", "eat", "rain"]
# print(s.findWords(board, words))

# board = [["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]]
# words = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]
# print(s.findWords(board, words))

board = [["a", "b"], ["a", "a"]]
words = ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]
print(s.findWords(board, words))
