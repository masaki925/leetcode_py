from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            k -= 1

            if k == 0:
                return cur.val

            cur = cur.right


root = TreeNode(
    val=3, left=TreeNode(val=1, left=None, right=TreeNode(val=2)), right=TreeNode(val=4)
)
k = 2

sol = Solution()
print(sol.kthSmallest(root, k))
