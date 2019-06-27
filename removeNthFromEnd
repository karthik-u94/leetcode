# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None) # dummy matters
        dummy.next = head
        ptr1 = ptr2 = dummy
        while n:
            ptr2 = ptr2.next
            n -= 1
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = ptr1.next.next
        return dummy.next
