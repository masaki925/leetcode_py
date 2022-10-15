# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxn):
            r = 0
            if node.val >= maxn:
                r += 1

            if node.left:
                r += dfs(node.left, max(maxn, node.val))
            if node.right:
                r += dfs(node.right, max(maxn, node.val))

            return r

        return dfs(root, root.val)


root = TreeNode(
    val=3,
    left=TreeNode(val=1, left=TreeNode(val=3)),
    right=TreeNode(val=4, left=TreeNode(val=1), right=TreeNode(val=5)),
)

sol = Solution()
print(sol.goodNodes(root))
