### DFS
​
the last recursive call means that
How is it backtracked ?
- keeps going on `root.left` all the way till it reaches leaf `Null`
- if on the way target is reached it returns `True`
- if leaf node returns `False` it moves to check `root.right`.
​
Hence The last recursive line returns `True`.
​