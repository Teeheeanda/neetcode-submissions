# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        l, n = 0, len(lists)

        if n == 0:
            return ;
        if n == 1:
            return lists[0]
        
        s = (l+n) // 2 

        left = self.mergeKLists(lists[l:s])
        right = self.mergeKLists(lists[s:n+1])
        
        if not left:
            return right
        if not right:
            return left

        dummy = node = ListNode()

        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next

        node.next = left or right

        return dummy.next



