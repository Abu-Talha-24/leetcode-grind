**stn.**   0  1  2  3  4
**gas**   [1, 2, 3, 4, 5]
**cost**  [3, 4, 5, 1, 2]
#### 1 - Brute Force: - TLE
Time Complexity: O(n^2)
Check all posibilities if it reaches the same station
```
n = len(gas)
res = 0
for i in range(n):
j = i
tank = gas[j] # fill tank at start station
while tank >= cost[j]: # check if enough fuel to next station
tank -= cost[j] # cost of travel
j = 0 if j == n-1 else j + 1
tank += gas[j] # fill at next station
if j == i:  # circle complete
return i
return -1
```