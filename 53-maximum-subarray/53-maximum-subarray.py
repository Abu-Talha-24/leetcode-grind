class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        
        n = len(arr)
        cur_sum = arr[0]
        max_sum = arr[0]
        
        for i in range(1,n):
            cur_sum = max(cur_sum + arr[i], arr[i])
            
            max_sum = max(max_sum, cur_sum)
        
        return max_sum
        
#         n = len(nums)
#         curr_sum = 0
#         max_sum = nums[0]
        
#         for i in range(n):

#             if curr_sum < 0:
#                 curr_sum = 0
#             curr_sum += nums[i]
                
#             max_sum = max(max_sum,curr_sum)
                
#         return max_sum
            
        