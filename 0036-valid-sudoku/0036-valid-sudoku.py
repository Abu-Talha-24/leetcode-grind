class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)
        
        n = len(board)
        
        for i in range(n):
            
            for j in range(n):
                num = board[i][j]
                if num == ".":
                    continue
                if num != '.' and num in rows[i] or num in cols[j]:
                    print(num, i, j)
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                
                gr = 0
                if i <=2:
                    if j <= 2:
                        gr = 1
                    elif j <= 5:
                        gr = 2
                    elif j <= 8:
                        gr = 3
                elif i <= 5:
                    if j <= 2:
                        gr = 4
                    elif j <= 5:
                        gr = 5
                    elif j <= 8:
                        gr = 6
                elif j <= 8:
                    if j <= 2:
                        gr = 7
                    elif j <= 5:
                        gr = 8
                    elif j <= 8:
                        gr = 9
                
                if num in grids[gr]:
                    print(num, "grid", gr)
                    return False
                
                grids[gr].add(num)
                
            
        return True
                
        