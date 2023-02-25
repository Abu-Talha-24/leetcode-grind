class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = ins = 0
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        while (i < n):
            if nums[i] < 1: # sort all 0's from left (ins)
                swap(i, ins)
                ins += 1
            i+= 1
        
        i = ins = n-1
        
        while (i >= 0): 
            if nums[i] > 1: # sort all 2's from right (ins)
                swap(i, ins)
                ins -= 1
            i-= 1
                   