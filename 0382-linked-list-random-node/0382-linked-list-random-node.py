# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        curr = self.head
        while curr:
            self.length += 1
            curr = curr.next
        
    def getRandom(self) -> int:
        node_num = random.randint(1, self.length)
        curr = ListNode(0)
        curr.next = self.head
        while node_num:
            curr = curr.next
            node_num -= 1
        return curr.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()