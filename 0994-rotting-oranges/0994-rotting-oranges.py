class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        
        q = deque()
        fresh = 0
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if not q and not fresh:
            return 0
        
        t = -1
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if grid[row][col] == 2: # if rotten
                    for dr, dc in dirs:
                        r, c = row + dr, col + dc
                        if r in range(rows) and c in range(cols) and grid[r][c] == 1: # if in range and fresh
                            grid[r][c] = 2 # make em rotten
                            fresh -= 1
                            q.append((r, c))      
            t += 1
            
        if fresh > 0:
            return -1
        
        return t
            

            