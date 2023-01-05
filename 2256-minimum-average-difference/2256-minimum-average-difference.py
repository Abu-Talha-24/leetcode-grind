class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        s = sum(nums)
        ans, mini = 0, float("inf")
        prefix = 0
        
        for i in range(n):
            s -= nums[i]
            prefix += nums[i]
            if i == n-1:
                avg = abs( (prefix) // (i+1) )
            else:
                avg = abs( (prefix) // (i+1) - (s // (n - (i+1)) ) )
            if avg < mini:
                ans, mini = i, avg
        
        return ans
                
                

            
    
            