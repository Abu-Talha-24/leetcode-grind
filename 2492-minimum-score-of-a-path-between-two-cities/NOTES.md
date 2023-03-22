*what I have to say ?
*
n = cities
**Adjacency Matrix -> Graph**
```
[
[], # a, b, distance, city 'a' and 'b' 'distance'
[],
[],
[],
]
```
​
**score of a path** : return the min distance road, in the whole path from 1 to n
​
### Brute Force:
1. Find the minimum distance
2. Check if any one of the two nodes in the min distance are connected to the final node
DFS from the both nodes to find connectivity
```
if true:
return
else:
check w/ the next least path
```