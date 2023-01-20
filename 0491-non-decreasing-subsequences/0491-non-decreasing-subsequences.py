class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
		## APPROACH : BACKTRACKING ##
		## TIME COMPLEXITY : O(N^2) ##
		## SPACE COMPLEXITY : O(N^2) ##
        def backtrack(curr, nums):
            # if not non-decreasing -> return 
            if ( len(curr) >= 2 and curr[-1] < curr[-2] ):
                return
            # if not in result -> add to result
            if ( len(curr) >= 2 and curr[:] not in result ):
                result.add(curr[:])
            for i in range(len(nums)):
                # using tuples for curr instead of list
                backtrack( curr + (nums[i],), nums[i+1:] )  
                
        result = set()
        
        backtrack( (), nums)
        return result