from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = tmp

        return root

    def printTree(self, root):
        if not root:
            return
        print(f"{root.val=}")
        self.printTree(root.left)
        self.printTree(root.right)


s = Solution()
# root = [4, 2, 7, 1, 3, 6, 9]
root = TreeNode(
    val=4,
    left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)),
    right=TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=9)),
)

inv = s.invertTree(root)
s.printTree(inv)
