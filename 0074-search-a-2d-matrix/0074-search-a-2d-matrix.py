class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        row = 0
        
        while top <= bot:
            mid = (top + bot) // 2
            
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                row = mid
                break
        
        if not top <= bot: # if out of bounds
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
        