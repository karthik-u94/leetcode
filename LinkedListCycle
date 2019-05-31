# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if(head==None):
            return False
        slow=fast=head
        while(slow.next!=None and fast.next!=None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(slow.val==fast.val):
                return True
        return False
