class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i, prev = 0, -1
        
        while (i < n):
            if nums[i] != val:
                if (i - prev) != 1: # if empty space
                    prev += 1
                    nums[prev] = nums[i]
                else:
                    prev = i
            elif nums[i] == val:
                while i < n and nums[i] == val:
                    i+=1
                continue
            i += 1                
        
        print(nums)
        return prev+1