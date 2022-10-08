class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # set col, posDiag, negDiag
        col = set()
        posDiag = set()
        negDiag = set()
        
        
        # board and res
        res = []
        board = [["."]* n for i in range(n) ]
        
        #backtrack fxn
        def backtrack(r):
            # if row reaches end
            if (r == n):
                # parse the board into an array and add to res
                copy = ["".join(row) for row in board]
                res.append(copy)
                return # return at this condition
        
            # go through the board
            for c in range(n):
                # check if it is a valid position
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue # skip if invalid
                
                # add it to one of the position
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                
                # backtrack - placing the next queen in next row
                backtrack(r + 1)
                
                # remove the queen from that position
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
                
        backtrack(0) #starting form 0th row
        return res