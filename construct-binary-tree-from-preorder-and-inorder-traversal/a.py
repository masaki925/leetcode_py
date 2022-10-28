from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

preo = [3, 9, 10, 20, 15, 7]
ino = [9, 10, 3, 15, 20, 7]


sol = Solution()
root = sol.buildTree(preo, ino)

sol.printTree(root)

