# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        head_cp = head
        head_cp2 = head_cp
        while head and n > 0:
            head = head.next
            n -= 1

        if not head:
            head_cp = head_cp.next
            return head_cp

        while head and head.next:
            head = head.next
            head_cp = head_cp.next

        if head_cp and head_cp.next:
            head_cp.next = head_cp.next.next
        return head_cp2