class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        ins = 0
        while (i < n):
            if nums[i] < 1:
                nums[i], nums[ins] = nums[ins], nums[i]
                ins += 1
            i+= 1
        
        i = ins = n-1
        while (i >= 0):
            if nums[i] > 1:
                nums[i], nums[ins] = nums[ins], nums[i]
                ins -= 1
            i-= 1
        
        
        