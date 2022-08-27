class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
# Kadane Code - 1

        n = len(arr)
        cur_sum = arr[0]   # because we are traversing from '1'
        max_sum = arr[0]  
        
        for i in range(1,n):
          
            cur_sum = max(cur_sum + arr[i], arr[i]) # if the ele is greater than the whole sub array 
          
            max_sum = max(max_sum, cur_sum) # max of all subarrays
        
        return max_sum
        
        
        
 # Kadane Code - 2

        n = len(nums)
        curr_sum = 0
        max_sum = nums[0]
        
        for i in range(n):

            if curr_sum < 0:       # iff the sum is neg make it 0
                curr_sum = 0
            # IMP ! SUM Should be done after the comparision else negative nums wont be counted
            curr_sum += nums[i]    
                
            max_sum = max(max_sum,curr_sum)
                
        return max_sum
            
        
