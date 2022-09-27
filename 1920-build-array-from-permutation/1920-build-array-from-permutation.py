class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        for i in range(n):    # using modulo to save the ans and original num
            nums[i] = nums[i] + (n * (nums[nums[i]] % n) )
        # nums[i] // n always gives 0 (as 0 < nums[i] < n)
        # second_term // n gives the req answer
        # Modulo is to get the value back in to the range(< n) when prev value is accessed
            
        for i in range(n):    # retreiving the value 
            nums[i] = nums[i] // n
    
        return nums
            
        
        