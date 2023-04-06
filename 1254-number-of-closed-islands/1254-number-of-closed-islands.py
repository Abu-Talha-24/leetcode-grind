class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 1 - Water , 0 - Land
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = 0
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS): # out of bounds
                return 0 # False
            
            if grid[r][c] == 1 or (r, c) in visit:
                return 1 # True
            
            visit.add((r, c))
            
            # if any of it is 0 return 0 , else 1
            return min(dfs(r+1, c), dfs(r-1, c), dfs(r, c+1), dfs(r, c-1))
        
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c] and (r, c) not in visit: # not water
                    res += dfs(r, c)
        
        return res