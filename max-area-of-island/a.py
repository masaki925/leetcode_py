from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c, total):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return total

            visit.add((r, c))
            total += 1

            total += dfs(r + 1, c, 0)
            total += dfs(r - 1, c, 0)
            total += dfs(r, c + 1, 0)
            total += dfs(r, c - 1, 0)

            return total

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(maxArea, dfs(r, c, 0))

        return maxArea


s = Solution()

grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]

print(f"{s.maxAreaOfIsland(grid)=}")
