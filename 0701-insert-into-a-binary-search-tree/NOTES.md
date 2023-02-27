#### Trees -> Recursion !
##### Base Case:
if found leaf node (null children) return new node
```
if not root:
return node
```
#### The logic part
Connecting those nodes based on value
```
if val > root.val:
root.right = insert(root.right)
elif val < root.val:
root.left = insert(root.left)
​
```
​
return root