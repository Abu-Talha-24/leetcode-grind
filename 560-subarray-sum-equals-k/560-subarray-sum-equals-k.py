class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		ans=0
		prefsum=0
		d={0:1}

		for num in nums:
			prefsum = prefsum + num

			if prefsum-k in d:
				ans = ans + d[prefsum-k]

			if prefsum not in d:
				d[prefsum] = 1
			else:
				d[prefsum] = d[prefsum]+1

		return ans
        
        
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