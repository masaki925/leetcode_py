from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minn, maxn):
            if not node:
                return True

            return (
                (minn < node.val)
                and (node.val < maxn)
                and dfs(node.left, minn, node.val)
                and dfs(node.right, node.val, maxn)
            )

        return dfs(root, float("-inf"), float("inf"))


root = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))
# root = TreeNode(
#     val=5,
#     left=TreeNode(val=4),
#     right=TreeNode(val=6, left=TreeNode(val=3), right=TreeNode(val=7)),
# )

sol = Solution()
print(sol.isValidBST(root))
