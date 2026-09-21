# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head:
            return
        dummy = ListNode(0,head)
        first = dummy
        sec = dummy
        
        for _ in range(n+1):
            first = first.next

        while first:
            first = first.next
            sec = sec.next

        sec.next = sec.next.next  
        
        return dummy.next
        