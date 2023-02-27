class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])
        
        top, bot = 0, rows - 1
        row = 0
        
        while top <= bot:
            mid = (top + bot) // 2
            
            if target > matrix[mid][-1]: # if it's next array
                top = mid + 1
            elif target < matrix[mid][0]: # if it's prev arrays
                bot = mid - 1
            else: # else it is that array
                row = mid
                break
                
        if not top <= bot:
            return False
        
        l, r = 0, cols - 1        
        while l <= r:
            mid = (l + r) // 2
            
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        
        return False
            