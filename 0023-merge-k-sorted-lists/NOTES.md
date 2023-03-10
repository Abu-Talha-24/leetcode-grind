```
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
```