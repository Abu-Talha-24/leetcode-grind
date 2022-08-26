class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = [0]*len(nums)
        ind = len(nums) - 1
        while (l <= r):
            if abs(nums[l]) > abs(nums[r]):
                res[ind] = pow(nums[l],2)
                l += 1
            else:
                res[ind] = pow(nums[r],2)
                r -= 1
            ind -= 1
        return res
            
        
        