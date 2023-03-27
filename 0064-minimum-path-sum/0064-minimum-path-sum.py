class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        # add a extra row and column
        res = [[float("inf")] * (COLS + 1) for r in range(ROWS + 1)]
        # initialise the bottom right value to 0
        res[ROWS - 1][COLS] = 0
        # going bottom - up
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                # calculate the sum by taking min of up and right(reverse)
                # res[r][c] is the sum to reach from (r,c) to the bottom right pos
                res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])
        
        # res[0][0] is the MINsum when traversed from 0,0 to bottom right pos
        return res[0][0]
    