### DFS
​
the last recursive call return means that
How is it backtracked ?
- keeps going on `root.left` all the way till it reaches leaf node `Null`
- if on the way target is reached it returns `True`
- if goes past leaf(**base case**) returns `False` it moves to check `root.right` recurs call.
​
If  found the last recursive line returns `True`.
else till last node it goes False the or condition returns False
​