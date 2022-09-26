####  using modulo to save the ans and original num
```
for i in range(n):
nums[i] = nums[i] + (n * (nums[nums[i]] % n) )
```
Retreiving the ans:
```
for i in range(n):
nums[i] = nums[i] // n
```
**# nums[i] // n always gives 0 (as 0 < nums[i] < n)**
**# second_term // n gives the req answer**
***# % is to get the value back in to the range when prev value is accessed (which would be greater than n in some case)***
​