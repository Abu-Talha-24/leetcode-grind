class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowset = defaultdict(set)
        colset = defaultdict(set)
        gridset = defaultdict(set)
        
        n = len(board)
        
        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num == ".":
                    continue
                
                if num in rowset[i]:
                    return False
                elif num in colset[j]:
                    return False
                elif num in gridset[(i // 3, j // 3)]:
                    return False
                
                rowset[i].add(num)
                colset[j].add(num)
                gridset[(i//3, j//3)].add(num)
            
        return True
        