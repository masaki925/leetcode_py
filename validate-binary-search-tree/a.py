from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.root = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minN, maxN):
            if not node:
                return True

            # print(f"{node.val=}, {minN=}, {maxN=}")
            if node.val <= minN:
                return False
            if maxN <= node.val:
                return False
            return dfs(node.left, minN, node.val) and dfs(node.right, node.val, maxN)

        return dfs(root, float("-inf"), float("inf"))

    def buildTree(self, i, nums: List[int]) -> None:
        n = len(nums)
        if n == 0:
            return None

        def inner(i=0):
            if n <= i or nums[i] is None:
                return None

            node = TreeNode(nums[i])
            node.left = inner(2 * i + 1)
            node.right = inner(2 * i + 2)
            return node

        return inner()

    def showTree(self, node):
        if not node:
            return

        print(f"{node.val=}")

        if node.left:
            self.showTree(node.left)
        else:
            print("None")
        if node.right:
            self.showTree(node.right)
        else:
            print("None")


s = Solution()
s.root = s.buildTree(0, [5, 1, 4, None, None, 3, 6])
# s.showTree(s.root)
print(s.isValidBST(s.root))
