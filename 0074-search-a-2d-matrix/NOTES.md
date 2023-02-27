```
if target > matrix[mid][-1]:
top = mid + 1
elif target < matrix[mid][0]:
bot = mid - 1
else:                                # it lies in the range
row = mid
break
```
-> Find out the orw it exists in
-> Search for the element in the row