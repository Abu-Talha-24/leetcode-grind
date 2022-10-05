class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        result = 0
        nrow = len(grid)
        ncol = len(grid[0])
        nums = []
        
        for r in range(nrow):
            for c in range(ncol):
                nums.append(grid[r][c])

        nums.sort()
        median = nums[len(nums) // 2]
        
        for num in nums:
            diff = abs(num - median)    
            if diff % x !=0:
                return -1
            else:
                result += diff // x
        
        return result
        
        
            
        