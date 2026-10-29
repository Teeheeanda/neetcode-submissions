# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        hn = head.next

        while head and head.next:
            if abs(hn.val) > 1000:
                return True
            
            head.val = abs(head.val) + 1000
            head = head.next
            hn = hn.next
        
        return False
            



