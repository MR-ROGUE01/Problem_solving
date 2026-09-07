# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0

        # Count nodes
        while curr:
            count += 1
            curr = curr.next

        # Middle index
        mid = count // 2
        curr = head

        # Move to middle
        for i in range(mid):
            curr = curr.next
        return curr

        