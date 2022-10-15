from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            val = []
            for i in range(len(queue)):
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                val.append(cur.val)
            res.append(val)

        return res


root = TreeNode(
    val=3,
    left=TreeNode(val=9),
    right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)),
)

sol = Solution()

print(sol.levelOrder(root))
