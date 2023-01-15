from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = deque()
        q.append(root)
        res.append([root.val])

        while q:
            tmp = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    tmp.append(cur.left.val)
                if cur.right:
                    q.append(cur.right)
                    tmp.append(cur.right.val)

            if tmp:
                res.append(tmp)

        return res


s = Solution()
root = TreeNode(
    3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
)

print(s.levelOrder(root))
