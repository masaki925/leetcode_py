from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, _next=None, random=None):
        self.val = int(x)
        self.next = _next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        hm = {None: None}

        curr = head
        while curr:
            hm[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            hm[curr].next = hm[curr.next]
            hm[curr].random = hm[curr.random]
            curr = curr.next

        return hm[head]


n1 = Node(x=1, _next=None, random=None)
n2 = Node(x=2, _next=None, random=None)
n3 = Node(x=3, _next=None, random=None)
n4 = Node(x=4, _next=None, random=None)
n5 = Node(x=5, _next=None, random=None)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

n2.random = n1
n3.random = n5
n4.random = n3
n5.random = n1

sol = Solution()

res = sol.copyRandomList(n1)

while res:
    print(f"{res.val=}")
    res = res.next
