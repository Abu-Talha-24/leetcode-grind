class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p = 0
        for i in range(n):
            if nums[i] < 1:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        
        p = n-1
        
        for i in range(n-1, -1, -1):
            if nums[i] > 1:
                nums[p], nums[i] = nums[i], nums[p]
                p -= 1
            
            