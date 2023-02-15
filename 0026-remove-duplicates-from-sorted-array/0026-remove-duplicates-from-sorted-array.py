class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        prev = 0
        
        for i in range(1, n):
            
            if nums[i] == nums[prev]:
                continue
            elif nums[i] > nums[prev]:
                prev += 1
                nums[prev] = nums[i]
                
        print(prev, nums)
        return prev+1
            