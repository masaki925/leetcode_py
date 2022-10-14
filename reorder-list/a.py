from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        while fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        second = prev

        while second:
            tmp1 = head.next
            tmp2 = second.next
            head.next = second
            second.next = tmp1
            head = tmp1
            second = tmp2


l1 = ListNode(val=1)
l2 = ListNode(val=2)
l3 = ListNode(val=3)
l4 = ListNode(val=4)

l1.next = l2
l2.next = l3
l3.next = l4

sol = Solution()
sol.reorderList(l1)

cur = l1
while cur:
    print(f"{cur.val=}")
    cur = cur.next
