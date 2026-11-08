class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        squares = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                square = (i // 3, j // 3)
                row = i
                col = j
                if board[i][j] in squares[square] or board[i][j] in rows[i] or board[i][j] in cols[j]:
                    return False
                
                squares[square].add(board[i][j])
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])

        return True
        