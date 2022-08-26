class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return nums
        
        i = 0
        ins = 0
        
        while (i < n):
            if nums[i] != 0:
                nums[i], nums[ins] = nums[ins], nums[i]
                ins += 1
            i += 1
        return nums
        