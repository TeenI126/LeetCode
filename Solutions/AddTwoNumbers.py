# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_out = ListNode()
        curr1 = l1
        curr2 = l2
        curr_out = list_out
        carry = 0
        while curr1 is not None or curr2 is not None:
            n1 = 0
            if curr1 is not None:
                n1 = curr1.val
                curr1 = curr1.next

            n2 = 0
            if curr2 is not None:
                n2 = curr2.val
                curr2 = curr2.next

            s = carry + n1 + n2

            if s > 9:
                carry = 1
                curr_out.next = ListNode(s-10)
            else:
                carry = 0
                curr_out.next = ListNode(s)
            curr_out = curr_out.next
        if carry == 1:
            curr_out.next = ListNode(1)
        return list_out.next
