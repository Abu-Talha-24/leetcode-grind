# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # go through linked lists making pairs and merging UNTIL ONE LIST IS LEFT
        
        def merge(l1, l2):
            dummy = head = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                head = head.next
            while l1:
                head.next = l1
                l1 = l1.next
                head = head.next
            while l2:
                head.next = l2
                l2 = l2.next
                head = head.next
                
            return dummy.next
        
        merged = []
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged.append(merge(l1, l2))
            lists = merged
        
        return lists[0] if lists else None
        