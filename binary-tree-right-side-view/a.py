from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []

        if root:
            q.append(root)

        while q:
            val = None
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                val = cur.val
            res.append(val)

        return res


root = TreeNode(
    val=1,
    left=TreeNode(
        val=2, left=None, right=TreeNode(val=5, left=None, right=TreeNode(val=8))
    ),
    right=TreeNode(val=3, left=None, right=TreeNode(val=4)),
)


sol = Solution()

print(sol.rightSideView(root))
