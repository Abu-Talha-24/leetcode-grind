### the infamous merging of two lists
​
##### You can (maybe should)
1. Use dummy nodes
```
dummy = ListNode()
return dummy.next
```
2. Use tail (as pointer) to track the end
* head and tail are initially the same
* tail keeps changing accordingly
​