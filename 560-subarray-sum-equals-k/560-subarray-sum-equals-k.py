class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		count = 0
		prefsum = 0
		d = {0:1}

		for i in range(len(nums)):
			prefsum += nums[i]
            # If the (prefixsum - target) occured as a prefix already
			if prefsum-k in d:
				count += d[prefsum-k]  # every occurence is the start of subarray
            
            # Storing the no. of times a prefix sum occurs
			if prefsum not in d:
				d[prefsum] = 1
			else:
				d[prefsum] = d[prefsum]+1

		return count
        
        
   # Can't use SLIDING WINDOW FOR NEGATIVE NUMBERS
#         n = len(arr)
#         start = 0
#         end = 0
#         c_sum = arr[0]
#         count = 0
        
#         while (start < n):
                
#             if start > end:
#                 end = start
#                 c_sum = arr[start]
            
#             if c_sum == k:
#                 count += 1
#                 c_sum = c_sum - arr[start]
#                 start +=1
            
#             if c_sum < k:
#                 if end == len(arr) - 1:
#                     break
#                 end += 1
#                 c_sum += arr[end]
#             elif c_sum > k:
#                 c_sum = c_sum - arr[start]
#                 start += 1
        
#         return count