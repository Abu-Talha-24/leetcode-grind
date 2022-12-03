class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = [1] * n
        
        for i in range(n-1):
            prefix[i+1] = prefix[i] * nums[i]
        
        prod = 1
        for i in range(n-1, 0, -1):
            prod = nums[i] * prod
            prefix[i-1] = prefix[i-1] * prod
        
        return prefix
            
        