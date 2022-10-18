from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left  = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

    def printTree(self, root):
        if not root:
            return

        print(root.val)
        self.printTree(root.left)
        self.printTree(root.right)


preo = [3, 9, 10, 20, 15, 7]
ino = [9, 10, 3, 15, 20, 7]


sol = Solution()
root = sol.buildTree(preo, ino)

sol.printTree(root)

