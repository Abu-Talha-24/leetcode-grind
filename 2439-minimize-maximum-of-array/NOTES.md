**avg = sum / total no. of elements**
​
*1st ->*
nums[0]  / (0 + 1)
*2nd ->*
nums[0] + nums[1] + 1 / (1 + 1)
*3rd ->*
nums[0] + nums[1] + nums[2] + (1 + 1) / (2 + 1)
​
numerator has "+ index" or else use math.ceil()
denominator has "+1 cuz" `total no. of elements = ( index + 1 )`
​
**Solution is the max of Average of the sub arrays**