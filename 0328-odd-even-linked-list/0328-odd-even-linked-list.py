# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
            
        curr = head
        evenHead = head.next
        
        while curr.next and curr.next.next :
            even = curr.next#2, 
            curr.next = curr.next.next
            curr = curr.next # 3
            even.next = curr.next
        
        curr.next = evenHead
        
        return head
            
        
        
        