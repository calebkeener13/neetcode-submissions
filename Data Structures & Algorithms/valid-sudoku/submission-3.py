class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            currSet = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                if board[i][j] in currSet:
                    return False
                
                currSet.add(board[i][j])


        for i in range(len(board)):
            currSet = set()
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue

                if board[j][i] in currSet:
                    return False
                
                currSet.add(board[j][i])

        squares = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                square = (i // 3, j // 3)
                if board[i][j] in squares[square]:
                    return False
                
                squares[square].add(board[i][j])

        return True
        