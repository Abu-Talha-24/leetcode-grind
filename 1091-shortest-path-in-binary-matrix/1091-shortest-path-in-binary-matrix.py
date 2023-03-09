class Solution:    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
            n = len(grid)
            if grid[0][0] == 1 or grid[n-1][n-1] == 1:
                return -1
            
            q = deque()
            visit = set()
            q.append((0,0,1)) # indice, dist
            visit.add((0,0))
            dirs = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1,1], [1,-1], [-1,1]]

            while q:
                row, col, length = q.popleft()
                if row == n -1 and col == n - 1:
                    return length
                for dr, dc in dirs: 
                    r, c = row + dr, col + dc
                    if r in range(n) and c in range(n) and (r, c) not in visit and grid[r][c] == 0:
                        q.append((r, c, length + 1))
                        visit.add((r, c))

                        
            return -1