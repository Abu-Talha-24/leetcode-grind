class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        s = sum(nums)
        res = [float("inf"), 0]
        prefix = 0
        
        for i in range(n):
            prefix += nums[i]
            if i == n-1:
                diff = abs( prefix // (i+1) - 0 )
            else:
                diff = abs( prefix // (i+1) - (s - prefix) // (n-1-i) )

            if diff < res[0]:
                res = [diff, i]
        
        return res[1]
            
        
        